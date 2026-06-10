"""
chains.py — LangChain logic for AI Interview Coach
Contains:
  - QuestionGeneratorChain  : generates interview questions
  - AnswerEvaluatorChain    : evaluates candidate answers
  - SessionSummaryChain     : produces end-of-session report
  - Output Parsers          : Pydantic-based structured outputs
"""

from __future__ import annotations
import os
from typing import List

from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()


# ─── LLM selector ────────────────────────────────────────────
def get_llm():
    provider = os.getenv("LLM_PROVIDER", "openai").lower()
    if provider == "groq":
        from langchain_groq import ChatGroq
        return ChatGroq(
            model="llama-3.1-8b-instant",
            api_key=os.getenv("GROQ_API_KEY"),
            temperature=0.7,
        )
    elif provider == "huggingface":
        from langchain_huggingface import HuggingFaceEndpoint
        return HuggingFaceEndpoint(
            repo_id=os.getenv("HF_MODEL_ID", "mistralai/Mistral-7B-Instruct-v0.3"),
            huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
            temperature=0.7,
            max_new_tokens=1024,
        )
    else:
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.7,
            api_key=os.getenv("OPENAI_API_KEY"),
        )


# ─── Pydantic Output Models ───────────────────────────────────

class InterviewQuestion(BaseModel):
    question: str = Field(description="Full text of the interview question")
    category: str = Field(description="Question type: Behavioral / Technical / Situational / HR")
    difficulty: str = Field(description="Difficulty level: Easy / Medium / Hard")
    tip: str = Field(description="One-sentence tip for a good answer")


class QuestionSet(BaseModel):
    job_title: str = Field(description="The job title being interviewed for")
    questions: List[InterviewQuestion] = Field(description="List of interview questions")


class AnswerEvaluation(BaseModel):
    score: int = Field(description="Score out of 10", ge=0, le=10)
    strengths: List[str] = Field(description="2-3 strengths of the answer")
    improvements: List[str] = Field(description="2-3 areas needing improvement")
    ideal_answer_outline: str = Field(description="2-3 sentence outline of an ideal answer")
    framework_used: str = Field(description="Did the candidate use STAR/CAR framework? Yes / No / Partially")


class SessionSummary(BaseModel):
    overall_score: float = Field(description="Average score out of 10")
    strongest_area: str = Field(description="The candidate's strongest area")
    weakest_area: str = Field(description="The candidate's weakest area needing development")
    top_improvements: List[str] = Field(description="Top 3 improvement recommendations")
    readiness_level: str = Field(description="Readiness level: Not Ready / Needs Work / Almost Ready / Ready")
    next_steps: List[str] = Field(description="Concrete next steps to prepare better")


# ─── Chain 1: Question Generator ─────────────────────────────

def make_question_generator_chain():
    parser = PydanticOutputParser(pydantic_object=QuestionSet)
    fmt = parser.get_format_instructions()

    template = """You are an expert technical interviewer and HR coach.
Generate a structured set of interview questions for the given job.
Mix different types: Behavioral, Technical, Situational, and HR questions.
IMPORTANT: Generate all questions, tips, and text in {language} language.

OUTPUT FORMAT:
{format_instructions}

IMPORTANT: Respond ONLY with valid JSON matching the schema above. No extra text, no markdown.

Job Title: {job_title}
Experience Level: {experience_level}
Focus Areas: {focus_areas}
Number of Questions: {num_questions}
Language: {language}

Generate diverse, realistic interview questions that a top company would ask."""

    prompt = PromptTemplate(
        template=template,
        input_variables=["job_title", "experience_level", "focus_areas", "num_questions", "language"],
        partial_variables={"format_instructions": fmt},
    )

    chain = prompt | get_llm() | parser
    return chain, parser


# ─── Chain 2: Answer Evaluator ────────────────────────────────

def make_answer_evaluator_chain():
    parser = PydanticOutputParser(pydantic_object=AnswerEvaluation)
    fmt = parser.get_format_instructions()

    template = """You are a strict but fair interview coach evaluating a candidate's answer.
Score based on clarity, relevance, depth, and use of concrete examples.
IMPORTANT: Write all feedback, strengths, improvements, and ideal answer in {language} language.

OUTPUT FORMAT:
{format_instructions}

IMPORTANT: Respond ONLY with valid JSON matching the schema above. No extra text, no markdown.

Job Title: {job_title}
Interview Question: {question}
Question Category: {category}
Language: {language}

Candidate's Answer:
{answer}

Evaluate this answer thoroughly."""

    prompt = PromptTemplate(
        template=template,
        input_variables=["job_title", "question", "category", "answer", "language"],
        partial_variables={"format_instructions": fmt},
    )

    chain = prompt | get_llm() | parser
    return chain, parser


# ─── Chain 3: Session Summary ─────────────────────────────────

def make_session_summary_chain():
    parser = PydanticOutputParser(pydantic_object=SessionSummary)
    fmt = parser.get_format_instructions()

    template = """You are a career coach providing a comprehensive interview performance review.
Analyze all Q&A pairs and individual scores to give honest, actionable feedback.
IMPORTANT: Write the entire summary, recommendations, and next steps in {language} language.

OUTPUT FORMAT:
{format_instructions}

IMPORTANT: Respond ONLY with valid JSON matching the schema above. No extra text, no markdown.

Job Title: {job_title}
Experience Level: {experience_level}
Language: {language}

Full Interview Session:
{session_data}

Individual scores: {scores}

Provide a comprehensive performance summary with actionable next steps."""

    prompt = PromptTemplate(
        template=template,
        input_variables=["job_title", "experience_level", "session_data", "scores", "language"],
        partial_variables={"format_instructions": fmt},
    )

    chain = prompt | get_llm() | parser
    return chain, parser
