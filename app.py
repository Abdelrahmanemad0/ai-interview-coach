"""
app.py — AI Interview Coach  (Futuristic UI)
"""

import streamlit as st

st.set_page_config(
    page_title="AI Interview Coach",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Orbitron:wght@700;800;900&display=swap');

html, body, [class*="css"] { font-family: 'Space Grotesk', sans-serif; }

/* ── Hide Streamlit chrome ── */
#MainMenu{visibility:hidden;}header{visibility:hidden;}footer{visibility:hidden;}
[data-testid="stToolbar"]{display:none!important;}
[data-testid="stDecoration"]{display:none!important;}
[data-testid="stStatusWidget"]{display:none!important;}
.viewerBadge_container__1QSob{display:none!important;}

/* ── Animated gradient background ── */
.stApp {
    background: #020208;
    color: #c8d0ff;
}
.stApp::before {
    content: '';
    position: fixed; top: 0; left: 0; right: 0; bottom: 0;
    background:
        radial-gradient(ellipse at 10% 20%, rgba(99,51,255,0.12) 0%, transparent 50%),
        radial-gradient(ellipse at 90% 80%, rgba(0,210,255,0.10) 0%, transparent 50%),
        radial-gradient(ellipse at 50% 50%, rgba(255,51,153,0.06) 0%, transparent 60%);
    pointer-events: none; z-index: 0;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #06060f 0%, #0a0a18 100%) !important;
    border-right: 1px solid rgba(99,51,255,0.3) !important;
}
[data-testid="stSidebar"] * { color: #7070a0 !important; }
[data-testid="stSidebar"] strong { color: #a0a0d0 !important; }
[data-testid="stSidebar"] h3 {
    font-family: 'Orbitron', sans-serif !important;
    background: linear-gradient(90deg, #6333ff, #00d2ff) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
}

/* ── Progress bar ── */
.stProgress > div > div {
    background: linear-gradient(90deg, #6333ff, #00d2ff) !important;
    border-radius: 99px !important;
}
[data-testid="stProgress"] > div {
    background: rgba(99,51,255,0.15) !important;
    border-radius: 99px !important;
}

/* ── Headings ── */
h1 {
    font-family: 'Orbitron', sans-serif !important;
    background: linear-gradient(135deg, #6333ff 0%, #00d2ff 50%, #ff3399 100%);
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    font-size: 2.8rem !important;
    letter-spacing: 1px !important;
}
h2, h3 {
    font-family: 'Orbitron', sans-serif !important;
    color: #a0c0ff !important;
    letter-spacing: 0.5px !important;
}

/* ── Glow card ── */
.q-card {
    background: linear-gradient(135deg, rgba(99,51,255,0.08) 0%, rgba(0,210,255,0.05) 100%);
    border: 1px solid rgba(99,51,255,0.4);
    border-radius: 16px; padding: 28px; margin-bottom: 16px;
    box-shadow: 0 0 30px rgba(99,51,255,0.1), inset 0 1px 0 rgba(255,255,255,0.05);
    position: relative; overflow: hidden;
}
.q-card::before {
    content: '';
    position: absolute; top: 0; left: 0; right: 0; height: 1px;
    background: linear-gradient(90deg, transparent, rgba(99,51,255,0.8), rgba(0,210,255,0.8), transparent);
}
.q-label {
    font-size: 10px; font-weight: 700; letter-spacing: 3px;
    color: rgba(99,51,255,0.7); text-transform: uppercase; margin-bottom: 12px;
    font-family: 'Orbitron', sans-serif;
}
.q-text { font-size: 18px; font-weight: 500; color: #e0e8ff; line-height: 1.65; }

/* ── Tags ── */
.tag {
    display: inline-block; padding: 4px 12px;
    border-radius: 20px; font-size: 11px; font-weight: 600;
    margin-top: 14px; margin-right: 6px; letter-spacing: 0.5px;
}
.tag-behavioral  {
    background: rgba(99,51,255,0.15); color: #a78bfa;
    border: 1px solid rgba(99,51,255,0.5);
    box-shadow: 0 0 8px rgba(99,51,255,0.2);
}
.tag-technical   {
    background: rgba(0,210,255,0.1); color: #00d2ff;
    border: 1px solid rgba(0,210,255,0.4);
    box-shadow: 0 0 8px rgba(0,210,255,0.15);
}
.tag-situational {
    background: rgba(255,153,0,0.1); color: #ff9900;
    border: 1px solid rgba(255,153,0,0.4);
    box-shadow: 0 0 8px rgba(255,153,0,0.15);
}
.tag-hr {
    background: rgba(255,51,153,0.1); color: #ff3399;
    border: 1px solid rgba(255,51,153,0.4);
    box-shadow: 0 0 8px rgba(255,51,153,0.1);
}

/* ── Score circle ── */
.score-circle {
    display: inline-flex; align-items: center; justify-content: center;
    width: 68px; height: 68px; border-radius: 50%;
    font-family: 'Orbitron', sans-serif; font-size: 22px; font-weight: 900;
    position: relative;
}
.score-high {
    background: rgba(0,255,150,0.08); color: #00ff96;
    border: 2px solid #00ff96;
    box-shadow: 0 0 20px rgba(0,255,150,0.3), inset 0 0 10px rgba(0,255,150,0.05);
}
.score-mid  {
    background: rgba(255,200,0,0.08); color: #ffc800;
    border: 2px solid #ffc800;
    box-shadow: 0 0 20px rgba(255,200,0,0.3), inset 0 0 10px rgba(255,200,0,0.05);
}
.score-low  {
    background: rgba(255,51,100,0.08); color: #ff3364;
    border: 2px solid #ff3364;
    box-shadow: 0 0 20px rgba(255,51,100,0.3), inset 0 0 10px rgba(255,51,100,0.05);
}

/* ── Eval boxes ── */
.eval-box {
    background: rgba(6,6,20,0.8);
    border-left: 3px solid;
    border-radius: 0 12px 12px 0; padding: 14px 18px; margin: 8px 0;
    font-size: 14px; line-height: 1.7; color: #b0b8e0;
    backdrop-filter: blur(4px);
}
.eval-strength {
    border-color: #00ff96;
    box-shadow: -2px 0 12px rgba(0,255,150,0.15);
}
.eval-improve  {
    border-color: #ffc800;
    box-shadow: -2px 0 12px rgba(255,200,0,0.15);
}
.eval-ideal    {
    border-color: #00d2ff;
    box-shadow: -2px 0 12px rgba(0,210,255,0.15);
}

/* ── Readiness badge ── */
.readiness {
    display: inline-block; padding: 6px 20px; border-radius: 20px;
    font-weight: 700; font-size: 13px; font-family: 'Orbitron', sans-serif;
    letter-spacing: 1px; text-transform: uppercase;
}
.r-ready     {
    background: rgba(0,255,150,0.1); color: #00ff96;
    border: 1px solid rgba(0,255,150,0.5);
    box-shadow: 0 0 16px rgba(0,255,150,0.2);
}
.r-almost    {
    background: rgba(0,210,255,0.1); color: #00d2ff;
    border: 1px solid rgba(0,210,255,0.5);
    box-shadow: 0 0 16px rgba(0,210,255,0.2);
}
.r-needs     {
    background: rgba(255,200,0,0.1); color: #ffc800;
    border: 1px solid rgba(255,200,0,0.5);
    box-shadow: 0 0 16px rgba(255,200,0,0.2);
}
.r-not-ready {
    background: rgba(255,51,100,0.1); color: #ff3364;
    border: 1px solid rgba(255,51,100,0.5);
    box-shadow: 0 0 16px rgba(255,51,100,0.2);
}

/* ── Metric cards ── */
[data-testid="stMetric"] {
    background: linear-gradient(135deg, rgba(99,51,255,0.08), rgba(0,210,255,0.05)) !important;
    border: 1px solid rgba(99,51,255,0.3) !important;
    border-radius: 14px !important; padding: 18px !important;
    box-shadow: 0 0 20px rgba(99,51,255,0.08) !important;
}
[data-testid="stMetricValue"] {
    font-family: 'Orbitron', sans-serif !important; font-weight: 900 !important;
    background: linear-gradient(90deg, #6333ff, #00d2ff) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    font-size: 1.8rem !important;
}
[data-testid="stMetricLabel"] {
    color: #5a5a8a !important; font-size: 11px !important;
    text-transform: uppercase; letter-spacing: 1.5px;
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, #6333ff 0%, #00d2ff 100%) !important;
    color: #fff !important; border: none !important;
    border-radius: 10px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 700 !important; font-size: 14px !important;
    padding: 0.6rem 1.8rem !important; letter-spacing: 0.5px !important;
    box-shadow: 0 0 20px rgba(99,51,255,0.4) !important;
    transition: all 0.2s !important;
}
.stButton > button:hover {
    box-shadow: 0 0 30px rgba(0,210,255,0.5) !important;
    transform: translateY(-1px) !important;
}

/* ── Inputs ── */
.stTextArea textarea, .stTextInput input {
    background: rgba(6,6,20,0.8) !important; color: #c8d0ff !important;
    border: 1px solid rgba(99,51,255,0.3) !important;
    border-radius: 10px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    backdrop-filter: blur(4px) !important;
}
.stTextArea textarea:focus, .stTextInput input:focus {
    border-color: #00d2ff !important;
    box-shadow: 0 0 16px rgba(0,210,255,0.2) !important;
}
.stSelectbox > div > div {
    background: rgba(6,6,20,0.8) !important;
    border: 1px solid rgba(99,51,255,0.3) !important;
    border-radius: 10px !important; color: #c8d0ff !important;
}

/* ── Slider ── */
[data-testid="stSlider"] > div > div > div {
    background: linear-gradient(90deg, #6333ff, #00d2ff) !important;
}

/* ── Divider ── */
hr {
    border: none !important;
    border-top: 1px solid rgba(99,51,255,0.2) !important;
    margin: 1.5rem 0 !important;
}

/* ── Alert ── */
.stAlert {
    border-radius: 10px !important;
    background: rgba(6,6,20,0.8) !important;
    backdrop-filter: blur(4px) !important;
}
.stInfo {
    border-color: rgba(0,210,255,0.4) !important;
    color: #a0c0ff !important;
}

/* ── Expander ── */
[data-testid="stExpander"] {
    background: rgba(6,6,20,0.6) !important;
    border: 1px solid rgba(99,51,255,0.25) !important;
    border-radius: 12px !important;
    backdrop-filter: blur(4px) !important;
}

/* ── Spinner ── */
.stSpinner > div { border-top-color: #6333ff !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #020208; }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #6333ff, #00d2ff);
    border-radius: 3px;
}
</style>
""", unsafe_allow_html=True)


# ─── Session state ─────────────────────────────────────────
defaults = {
    "stage": "setup",
    "job_title": "",
    "experience_level": "Mid-level (2-5 years)",
    "questions": [],
    "current_q_idx": 0,
    "answers": [],
    "evaluations": [],
    "session_summary": None,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


# ─── Helpers ───────────────────────────────────────────────
def score_class(s):
    return "score-high" if s >= 7 else ("score-mid" if s >= 4 else "score-low")

def cat_class(c):
    c = c.lower()
    if "behavioral"  in c: return "tag-behavioral"
    if "technical"   in c: return "tag-technical"
    if "situational" in c: return "tag-situational"
    return "tag-hr"

def readiness_class(r):
    r = r.lower()
    if "not ready"  in r: return "r-not-ready"
    if "needs work" in r: return "r-needs"
    if "almost"     in r: return "r-almost"
    return "r-ready"

def reset():
    for k, v in defaults.items():
        st.session_state[k] = v
    st.rerun()


# ─── Sidebar ───────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🎯 Interview Coach")
    st.divider()

    if st.session_state.stage != "setup":
        st.markdown(f"**Role:** {st.session_state.job_title}")
        st.markdown(f"**Level:** {st.session_state.experience_level}")
        total_q  = len(st.session_state.questions)
        answered = len(st.session_state.answers)
        if total_q > 0:
            st.markdown(f"**Progress:** {answered} / {total_q}")
            st.progress(answered / total_q)
        if st.session_state.evaluations:
            scores = [e.score for e in st.session_state.evaluations]
            st.markdown(f"**Avg score:** {sum(scores)/len(scores):.1f} / 10")
        st.divider()
        if st.button("↩ Start over"):
            reset()
    else:
        st.markdown("1. Enter job title & level")
        st.markdown("2. Answer each question")
        st.markdown("3. Get instant AI feedback")
        st.markdown("4. Review full session report")


# ══════════════════════════════════════════════
#  STAGE 1 — SETUP
# ══════════════════════════════════════════════
if st.session_state.stage == "setup":

    st.markdown("# AI Interview Coach")
    st.markdown(
        '<p style="color:#7080b0; font-size:16px; margin-top:-10px;">'
        'Practice interviews with AI that scores your answers and gives instant feedback.'
        '</p>', unsafe_allow_html=True
    )
    st.divider()

    col1, col2 = st.columns([2, 1], gap="large")
    with col1:
        job_title = st.text_input(
            "Job title",
            placeholder="e.g. Machine Learning Engineer, Backend Developer, Data Scientist",
        )
        focus_areas = st.text_input(
            "Focus areas  (optional)",
            placeholder="e.g. Python, Deep Learning, System Design, SQL",
        )
    with col2:
        experience_level = st.selectbox("Experience level", [
            "Fresh Graduate (0-1 year)",
            "Junior (1-2 years)",
            "Mid-level (2-5 years)",
            "Senior (5+ years)",
            "Lead / Manager",
        ])
        num_questions = st.slider("Number of questions", 3, 10, 5)

    st.divider()

    col_btn, col_tip = st.columns([1, 3])
    with col_btn:
        start = st.button("Start Interview →", use_container_width=True)
    with col_tip:
        st.info("The AI generates questions tailored to your role, evaluates every answer with a score, strengths, and improvements.")

    if start:
        if not job_title.strip():
            st.error("Please enter a job title first.")
        else:
            with st.spinner(f"Generating questions for {job_title}..."):
                try:
                    from chains import make_question_generator_chain
                    chain, _ = make_question_generator_chain()
                    result = chain.invoke({
                        "job_title":        job_title,
                        "experience_level": experience_level,
                        "focus_areas":      focus_areas or "General",
                        "num_questions":    num_questions,
                    })
                    st.session_state.questions        = result.questions
                    st.session_state.job_title        = job_title
                    st.session_state.experience_level = experience_level
                    st.session_state.stage            = "interview"
                    st.rerun()
                except Exception as e:
                    err = str(e)
                    if "RerunData" not in err:
                        st.error(f"Error: {err}")


# ══════════════════════════════════════════════
#  STAGE 2 — INTERVIEW
# ══════════════════════════════════════════════
elif st.session_state.stage == "interview":
    idx       = st.session_state.current_q_idx
    questions = st.session_state.questions
    total     = len(questions)

    if idx >= total:
        st.session_state.stage = "summary"
        st.rerun()

    q = questions[idx]
    st.progress(idx / total)

    diff_colors = {"Easy": "#00ff96", "Medium": "#ffc800", "Hard": "#ff3364"}
    diff_color  = diff_colors.get(q.difficulty, "#a0a0c0")

    st.markdown(f"""
    <div class="q-card">
        <div class="q-label">Question {idx + 1} of {total}</div>
        <div class="q-text">{q.question}</div>
        <span class="tag {cat_class(q.category)}">{q.category}</span>
        <span style="font-size:12px; color:{diff_color}; margin-left:6px; font-weight:700;
                     text-shadow: 0 0 8px {diff_color};">● {q.difficulty}</span>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("💡 Hint"):
        st.markdown(f'<span style="color:#8090c0;">{q.tip}</span>', unsafe_allow_html=True)

    answer = st.text_area(
        "Your answer",
        height=160,
        placeholder="Write your answer here. Try the STAR method: Situation → Task → Action → Result",
        key=f"ans_{idx}",
    )

    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        submit = st.button("Submit & Get Feedback →", use_container_width=True)
    with col3:
        skip = st.button("Skip →", use_container_width=True)

    if submit:
        if not answer.strip():
            st.warning("Please write an answer before submitting.")
        else:
            with st.spinner("Evaluating your answer..."):
                try:
                    from chains import make_answer_evaluator_chain
                    chain, _ = make_answer_evaluator_chain()
                    evaluation = chain.invoke({
                        "job_title": st.session_state.job_title,
                        "question":  q.question,
                        "category":  q.category,
                        "answer":    answer,
                    })
                    st.session_state.answers.append(answer)
                    st.session_state.evaluations.append(evaluation)
                    st.session_state.stage = "evaluation"
                    st.rerun()
                except Exception as e:
                    err = str(e)
                    if "RerunData" not in err:
                        st.error(f"Evaluation error: {err}")

    if skip:
        from chains import AnswerEvaluation
        st.session_state.answers.append("[skipped]")
        st.session_state.evaluations.append(AnswerEvaluation(
            score=0,
            strengths=["No answer provided"],
            improvements=["Make sure to answer this type of question"],
            ideal_answer_outline="N/A",
            framework_used="No",
        ))
        st.session_state.current_q_idx += 1
        st.rerun()


# ══════════════════════════════════════════════
#  STAGE 3 — EVALUATION
# ══════════════════════════════════════════════
elif st.session_state.stage == "evaluation":
    idx    = st.session_state.current_q_idx
    q      = st.session_state.questions[idx]
    ev     = st.session_state.evaluations[-1]
    answer = st.session_state.answers[-1]
    total  = len(st.session_state.questions)

    st.progress((idx + 1) / total)
    st.markdown(f"# Feedback — Q{idx + 1}")
    st.divider()

    col_score, col_fw, col_spacer = st.columns([1, 2, 3])
    with col_score:
        s_cls = score_class(ev.score)
        st.markdown(f"""
        <div style="text-align:center; padding:10px 0;">
            <div class="score-circle {s_cls}">{ev.score}</div>
            <div style="font-size:10px; color:#44447a; margin-top:10px;
                        letter-spacing:2px; text-transform:uppercase;
                        font-family:'Orbitron',sans-serif;">Score</div>
        </div>
        """, unsafe_allow_html=True)
    with col_fw:
        fw_colors = {"Yes": "#00ff96", "Partially": "#ffc800", "No": "#ff3364"}
        fw_color  = fw_colors.get(ev.framework_used, "#a0a0c0")
        fw_glow   = fw_colors.get(ev.framework_used, "#a0a0c0")
        st.markdown(f"""
        <div style="background:rgba(6,6,20,0.8); border:1px solid rgba(99,51,255,0.3);
                    border-radius:12px; padding:16px 18px;
                    box-shadow: 0 0 20px rgba(99,51,255,0.08);">
            <div style="font-size:9px; color:#44447a; margin-bottom:8px;
                        text-transform:uppercase; letter-spacing:2.5px;
                        font-family:'Orbitron',sans-serif;">STAR Framework</div>
            <div style="font-size:17px; font-weight:700; color:{fw_color};
                        text-shadow: 0 0 10px {fw_glow};">{ev.framework_used}</div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    with st.expander("View question & your answer"):
        st.markdown(f'<span style="color:#8090c0;">**Q:** {q.question}</span>', unsafe_allow_html=True)
        st.markdown(f'<span style="color:#6070a0;">**A:** {answer}</span>', unsafe_allow_html=True)

    st.markdown("### ✅ Strengths")
    for s in ev.strengths:
        st.markdown(f'<div class="eval-box eval-strength">• {s}</div>', unsafe_allow_html=True)

    st.markdown("### ⚠️ Areas to improve")
    for imp in ev.improvements:
        st.markdown(f'<div class="eval-box eval-improve">• {imp}</div>', unsafe_allow_html=True)

    st.markdown("### 💡 Ideal answer")
    st.markdown(f'<div class="eval-box eval-ideal">{ev.ideal_answer_outline}</div>', unsafe_allow_html=True)

    st.divider()

    is_last = (idx + 1 >= total)
    label   = "View Final Report →" if is_last else f"Next Question ({idx + 2}/{total}) →"
    if st.button(label):
        st.session_state.current_q_idx += 1
        st.session_state.stage = "summary" if is_last else "interview"
        st.rerun()


# ══════════════════════════════════════════════
#  STAGE 4 — SESSION SUMMARY
# ══════════════════════════════════════════════
elif st.session_state.stage == "summary":

    if st.session_state.session_summary is None:
        with st.spinner("Analyzing your full session..."):
            try:
                from chains import make_session_summary_chain
                chain, _ = make_session_summary_chain()
                lines = []
                for i, (q, a, ev) in enumerate(zip(
                    st.session_state.questions,
                    st.session_state.answers,
                    st.session_state.evaluations,
                )):
                    lines.append(
                        f"Q{i+1} [{q.category}]: {q.question}\n"
                        f"Answer: {a}\nScore: {ev.score}/10 | STAR: {ev.framework_used}"
                    )
                scores  = [ev.score for ev in st.session_state.evaluations]
                summary = chain.invoke({
                    "job_title":        st.session_state.job_title,
                    "experience_level": st.session_state.experience_level,
                    "session_data":     "\n---\n".join(lines),
                    "scores":           str(scores),
                })
                st.session_state.session_summary = summary
            except Exception as e:
                err = str(e)
                if "RerunData" not in err:
                    st.error(f"Summary error: {err}")
                    st.stop()

    summary = st.session_state.session_summary
    scores  = [ev.score for ev in st.session_state.evaluations]
    avg     = sum(scores) / len(scores)

    st.markdown("# Session Report")
    st.markdown(
        f'<p style="color:#5060a0; font-size:15px; margin-top:-8px;">'
        f'{st.session_state.job_title} · {st.session_state.experience_level}</p>',
        unsafe_allow_html=True
    )
    st.divider()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Overall Score",  f"{avg:.1f} / 10")
    c2.metric("Answered",       f"{sum(1 for a in st.session_state.answers if a != '[skipped]')} / {len(st.session_state.questions)}")
    c3.metric("Strong",         str(sum(1 for s in scores if s >= 7)))
    c4.metric("Needs Work",     str(sum(1 for s in scores if s < 5)))

    r_cls = readiness_class(summary.readiness_level)
    st.markdown(f"""
    <div style="margin: 24px 0 8px;">
        <span style="color:#44447a; font-size:11px; text-transform:uppercase;
                     letter-spacing:2px; font-family:'Orbitron',sans-serif;">Readiness Level</span><br/>
        <span class="readiness {r_cls}" style="margin-top:8px; display:inline-block;">
            {summary.readiness_level}
        </span>
    </div>
    """, unsafe_allow_html=True)

    st.divider()
    st.markdown("### Score Breakdown")
    import pandas as pd
    df = pd.DataFrame({
        "Question": [f"Q{i+1}" for i in range(len(scores))],
        "Score":    scores,
    })
    st.bar_chart(df.set_index("Question"), color="#6333ff")

    st.divider()

    col_l, col_r = st.columns(2)
    with col_l:
        st.markdown("### 💪 Strongest Area")
        st.success(summary.strongest_area)
        st.markdown("### ⚠️ Weakest Area")
        st.warning(summary.weakest_area)
    with col_r:
        st.markdown("### 🎯 Top Recommendations")
        for i, tip in enumerate(summary.top_improvements, 1):
            st.markdown(
                f'<div class="eval-box eval-improve"><strong>{i}.</strong> {tip}</div>',
                unsafe_allow_html=True
            )

    st.divider()
    st.markdown("### 🚀 Next Steps")
    cols = st.columns(len(summary.next_steps))
    for col, step in zip(cols, summary.next_steps):
        with col:
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,rgba(99,51,255,0.08),rgba(0,210,255,0.05));
                        border:1px solid rgba(99,51,255,0.3); border-radius:14px;
                        padding:18px; font-size:13px; color:#8090c0; line-height:1.7;
                        box-shadow: 0 0 20px rgba(99,51,255,0.08);">
                {step}
            </div>""", unsafe_allow_html=True)

    st.divider()
    with st.expander("Full Q&A Review"):
        for i, (q, a, ev) in enumerate(zip(
            st.session_state.questions,
            st.session_state.answers,
            st.session_state.evaluations,
        )):
            s_cls = score_class(ev.score)
            st.markdown(f"""
            <div class="q-card" style="margin-bottom:12px;">
                <div style="display:flex; justify-content:space-between; align-items:flex-start; gap:16px;">
                    <div style="flex:1;">
                        <div class="q-label">Q{i+1} · {q.category}</div>
                        <div style="font-size:15px; font-weight:500; color:#d0d8ff; margin-bottom:8px;">{q.question}</div>
                        <div style="font-size:13px; color:#50507a; font-style:italic;">{a}</div>
                    </div>
                    <div class="score-circle {s_cls}" style="flex-shrink:0;">{ev.score}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.divider()
    if st.button("↩ Start a New Interview"):
        reset()
