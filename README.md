# AI Interview Coach

**Practice job interviews with an AI coach that generates tailored questions, scores your answers, and gives instant, structured feedback — in 5 languages, with optional voice mode.**

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/built%20with-Streamlit-FF4B4B)
![LangChain](https://img.shields.io/badge/powered%20by-LangChain-1C3C3C)
![License](https://img.shields.io/badge/license-MIT-green)

## Features

- **Tailored question generation** — enter a job title, experience level, and focus areas; the AI generates a mix of Behavioral, Technical, Situational, and HR questions with difficulty tags and hints.
- **Instant structured feedback** — every answer is scored out of 10 with concrete strengths, areas to improve, an ideal-answer outline, and whether you used the STAR framework.
- **Session report** — after the last question, get an overall score, strongest/weakest areas, a score-breakdown chart, and a prioritized list of next steps.
- **Voice interview mode** — questions are read aloud (gTTS) and you can answer by recording your voice, transcribed automatically (OpenAI Whisper).
- **Multi-language support** — full UI and AI-generated content in English, Arabic (RTL), French, German, and Spanish.
- **Dark / light theme** — a custom "futuristic" UI theme with a toggle.
- **Pluggable LLM backend** — works with OpenAI, Groq, or a Hugging Face inference endpoint, switchable via one environment variable.

## How it works

1. Enter a job title, experience level, optional focus areas, and how many questions you want.
2. Answer each question (written or voice) — try the STAR method: Situation → Task → Action → Result.
3. Get instant AI feedback on each answer: score, strengths, improvements, and an ideal answer.
4. Review your full session report: overall readiness level, strongest/weakest areas, and next steps.

Under the hood, three LangChain chains (in `chains.py`) handle question generation, answer evaluation, and session summarization, each using a Pydantic schema so the LLM's output is always structured and predictable.

## Tech Stack

| Layer          | Technology                                      |
|----------------|--------------------------------------------------|
| UI              | Streamlit                                        |
| AI orchestration | LangChain (`langchain`, `langchain-core`)        |
| LLM providers   | OpenAI (`gpt-4o-mini`), Groq (`llama-3.1-8b-instant`), or Hugging Face |
| Structured output | Pydantic                                       |
| Voice           | gTTS (text-to-speech), OpenAI Whisper (speech-to-text), `audio-recorder-streamlit` |

## Quick Start

```bash
# 1. Clone
git clone https://github.com/Abdelrahmanemad0/ai-interview-coach.git
cd ai-interview-coach

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment variables (see below)
cp .env.example .env   # then fill in your API key(s)

# 4. Run
streamlit run app.py
```

## Environment Variables

| Variable | Required | Purpose |
|----------|:--------:|---------|
| `LLM_PROVIDER` | No | `openai` (default), `groq`, or `huggingface` — selects which backend `get_llm()` uses |
| `OPENAI_API_KEY` | If using OpenAI | API key for `gpt-4o-mini` |
| `GROQ_API_KEY` | If using Groq | API key for `llama-3.1-8b-instant` |
| `HUGGINGFACEHUB_API_TOKEN` / `HF_MODEL_ID` | If using Hugging Face | Token and model repo id for the inference endpoint |

Voice-mode transcription additionally expects `OPENAI_API_KEY` to be set, since it calls the Whisper API directly.

## Project Structure

```
ai-interview-coach/
├── app.py              # Streamlit UI: setup, interview, evaluation, and summary stages
├── chains.py           # LangChain chains + Pydantic schemas (questions, evaluation, summary)
├── requirements.txt    # Python dependencies
├── runtime.txt         # Python version pin for deployment platforms
├── Procfile            # Process definition for Heroku-style/Streamlit deployment
└── .streamlit/         # Streamlit configuration
```

## Deploying for free

This app is ready for [Streamlit Community Cloud](https://streamlit.io/cloud) (free): connect this repo, set the entry point to `app.py`, and add your `OPENAI_API_KEY` (or `GROQ_API_KEY` + `LLM_PROVIDER=groq`) as a secret. No server management required.

## License

MIT — see [`LICENSE`](LICENSE).
