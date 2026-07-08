#  AI Interview Coach

AI-powered mock interview coach that generates role-specific questions, scores your spoken or written answers with structured feedback (STAR framework), and produces a full session report — in 5 languages, with an optional voice mode.

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white">
  <img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-1.37-FF4B4B?logo=streamlit&logoColor=white">
  <img alt="LangChain" src="https://img.shields.io/badge/LangChain-0.2-1C3C3C">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-yellow.svg">
  <img alt="Live Demo" src="https://img.shields.io/badge/demo-live-brightgreen">
</p>

**[Live demo →](#deployment)** &nbsp;·&nbsp; Built with Streamlit + LangChain, LLM-agnostic (Groq / OpenAI / HuggingFace)

---

## Features

- **Role-tailored questions** — generates a mix of Behavioral, Technical, Situational, and HR questions for any job title, experience level, and focus area.
- **Structured AI feedback** — every answer is scored 0–10 with strengths, areas to improve, an ideal-answer outline, and whether you used the STAR framework.
- **Voice interviews** — record spoken answers directly in the browser; transcribed via Whisper.
- **Session report** — overall score, strongest/weakest area, readiness level, and concrete next steps after the full session.
- **5 languages** — English, Arabic (RTL layout), French, German, Spanish — questions, feedback, and UI all localize together.
- **Dark / light theme** with a custom, animated UI (no default Streamlit chrome).
- **Provider-agnostic LLM layer** — swap between Groq (`llama-3.1-8b-instant`), OpenAI (`gpt-4o-mini`), or a HuggingFace endpoint via a single environment variable.

## Architecture

```
┌─────────────────┐        ┌──────────────────────────┐
│   Streamlit UI    │──────▶│  chains.py (LangChain)    │
│   (app.py)        │        │  ─ QuestionGenerator      │
│  - session state  │◀──────│  ─ AnswerEvaluator         │
│  - voice capture   │        │  ─ SessionSummary          │
│  - i18n / theming  │        │  Pydantic-structured output│
└──────────────────┘        └────────────┬─────────────┘
                                          │
                              ┌───────────▼───────────┐
                              │   LLM Provider          │
                              │   Groq / OpenAI / HF    │
                              └────────────────────────┘
```

Each LLM call is a LangChain pipeline (`prompt | llm | PydanticOutputParser`) that forces the model to return schema-validated JSON — questions, evaluations, and the final report are strongly typed (`chains.py`), so the UI never has to parse free-form text.

## Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit, custom CSS/JS injection |
| Orchestration | LangChain (`langchain`, `langchain-core`) |
| LLM providers | Groq, OpenAI, HuggingFace Inference Endpoints |
| Structured output | Pydantic v2 |
| Voice | `audio-recorder-streamlit`, OpenAI Whisper (transcription), gTTS (speech synthesis) |
| Deployment | Streamlit Community Cloud / Heroku-style `Procfile` |

## Quick Start

```bash
# 1. Clone
git clone https://github.com/Abdelrahmanemad0/ai-interview-coach.git
cd ai-interview-coach

# 2. Install dependencies (Python 3.11)
pip install -r requirements.txt

# 3. Configure secrets
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# then fill in your GROQ_API_KEY (or switch LLM_PROVIDER to "openai"/"huggingface")

# 4. Run
streamlit run app.py
```

The app is also deployable as-is to any Heroku-style host via the included `Procfile`:

```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

## Configuration

All configuration lives in `.streamlit/secrets.toml` (local) or your host's secrets manager (production). See `.streamlit/secrets.toml.example` for the full list:

| Variable | Required | Purpose |
|---|---|---|
| `LLM_PROVIDER` | No (default `openai`) | `groq`, `openai`, or `huggingface` |
| `GROQ_API_KEY` | If using Groq | Groq API key |
| `OPENAI_API_KEY` | If using OpenAI | OpenAI API key (also used for Whisper transcription) |
| `HUGGINGFACEHUB_API_TOKEN` / `HF_MODEL_ID` | If using HuggingFace | HF Inference Endpoint credentials |

`.streamlit/secrets.toml` is git-ignored — never commit real keys.

## Project Structure

```
ai-interview-coach/
├── app.py                        # Streamlit UI, session state, i18n, voice capture
├── chains.py                     # LangChain chains + Pydantic schemas (questions/eval/report)
├── requirements.txt
├── Procfile                      # Heroku-style start command
├── runtime.txt                   # Python version pin
├── .streamlit/
│   └── secrets.toml.example      # Template for local secrets
└── .github/workflows/ci.yml      # Lint + compile check on push/PR
```

## Deployment

Live on **Streamlit Community Cloud**, auto-deployed from `main`.

To deploy your own copy:
1. Fork this repo.
2. Go to [share.streamlit.io](https://share.streamlit.io), connect your GitHub, and pick the fork.
3. Set `app.py` as the entry point and add your secrets (same keys as `.streamlit/secrets.toml.example`) in the app's **Settings → Secrets**.

## Roadmap

- [ ] Automated tests for `chains.py` output parsing
- [ ] Persist session history across visits (currently in-memory per session)
- [ ] Add a "company-specific" question mode (e.g. tailor to a target company's known interview style)

## License

MIT — see [LICENSE](LICENSE).
