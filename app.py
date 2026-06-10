"""
app.py — AI Interview Coach  (Futuristic UI + Dark/Light + Languages + Voice)
"""

import streamlit as st
import base64
import os

st.set_page_config(
    page_title="AI Interview Coach",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Language config ──────────────────────────────────────────
LANGUAGES = {
    "English":  {"code": "en", "flag": "🇬🇧", "dir": "ltr"},
    "Arabic":   {"code": "ar", "flag": "🇸🇦", "dir": "rtl"},
    "French":   {"code": "fr", "flag": "🇫🇷", "dir": "ltr"},
    "German":   {"code": "de", "flag": "🇩🇪", "dir": "ltr"},
    "Spanish":  {"code": "es", "flag": "🇪🇸", "dir": "ltr"},
}

UI_TEXT = {
    "English": {
        "title": "AI Interview Coach",
        "subtitle": "Practice interviews with AI that scores your answers and gives instant feedback.",
        "job_title": "Job title",
        "job_placeholder": "e.g. Machine Learning Engineer, Backend Developer",
        "focus": "Focus areas (optional)",
        "focus_placeholder": "e.g. Python, Deep Learning, System Design",
        "level": "Experience level",
        "levels": ["Fresh Graduate (0-1 year)", "Junior (1-2 years)", "Mid-level (2-5 years)", "Senior (5+ years)", "Lead / Manager"],
        "num_q": "Number of questions",
        "start": "Start Interview →",
        "hint": "💡 Hint",
        "your_answer": "Your answer",
        "answer_placeholder": "Write your answer here. Try the STAR method: Situation → Task → Action → Result",
        "submit": "Submit & Get Feedback →",
        "skip": "Skip →",
        "feedback": "Feedback",
        "score": "Score",
        "star": "STAR Framework",
        "strengths": "✅ Strengths",
        "improve": "⚠️ Areas to improve",
        "ideal": "💡 Ideal answer",
        "next_q": "Next Question",
        "final_report": "View Final Report →",
        "report_title": "Session Report",
        "overall": "Overall Score",
        "answered": "Answered",
        "strong": "Strong",
        "needs_work": "Needs Work",
        "readiness": "Readiness Level",
        "score_breakdown": "Score Breakdown",
        "strongest": "💪 Strongest Area",
        "weakest": "⚠️ Weakest Area",
        "recommendations": "🎯 Top Recommendations",
        "next_steps": "🚀 Next Steps",
        "full_review": "Full Q&A Review",
        "start_over": "↩ Start over",
        "new_interview": "↩ Start a New Interview",
        "how_works": "How it works",
        "step1": "1. Enter job title & level",
        "step2": "2. Answer each question",
        "step3": "3. Get instant AI feedback",
        "step4": "4. Review full session report",
        "mode": "🌙 Dark Mode",
        "voice_mode": "🎤 Voice Interview",
        "written_mode": "✍️ Written Interview",
        "record_hint": "Click the mic to record your answer",
        "processing": "Processing your voice...",
        "view_q": "View question & your answer",
        "info": "The AI generates questions tailored to your role, evaluates every answer with a score, strengths, and improvements.",
        "generating": "Generating questions...",
        "evaluating": "Evaluating your answer...",
        "analyzing": "Analyzing your full session...",
        "role": "Role",
        "level_label": "Level",
        "progress": "Progress",
        "avg_score": "Avg score",
        "skipped": "skipped",
        "readiness_levels": {"not ready": "r-not-ready", "needs work": "r-needs", "almost": "r-almost"},
    },
    "Arabic": {
        "title": "مدرب الانترفيو بالذكاء الاصطناعي",
        "subtitle": "تدرب على الانترفيو مع AI يقيّم إجاباتك ويديك feedback فوري.",
        "job_title": "المسمى الوظيفي",
        "job_placeholder": "مثال: مهندس تعلم آلي، مطور خلفي",
        "focus": "المجالات المحددة (اختياري)",
        "focus_placeholder": "مثال: Python, Deep Learning, System Design",
        "level": "مستوى الخبرة",
        "levels": ["خريج جديد (0-1 سنة)", "مبتدئ (1-2 سنة)", "متوسط (2-5 سنوات)", "خبير (5+ سنوات)", "قيادي / مدير"],
        "num_q": "عدد الأسئلة",
        "start": "ابدأ الانترفيو →",
        "hint": "💡 تلميح",
        "your_answer": "إجابتك",
        "answer_placeholder": "اكتب إجابتك هنا. حاول تستخدم أسلوب STAR: الموقف ← المهمة ← الإجراء ← النتيجة",
        "submit": "سبمت واعرض التقييم →",
        "skip": "تخطّي →",
        "feedback": "التقييم",
        "score": "الدرجة",
        "star": "أسلوب STAR",
        "strengths": "✅ نقاط القوة",
        "improve": "⚠️ نقاط تحتاج تحسين",
        "ideal": "💡 الإجابة المثالية",
        "next_q": "السؤال التالي",
        "final_report": "عرض التقرير النهائي →",
        "report_title": "التقرير النهائي",
        "overall": "المتوسط العام",
        "answered": "تم الإجابة",
        "strong": "إجابات قوية",
        "needs_work": "تحتاج تطوير",
        "readiness": "مستوى الاستعداد",
        "score_breakdown": "توزيع الدرجات",
        "strongest": "💪 أقوى نقطة",
        "weakest": "⚠️ أضعف نقطة",
        "recommendations": "🎯 أهم التوصيات",
        "next_steps": "🚀 الخطوات التالية",
        "full_review": "مراجعة كل الأسئلة والإجابات",
        "start_over": "↩ ابدأ من جديد",
        "new_interview": "↩ انترفيو جديد",
        "how_works": "كيف يعمل",
        "step1": "١. أدخل الوظيفة والمستوى",
        "step2": "٢. أجب على كل سؤال",
        "step3": "٣. احصل على تقييم فوري",
        "step4": "٤. راجع التقرير الكامل",
        "mode": "🌙 الوضع الداكن",
        "voice_mode": "🎤 انترفيو بالصوت",
        "written_mode": "✍️ انترفيو مكتوب",
        "record_hint": "اضغط على الميكروفون لتسجيل إجابتك",
        "processing": "جارٍ معالجة الصوت...",
        "view_q": "عرض السؤال وإجابتك",
        "info": "الذكاء الاصطناعي يولّد أسئلة مخصصة لوظيفتك ويقيّم كل إجابة بدرجة ونقاط قوة وتحسينات.",
        "generating": "جارٍ توليد الأسئلة...",
        "evaluating": "جارٍ تقييم إجابتك...",
        "analyzing": "جارٍ تحليل جلستك الكاملة...",
        "role": "الوظيفة",
        "level_label": "المستوى",
        "progress": "التقدم",
        "avg_score": "متوسط الدرجات",
        "skipped": "تم التخطي",
        "readiness_levels": {"not ready": "r-not-ready", "needs work": "r-needs", "almost": "r-almost"},
    },
    "French": {
        "title": "Coach d'Entretien IA",
        "subtitle": "Pratiquez vos entretiens avec une IA qui évalue vos réponses et donne un retour instantané.",
        "job_title": "Intitulé du poste",
        "job_placeholder": "ex. Ingénieur ML, Développeur Backend",
        "focus": "Domaines de focus (optionnel)",
        "focus_placeholder": "ex. Python, Deep Learning, System Design",
        "level": "Niveau d'expérience",
        "levels": ["Diplômé (0-1 an)", "Junior (1-2 ans)", "Intermédiaire (2-5 ans)", "Senior (5+ ans)", "Manager"],
        "num_q": "Nombre de questions",
        "start": "Commencer l'entretien →",
        "hint": "💡 Indice",
        "your_answer": "Votre réponse",
        "answer_placeholder": "Écrivez votre réponse ici. Utilisez la méthode STAR.",
        "submit": "Soumettre →",
        "skip": "Passer →",
        "feedback": "Retour",
        "score": "Score",
        "star": "Méthode STAR",
        "strengths": "✅ Points forts",
        "improve": "⚠️ Points à améliorer",
        "ideal": "💡 Réponse idéale",
        "next_q": "Question suivante",
        "final_report": "Voir le rapport final →",
        "report_title": "Rapport de session",
        "overall": "Score global",
        "answered": "Répondues",
        "strong": "Fortes",
        "needs_work": "À améliorer",
        "readiness": "Niveau de préparation",
        "score_breakdown": "Répartition des scores",
        "strongest": "💪 Point le plus fort",
        "weakest": "⚠️ Point le plus faible",
        "recommendations": "🎯 Top recommandations",
        "next_steps": "🚀 Prochaines étapes",
        "full_review": "Révision complète Q&R",
        "start_over": "↩ Recommencer",
        "new_interview": "↩ Nouvel entretien",
        "how_works": "Comment ça marche",
        "step1": "1. Entrez le poste et le niveau",
        "step2": "2. Répondez aux questions",
        "step3": "3. Obtenez un retour instantané",
        "step4": "4. Consultez le rapport complet",
        "mode": "🌙 Mode sombre",
        "voice_mode": "🎤 Entretien vocal",
        "written_mode": "✍️ Entretien écrit",
        "record_hint": "Cliquez sur le micro pour enregistrer",
        "processing": "Traitement de la voix...",
        "view_q": "Voir la question et votre réponse",
        "info": "L'IA génère des questions adaptées à votre rôle et évalue chaque réponse.",
        "generating": "Génération des questions...",
        "evaluating": "Évaluation de votre réponse...",
        "analyzing": "Analyse de votre session...",
        "role": "Rôle",
        "level_label": "Niveau",
        "progress": "Progression",
        "avg_score": "Score moyen",
        "skipped": "ignorée",
        "readiness_levels": {"not ready": "r-not-ready", "needs work": "r-needs", "almost": "r-almost"},
    },
    "German": {
        "title": "KI-Interview-Coach",
        "subtitle": "Üben Sie Vorstellungsgespräche mit KI, die Ihre Antworten bewertet und sofortiges Feedback gibt.",
        "job_title": "Berufsbezeichnung",
        "job_placeholder": "z.B. ML-Ingenieur, Backend-Entwickler",
        "focus": "Schwerpunkte (optional)",
        "focus_placeholder": "z.B. Python, Deep Learning, System Design",
        "level": "Erfahrungsstufe",
        "levels": ["Absolvent (0-1 Jahr)", "Junior (1-2 Jahre)", "Mittelklasse (2-5 Jahre)", "Senior (5+ Jahre)", "Führungskraft"],
        "num_q": "Anzahl der Fragen",
        "start": "Interview starten →",
        "hint": "💡 Hinweis",
        "your_answer": "Ihre Antwort",
        "answer_placeholder": "Schreiben Sie Ihre Antwort hier. Verwenden Sie die STAR-Methode.",
        "submit": "Absenden →",
        "skip": "Überspringen →",
        "feedback": "Feedback",
        "score": "Bewertung",
        "star": "STAR-Methode",
        "strengths": "✅ Stärken",
        "improve": "⚠️ Verbesserungsbereiche",
        "ideal": "💡 Ideale Antwort",
        "next_q": "Nächste Frage",
        "final_report": "Abschlussbericht anzeigen →",
        "report_title": "Sitzungsbericht",
        "overall": "Gesamtbewertung",
        "answered": "Beantwortet",
        "strong": "Stark",
        "needs_work": "Verbesserungsbedarf",
        "readiness": "Bereitschaftsstufe",
        "score_breakdown": "Bewertungsübersicht",
        "strongest": "💪 Stärkster Bereich",
        "weakest": "⚠️ Schwächster Bereich",
        "recommendations": "🎯 Top-Empfehlungen",
        "next_steps": "🚀 Nächste Schritte",
        "full_review": "Vollständige Überprüfung",
        "start_over": "↩ Neu starten",
        "new_interview": "↩ Neues Interview",
        "how_works": "So funktioniert es",
        "step1": "1. Stelle und Niveau eingeben",
        "step2": "2. Jede Frage beantworten",
        "step3": "3. Sofortiges KI-Feedback",
        "step4": "4. Vollständigen Bericht ansehen",
        "mode": "🌙 Dunkelmodus",
        "voice_mode": "🎤 Sprach-Interview",
        "written_mode": "✍️ Schriftliches Interview",
        "record_hint": "Klicken Sie auf das Mikrofon zum Aufnehmen",
        "processing": "Sprache wird verarbeitet...",
        "view_q": "Frage und Antwort anzeigen",
        "info": "Die KI generiert rollenspezifische Fragen und bewertet jede Antwort.",
        "generating": "Fragen werden generiert...",
        "evaluating": "Antwort wird bewertet...",
        "analyzing": "Sitzung wird analysiert...",
        "role": "Rolle",
        "level_label": "Niveau",
        "progress": "Fortschritt",
        "avg_score": "Durchschnittsbewertung",
        "skipped": "übersprungen",
        "readiness_levels": {"not ready": "r-not-ready", "needs work": "r-needs", "almost": "r-almost"},
    },
    "Spanish": {
        "title": "Coach de Entrevistas IA",
        "subtitle": "Practica entrevistas con IA que puntúa tus respuestas y da retroalimentación instantánea.",
        "job_title": "Título del puesto",
        "job_placeholder": "ej. Ingeniero ML, Desarrollador Backend",
        "focus": "Áreas de enfoque (opcional)",
        "focus_placeholder": "ej. Python, Deep Learning, System Design",
        "level": "Nivel de experiencia",
        "levels": ["Recién graduado (0-1 año)", "Junior (1-2 años)", "Intermedio (2-5 años)", "Senior (5+ años)", "Líder / Manager"],
        "num_q": "Número de preguntas",
        "start": "Iniciar entrevista →",
        "hint": "💡 Pista",
        "your_answer": "Tu respuesta",
        "answer_placeholder": "Escribe tu respuesta aquí. Usa el método STAR.",
        "submit": "Enviar →",
        "skip": "Saltar →",
        "feedback": "Retroalimentación",
        "score": "Puntuación",
        "star": "Método STAR",
        "strengths": "✅ Fortalezas",
        "improve": "⚠️ Áreas a mejorar",
        "ideal": "💡 Respuesta ideal",
        "next_q": "Siguiente pregunta",
        "final_report": "Ver informe final →",
        "report_title": "Informe de sesión",
        "overall": "Puntuación global",
        "answered": "Respondidas",
        "strong": "Fuertes",
        "needs_work": "Necesita trabajo",
        "readiness": "Nivel de preparación",
        "score_breakdown": "Desglose de puntuación",
        "strongest": "💪 Área más fuerte",
        "weakest": "⚠️ Área más débil",
        "recommendations": "🎯 Top recomendaciones",
        "next_steps": "🚀 Próximos pasos",
        "full_review": "Revisión completa",
        "start_over": "↩ Empezar de nuevo",
        "new_interview": "↩ Nueva entrevista",
        "how_works": "Cómo funciona",
        "step1": "1. Ingresa el puesto y nivel",
        "step2": "2. Responde cada pregunta",
        "step3": "3. Obtén retroalimentación IA",
        "step4": "4. Revisa el informe completo",
        "mode": "🌙 Modo oscuro",
        "voice_mode": "🎤 Entrevista por voz",
        "written_mode": "✍️ Entrevista escrita",
        "record_hint": "Haz clic en el micrófono para grabar",
        "processing": "Procesando voz...",
        "view_q": "Ver pregunta y tu respuesta",
        "info": "La IA genera preguntas adaptadas a tu rol y evalúa cada respuesta.",
        "generating": "Generando preguntas...",
        "evaluating": "Evaluando tu respuesta...",
        "analyzing": "Analizando tu sesión...",
        "role": "Rol",
        "level_label": "Nivel",
        "progress": "Progreso",
        "avg_score": "Puntuación media",
        "skipped": "omitida",
        "readiness_levels": {"not ready": "r-not-ready", "needs work": "r-needs", "almost": "r-almost"},
    },
}


# ─── Session state ─────────────────────────────────────────
defaults = {
    "stage": "setup",
    "job_title": "",
    "experience_level": "",
    "questions": [],
    "current_q_idx": 0,
    "answers": [],
    "evaluations": [],
    "session_summary": None,
    "dark_mode": True,
    "language": "English",
    "interview_mode": "written",
    "voice_answer": "",
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

lang = st.session_state.language
T = UI_TEXT[lang]
is_dark = st.session_state.dark_mode
is_rtl = LANGUAGES[lang]["dir"] == "rtl"


# ─── CSS ───────────────────────────────────────────────────
def get_css(dark):
    if dark:
        bg = "#020208"
        bg2 = "#111120"
        sidebar_bg = "linear-gradient(180deg,#06060f,#0a0a18)"
        sidebar_border = "rgba(99,51,255,0.3)"
        text = "#c8d0ff"
        text2 = "#7070a0"
        card_bg = "rgba(99,51,255,0.08)"
        card_border = "rgba(99,51,255,0.4)"
        card_glow = "0 0 30px rgba(99,51,255,0.1)"
        label_color = "rgba(99,51,255,0.7)"
        q_text = "#e0e8ff"
        input_bg = "rgba(6,6,20,0.8)"
        input_border = "rgba(99,51,255,0.3)"
        eval_bg = "rgba(6,6,20,0.8)"
        metric_bg = "linear-gradient(135deg,rgba(99,51,255,0.08),rgba(0,210,255,0.05))"
        metric_border = "rgba(99,51,255,0.3)"
        metric_val = "linear-gradient(90deg,#6333ff,#00d2ff)"
        metric_label = "#5a5a8a"
        btn_bg = "linear-gradient(135deg,#6333ff,#00d2ff)"
        btn_shadow = "0 0 20px rgba(99,51,255,0.4)"
        divider = "rgba(99,51,255,0.2)"
        expander_bg = "rgba(6,6,20,0.6)"
        expander_border = "rgba(99,51,255,0.25)"
        next_step_bg = "linear-gradient(135deg,rgba(99,51,255,0.08),rgba(0,210,255,0.05))"
        next_step_border = "rgba(99,51,255,0.3)"
        next_step_text = "#8090c0"
        glow_colors = "radial-gradient(ellipse at 10% 20%,rgba(99,51,255,0.12) 0%,transparent 50%),radial-gradient(ellipse at 90% 80%,rgba(0,210,255,0.10) 0%,transparent 50%)"
    else:
        bg = "#f0f2ff"
        bg2 = "#ffffff"
        sidebar_bg = "linear-gradient(180deg,#e8eaff,#f0f2ff)"
        sidebar_border = "rgba(99,51,255,0.2)"
        text = "#1a1a3a"
        text2 = "#5a5a8a"
        card_bg = "rgba(255,255,255,0.9)"
        card_border = "rgba(99,51,255,0.3)"
        card_glow = "0 4px 20px rgba(99,51,255,0.08)"
        label_color = "#6333ff"
        q_text = "#1a1a3a"
        input_bg = "#ffffff"
        input_border = "rgba(99,51,255,0.3)"
        eval_bg = "#ffffff"
        metric_bg = "linear-gradient(135deg,rgba(99,51,255,0.05),rgba(0,210,255,0.03))"
        metric_border = "rgba(99,51,255,0.2)"
        metric_val = "linear-gradient(90deg,#6333ff,#0099cc)"
        metric_label = "#7070a0"
        btn_bg = "linear-gradient(135deg,#6333ff,#00b4d8)"
        btn_shadow = "0 4px 15px rgba(99,51,255,0.3)"
        divider = "rgba(99,51,255,0.15)"
        expander_bg = "rgba(255,255,255,0.8)"
        expander_border = "rgba(99,51,255,0.2)"
        next_step_bg = "rgba(255,255,255,0.9)"
        next_step_border = "rgba(99,51,255,0.2)"
        next_step_text = "#5a5a8a"
        glow_colors = "radial-gradient(ellipse at 10% 20%,rgba(99,51,255,0.06) 0%,transparent 50%),radial-gradient(ellipse at 90% 80%,rgba(0,210,255,0.05) 0%,transparent 50%)"

    rtl_body = "direction:rtl; text-align:right;" if is_rtl else ""

    return f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Orbitron:wght@700;800;900&display=swap');
html,body,[class*="css"]{{font-family:'Space Grotesk',sans-serif; {rtl_body} }}
#MainMenu{{visibility:hidden;}}header{{visibility:hidden;}}footer{{visibility:hidden;}}
[data-testid="stToolbar"]{{display:none!important;}}
[data-testid="stDecoration"]{{display:none!important;}}
[data-testid="stStatusWidget"]{{display:none!important;}}
.viewerBadge_container__1QSob{{display:none!important;}}
.stApp{{background:{bg}; color:{text};}}
.stApp::before{{content:'';position:fixed;top:0;left:0;right:0;bottom:0;
  background:{glow_colors};pointer-events:none;z-index:0;}}
[data-testid="stSidebar"]{{background:{sidebar_bg}!important;border-right:1px solid {sidebar_border}!important;}}
[data-testid="stSidebar"] *{{color:{text2}!important;}}
[data-testid="stSidebar"] strong{{color:{text}!important;}}
h1{{font-family:'Orbitron',sans-serif!important;
  background:linear-gradient(135deg,#6333ff 0%,#00d2ff 50%,#ff3399 100%);
  -webkit-background-clip:text!important;-webkit-text-fill-color:transparent!important;
  font-size:2.6rem!important;letter-spacing:1px!important;}}
h2,h3{{font-family:'Orbitron',sans-serif!important;color:#a0c0ff!important;}}
.stProgress>div>div{{background:linear-gradient(90deg,#6333ff,#00d2ff)!important;border-radius:99px!important;}}
[data-testid="stProgress"]>div{{background:rgba(99,51,255,0.15)!important;border-radius:99px!important;}}
.score-circle{{display:inline-flex;align-items:center;justify-content:center;
  width:68px;height:68px;border-radius:50%;font-family:'Orbitron',sans-serif;font-size:22px;font-weight:900;}}
.score-high{{background:rgba(0,255,150,0.08);color:#00ff96;border:2px solid #00ff96;box-shadow:0 0 20px rgba(0,255,150,0.3);}}
.score-mid{{background:rgba(255,200,0,0.08);color:#ffc800;border:2px solid #ffc800;box-shadow:0 0 20px rgba(255,200,0,0.3);}}
.score-low{{background:rgba(255,51,100,0.08);color:#ff3364;border:2px solid #ff3364;box-shadow:0 0 20px rgba(255,51,100,0.3);}}
.q-card{{background:{card_bg};border:1px solid {card_border};border-radius:16px;padding:28px;
  margin-bottom:16px;box-shadow:{card_glow};position:relative;overflow:hidden;}}
.q-card::before{{content:'';position:absolute;top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,rgba(99,51,255,0.8),rgba(0,210,255,0.8),transparent);}}
.q-label{{font-size:10px;font-weight:700;letter-spacing:2.5px;color:{label_color};
  text-transform:uppercase;margin-bottom:12px;font-family:'Orbitron',sans-serif;}}
.q-text{{font-size:18px;font-weight:500;color:{q_text};line-height:1.65;}}
.tag{{display:inline-block;padding:4px 12px;border-radius:20px;font-size:11px;font-weight:600;margin-top:14px;margin-right:6px;}}
.tag-behavioral{{background:rgba(99,51,255,0.15);color:#a78bfa;border:1px solid rgba(99,51,255,0.5);}}
.tag-technical{{background:rgba(0,210,255,0.1);color:#00d2ff;border:1px solid rgba(0,210,255,0.4);}}
.tag-situational{{background:rgba(255,153,0,0.1);color:#ff9900;border:1px solid rgba(255,153,0,0.4);}}
.tag-hr{{background:rgba(255,51,153,0.1);color:#ff3399;border:1px solid rgba(255,51,153,0.4);}}
.eval-box{{background:{eval_bg};border-left:3px solid;border-radius:0 12px 12px 0;
  padding:14px 18px;margin:8px 0;font-size:14px;line-height:1.7;color:{text2};}}
.eval-strength{{border-color:#00ff96;box-shadow:-2px 0 12px rgba(0,255,150,0.15);}}
.eval-improve{{border-color:#ffc800;box-shadow:-2px 0 12px rgba(255,200,0,0.15);}}
.eval-ideal{{border-color:#00d2ff;box-shadow:-2px 0 12px rgba(0,210,255,0.15);}}
.readiness{{display:inline-block;padding:6px 20px;border-radius:20px;font-weight:700;
  font-size:13px;font-family:'Orbitron',sans-serif;letter-spacing:1px;text-transform:uppercase;}}
.r-ready{{background:rgba(0,255,150,0.1);color:#00ff96;border:1px solid rgba(0,255,150,0.5);box-shadow:0 0 16px rgba(0,255,150,0.2);}}
.r-almost{{background:rgba(0,210,255,0.1);color:#00d2ff;border:1px solid rgba(0,210,255,0.5);box-shadow:0 0 16px rgba(0,210,255,0.2);}}
.r-needs{{background:rgba(255,200,0,0.1);color:#ffc800;border:1px solid rgba(255,200,0,0.5);box-shadow:0 0 16px rgba(255,200,0,0.2);}}
.r-not-ready{{background:rgba(255,51,100,0.1);color:#ff3364;border:1px solid rgba(255,51,100,0.5);box-shadow:0 0 16px rgba(255,51,100,0.2);}}
[data-testid="stMetric"]{{background:{metric_bg}!important;border:1px solid {metric_border}!important;
  border-radius:14px!important;padding:18px!important;box-shadow:0 0 20px rgba(99,51,255,0.08)!important;}}
[data-testid="stMetricValue"]{{font-family:'Orbitron',sans-serif!important;font-weight:900!important;
  background:{metric_val}!important;-webkit-background-clip:text!important;-webkit-text-fill-color:transparent!important;font-size:1.8rem!important;}}
[data-testid="stMetricLabel"]{{color:{metric_label}!important;font-size:11px!important;text-transform:uppercase;letter-spacing:1.5px;}}
.stButton>button{{background:{btn_bg}!important;color:#fff!important;border:none!important;
  border-radius:10px!important;font-family:'Space Grotesk',sans-serif!important;font-weight:700!important;
  font-size:14px!important;padding:0.6rem 1.8rem!important;box-shadow:{btn_shadow}!important;}}
.stButton>button:hover{{box-shadow:0 0 30px rgba(0,210,255,0.5)!important;transform:translateY(-1px)!important;}}
.stTextArea textarea,.stTextInput input{{background:{input_bg}!important;color:{text}!important;
  border:1px solid {input_border}!important;border-radius:10px!important;font-family:'Space Grotesk',sans-serif!important;}}
.stTextArea textarea:focus,.stTextInput input:focus{{border-color:#00d2ff!important;box-shadow:0 0 16px rgba(0,210,255,0.2)!important;}}
.stSelectbox>div>div{{background:{input_bg}!important;border:1px solid {input_border}!important;border-radius:10px!important;color:{text}!important;}}
hr{{border:none!important;border-top:1px solid {divider}!important;margin:1.5rem 0!important;}}
.stAlert{{border-radius:10px!important;}}
[data-testid="stExpander"]{{background:{expander_bg}!important;border:1px solid {expander_border}!important;border-radius:12px!important;}}
.stSpinner>div{{border-top-color:#6333ff!important;}}
::-webkit-scrollbar{{width:6px;}}
::-webkit-scrollbar-track{{background:{bg};}}
::-webkit-scrollbar-thumb{{background:linear-gradient(180deg,#6333ff,#00d2ff);border-radius:3px;}}
.voice-btn{{display:flex;align-items:center;justify-content:center;width:80px;height:80px;
  border-radius:50%;background:linear-gradient(135deg,#6333ff,#00d2ff);
  border:none;cursor:pointer;font-size:32px;margin:20px auto;
  box-shadow:0 0 30px rgba(99,51,255,0.5);transition:all 0.3s;}}
.voice-btn:hover{{transform:scale(1.1);box-shadow:0 0 50px rgba(0,210,255,0.6);}}
.voice-recording{{animation:pulse 1s infinite;}}
@keyframes pulse{{0%{{box-shadow:0 0 30px rgba(255,51,100,0.5);}}
  50%{{box-shadow:0 0 60px rgba(255,51,100,0.9);}}100%{{box-shadow:0 0 30px rgba(255,51,100,0.5);}}}}
.mode-badge{{display:inline-flex;align-items:center;gap:8px;padding:6px 16px;
  border-radius:20px;font-size:12px;font-weight:600;margin-bottom:8px;
  background:rgba(99,51,255,0.15);color:#a78bfa;border:1px solid rgba(99,51,255,0.4);}}
</style>
"""

st.markdown(get_css(is_dark), unsafe_allow_html=True)


# ─── Helpers ───────────────────────────────────────────────
def score_class(s):
    return "score-high" if s >= 7 else ("score-mid" if s >= 4 else "score-low")

def cat_class(c):
    c = c.lower()
    if "behavioral" in c: return "tag-behavioral"
    if "technical"  in c: return "tag-technical"
    if "situational"in c: return "tag-situational"
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

def speak_text(text, lang_code):
    """Generate TTS audio and return base64"""
    try:
        from gtts import gTTS
        import io
        tts = gTTS(text=text, lang=lang_code, slow=False)
        buf = io.BytesIO()
        tts.write_to_fp(buf)
        buf.seek(0)
        b64 = base64.b64encode(buf.read()).decode()
        return b64
    except Exception:
        return None

def transcribe_audio(audio_bytes):
    """Transcribe audio using OpenAI Whisper"""
    try:
        import openai, io
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY", ""))
        audio_file = io.BytesIO(audio_bytes)
        audio_file.name = "audio.wav"
        transcript = client.audio.transcriptions.create(
            model="whisper-1", file=audio_file
        )
        return transcript.text
    except Exception as e:
        return ""


# ─── Sidebar ───────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🎯 Interview Coach")
    st.divider()

    # Language selector
    lang_options = [f"{LANGUAGES[l]['flag']} {l}" for l in LANGUAGES]
    current_idx = list(LANGUAGES.keys()).index(st.session_state.language)
    selected_lang_str = st.selectbox("🌐 Language", lang_options, index=current_idx)
    selected_lang = selected_lang_str.split(" ", 1)[1]
    if selected_lang != st.session_state.language:
        st.session_state.language = selected_lang
        st.rerun()

    # Dark/Light mode toggle
    mode_label = "☀️ Light Mode" if is_dark else "🌙 Dark Mode"
    if st.button(mode_label, use_container_width=True):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()

    # Interview mode toggle
    st.divider()
    st.markdown("**Interview Mode**")
    col_w, col_v = st.columns(2)
    with col_w:
        if st.button("✍️", use_container_width=True, help="Written"):
            st.session_state.interview_mode = "written"
            st.rerun()
    with col_v:
        if st.button("🎤", use_container_width=True, help="Voice"):
            st.session_state.interview_mode = "voice"
            st.rerun()

    mode_display = T["voice_mode"] if st.session_state.interview_mode == "voice" else T["written_mode"]
    st.markdown(f'<div class="mode-badge">{mode_display}</div>', unsafe_allow_html=True)

    st.divider()

    if st.session_state.stage != "setup":
        st.markdown(f"**{T['role']}:** {st.session_state.job_title}")
        st.markdown(f"**{T['level_label']}:** {st.session_state.experience_level}")
        total_q  = len(st.session_state.questions)
        answered = len(st.session_state.answers)
        if total_q > 0:
            st.markdown(f"**{T['progress']}:** {answered} / {total_q}")
            st.progress(answered / total_q)
        if st.session_state.evaluations:
            scores = [e.score for e in st.session_state.evaluations]
            st.markdown(f"**{T['avg_score']}:** {sum(scores)/len(scores):.1f} / 10")
        st.divider()
        if st.button(T["start_over"]):
            reset()
    else:
        st.markdown(T["how_works"])
        st.markdown(T["step1"])
        st.markdown(T["step2"])
        st.markdown(T["step3"])
        st.markdown(T["step4"])


# ══════════════════════════════════════════════
#  STAGE 1 — SETUP
# ══════════════════════════════════════════════
if st.session_state.stage == "setup":
    st.markdown(f"# {T['title']}")
    st.markdown(f'<p style="color:#7080b0;font-size:16px;margin-top:-10px;">{T["subtitle"]}</p>', unsafe_allow_html=True)
    st.divider()

    col1, col2 = st.columns([2, 1], gap="large")
    with col1:
        job_title   = st.text_input(T["job_title"], placeholder=T["job_placeholder"])
        focus_areas = st.text_input(T["focus"],     placeholder=T["focus_placeholder"])
    with col2:
        experience_level = st.selectbox(T["level"], T["levels"])
        num_questions    = st.slider(T["num_q"], 3, 10, 5)

    st.divider()
    col_btn, col_tip = st.columns([1, 3])
    with col_btn:
        start = st.button(T["start"], use_container_width=True)
    with col_tip:
        st.info(T["info"])

    if start:
        if not job_title.strip():
            st.error("Please enter a job title first." if lang == "English" else "من فضلك أدخل المسمى الوظيفي أولاً.")
        else:
            with st.spinner(T["generating"]):
                try:
                    from chains import make_question_generator_chain
                    chain, _ = make_question_generator_chain()
                    result = chain.invoke({
                        "job_title":        job_title,
                        "experience_level": experience_level,
                        "focus_areas":      focus_areas or "General",
                        "num_questions":    num_questions,
                        "language":         lang,
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
        <div class="q-label">{T['hint'].replace('💡 ','')} {idx+1} / {total}</div>
        <div class="q-text">{q.question}</div>
        <span class="tag {cat_class(q.category)}">{q.category}</span>
        <span style="font-size:12px;color:{diff_color};margin-left:6px;font-weight:700;">● {q.difficulty}</span>
    </div>
    """, unsafe_allow_html=True)

    # TTS — read question aloud
    if st.session_state.interview_mode == "voice":
        lang_code = LANGUAGES[lang]["code"]
        audio_b64 = speak_text(q.question, lang_code)
        if audio_b64:
            st.markdown(f"""
            <audio autoplay>
                <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
            </audio>
            """, unsafe_allow_html=True)

    with st.expander(T["hint"]):
        st.markdown(f'<span style="color:#8090c0;">{q.tip}</span>', unsafe_allow_html=True)

    # ── Answer input: voice or written ──
    answer = ""
    if st.session_state.interview_mode == "voice":
        st.markdown(f'<p style="color:#8090c0;text-align:center;">{T["record_hint"]}</p>', unsafe_allow_html=True)
        try:
            from audio_recorder_streamlit import audio_recorder
            audio_bytes = audio_recorder(
                text="",
                recording_color="#ff3364",
                neutral_color="#6333ff",
                icon_name="microphone",
                icon_size="3x",
            )
            if audio_bytes:
                with st.spinner(T["processing"]):
                    transcribed = transcribe_audio(audio_bytes)
                    if transcribed:
                        st.session_state.voice_answer = transcribed
                        st.success(f"✅ Transcribed: {transcribed}")
            answer = st.session_state.voice_answer
            if answer:
                st.text_area("Transcribed answer", value=answer, height=100, disabled=True)
        except ImportError:
            st.warning("Voice mode requires `audio-recorder-streamlit`. Falling back to written mode.")
            answer = st.text_area(T["your_answer"], height=160,
                placeholder=T["answer_placeholder"], key=f"ans_{idx}")
    else:
        answer = st.text_area(T["your_answer"], height=160,
            placeholder=T["answer_placeholder"], key=f"ans_{idx}")

    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        submit = st.button(T["submit"], use_container_width=True)
    with col3:
        skip = st.button(T["skip"], use_container_width=True)

    if submit:
        if not answer.strip():
            st.warning("Please write or record an answer first.")
        else:
            with st.spinner(T["evaluating"]):
                try:
                    from chains import make_answer_evaluator_chain
                    chain, _ = make_answer_evaluator_chain()
                    evaluation = chain.invoke({
                        "job_title": st.session_state.job_title,
                        "question":  q.question,
                        "category":  q.category,
                        "answer":    answer,
                        "language":  lang,
                    })
                    st.session_state.answers.append(answer)
                    st.session_state.evaluations.append(evaluation)
                    st.session_state.voice_answer = ""
                    st.session_state.stage = "evaluation"
                    st.rerun()
                except Exception as e:
                    err = str(e)
                    if "RerunData" not in err:
                        st.error(f"Error: {err}")

    if skip:
        from chains import AnswerEvaluation
        st.session_state.answers.append(f"[{T['skipped']}]")
        st.session_state.evaluations.append(AnswerEvaluation(
            score=0, strengths=["No answer provided"],
            improvements=["Answer this type of question"],
            ideal_answer_outline="N/A", framework_used="No",
        ))
        st.session_state.current_q_idx += 1
        st.session_state.voice_answer = ""
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

    st.progress((idx+1)/total)
    st.markdown(f"# {T['feedback']} — Q{idx+1}")
    st.divider()

    col_score, col_fw, _ = st.columns([1, 2, 3])
    with col_score:
        s_cls = score_class(ev.score)
        st.markdown(f"""
        <div style="text-align:center;padding:10px 0;">
            <div class="score-circle {s_cls}">{ev.score}</div>
            <div style="font-size:10px;color:#44447a;margin-top:10px;letter-spacing:2px;
                        text-transform:uppercase;font-family:'Orbitron',sans-serif;">{T['score']}</div>
        </div>""", unsafe_allow_html=True)
    with col_fw:
        fw_colors = {"Yes": "#00ff96", "Partially": "#ffc800", "No": "#ff3364",
                     "نعم": "#00ff96", "جزئياً": "#ffc800", "لا": "#ff3364",
                     "Oui": "#00ff96", "Partiellement": "#ffc800", "Non": "#ff3364",
                     "Ja": "#00ff96", "Teilweise": "#ffc800", "Nein": "#ff3364",
                     "Sí": "#00ff96", "Parcialmente": "#ffc800"}
        fw_color = fw_colors.get(ev.framework_used, "#a0a0c0")
        st.markdown(f"""
        <div style="background:rgba(6,6,20,0.8);border:1px solid rgba(99,51,255,0.3);
                    border-radius:12px;padding:16px 18px;">
            <div style="font-size:9px;color:#44447a;margin-bottom:8px;text-transform:uppercase;
                        letter-spacing:2.5px;font-family:'Orbitron',sans-serif;">{T['star']}</div>
            <div style="font-size:17px;font-weight:700;color:{fw_color};">{ev.framework_used}</div>
        </div>""", unsafe_allow_html=True)

    st.divider()
    with st.expander(T["view_q"]):
        st.markdown(f'**Q:** {q.question}')
        st.markdown(f'**A:** {answer}')

    st.markdown(f"### {T['strengths']}")
    for s in ev.strengths:
        st.markdown(f'<div class="eval-box eval-strength">• {s}</div>', unsafe_allow_html=True)

    st.markdown(f"### {T['improve']}")
    for imp in ev.improvements:
        st.markdown(f'<div class="eval-box eval-improve">• {imp}</div>', unsafe_allow_html=True)

    st.markdown(f"### {T['ideal']}")
    st.markdown(f'<div class="eval-box eval-ideal">{ev.ideal_answer_outline}</div>', unsafe_allow_html=True)
    st.divider()

    is_last = (idx+1 >= total)
    label   = T["final_report"] if is_last else f"{T['next_q']} ({idx+2}/{total}) →"
    if st.button(label):
        st.session_state.current_q_idx += 1
        st.session_state.stage = "summary" if is_last else "interview"
        st.rerun()


# ══════════════════════════════════════════════
#  STAGE 4 — SUMMARY
# ══════════════════════════════════════════════
elif st.session_state.stage == "summary":

    if st.session_state.session_summary is None:
        with st.spinner(T["analyzing"]):
            try:
                from chains import make_session_summary_chain
                chain, _ = make_session_summary_chain()
                lines = []
                for i, (q, a, ev) in enumerate(zip(
                    st.session_state.questions,
                    st.session_state.answers,
                    st.session_state.evaluations,
                )):
                    lines.append(f"Q{i+1} [{q.category}]: {q.question}\nAnswer: {a}\nScore: {ev.score}/10 | STAR: {ev.framework_used}")
                scores  = [ev.score for ev in st.session_state.evaluations]
                summary = chain.invoke({
                    "job_title":        st.session_state.job_title,
                    "experience_level": st.session_state.experience_level,
                    "session_data":     "\n---\n".join(lines),
                    "scores":           str(scores),
                    "language":         lang,
                })
                st.session_state.session_summary = summary
            except Exception as e:
                err = str(e)
                if "RerunData" not in err:
                    st.error(f"Error: {err}")
                    st.stop()

    summary = st.session_state.session_summary
    scores  = [ev.score for ev in st.session_state.evaluations]
    avg     = sum(scores)/len(scores)

    st.markdown(f"# {T['report_title']}")
    st.markdown(f'<p style="color:#5060a0;font-size:15px;margin-top:-8px;">{st.session_state.job_title} · {st.session_state.experience_level}</p>', unsafe_allow_html=True)
    st.divider()

    c1,c2,c3,c4 = st.columns(4)
    c1.metric(T["overall"],   f"{avg:.1f} / 10")
    c2.metric(T["answered"],  f"{sum(1 for a in st.session_state.answers if T['skipped'] not in a)} / {len(st.session_state.questions)}")
    c3.metric(T["strong"],    str(sum(1 for s in scores if s >= 7)))
    c4.metric(T["needs_work"],str(sum(1 for s in scores if s < 5)))

    r_cls = readiness_class(summary.readiness_level)
    st.markdown(f"""
    <div style="margin:24px 0 8px;">
        <span style="color:#44447a;font-size:11px;text-transform:uppercase;letter-spacing:2px;font-family:'Orbitron',sans-serif;">{T['readiness']}</span><br/>
        <span class="readiness {r_cls}" style="margin-top:8px;display:inline-block;">{summary.readiness_level}</span>
    </div>""", unsafe_allow_html=True)

    st.divider()
    st.markdown(f"### {T['score_breakdown']}")
    import pandas as pd
    df = pd.DataFrame({"Question": [f"Q{i+1}" for i in range(len(scores))], "Score": scores})
    st.bar_chart(df.set_index("Question"), color="#6333ff")

    st.divider()
    col_l, col_r = st.columns(2)
    with col_l:
        st.markdown(f"### {T['strongest']}")
        st.success(summary.strongest_area)
        st.markdown(f"### {T['weakest']}")
        st.warning(summary.weakest_area)
    with col_r:
        st.markdown(f"### {T['recommendations']}")
        for i, tip in enumerate(summary.top_improvements, 1):
            st.markdown(f'<div class="eval-box eval-improve"><strong>{i}.</strong> {tip}</div>', unsafe_allow_html=True)

    st.divider()
    st.markdown(f"### {T['next_steps']}")
    cols = st.columns(len(summary.next_steps))
    for col, step in zip(cols, summary.next_steps):
        with col:
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,rgba(99,51,255,0.08),rgba(0,210,255,0.05));
                        border:1px solid rgba(99,51,255,0.3);border-radius:14px;
                        padding:18px;font-size:13px;color:#8090c0;line-height:1.7;">
                {step}
            </div>""", unsafe_allow_html=True)

    st.divider()
    with st.expander(T["full_review"]):
        for i,(q,a,ev) in enumerate(zip(st.session_state.questions,st.session_state.answers,st.session_state.evaluations)):
            s_cls = score_class(ev.score)
            st.markdown(f"""
            <div class="q-card" style="margin-bottom:12px;">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:16px;">
                    <div style="flex:1;">
                        <div class="q-label">Q{i+1} · {q.category}</div>
                        <div style="font-size:15px;font-weight:500;color:#d0d8ff;margin-bottom:8px;">{q.question}</div>
                        <div style="font-size:13px;color:#50507a;font-style:italic;">{a}</div>
                    </div>
                    <div class="score-circle {s_cls}" style="flex-shrink:0;">{ev.score}</div>
                </div>
            </div>""", unsafe_allow_html=True)

    st.divider()
    if st.button(T["new_interview"]):
        reset()
