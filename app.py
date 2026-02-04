# 1️⃣ IMPORTS (TOP)
import streamlit as st
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# 2️⃣ PAGE CONFIG
st.set_page_config(page_title="AI Resume Analyzer", layout="centered")


# 3️⃣ 🔥 DESIGN + FONT CODE
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

/* Apply font everywhere */
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Background */
.stApp {
    background-color: #fff7ed;
}

/* Headings */
h1 {
    color: #6b6bb3;
}

h4 {
    color: #8b8bcf;
}

/* Upload & text areas */
.stFileUploader, .stTextArea {
    background-color: #ffffff;
    border-radius: 12px;
}

/* Match score card */
.match-box {
    background: linear-gradient(135deg, #4f46e5, #6d28d9);
    padding: 22px;
    border-radius: 18px;
    font-size: 22px;
    text-align: center;
    margin-top: 25px;
    color: #ffffff;
    font-weight: 600;
    box-shadow: 0px 6px 18px rgba(77,70,229,0.18);
}
</style>
""", unsafe_allow_html=True)


# 4️⃣ TITLE / HEADING
st.markdown(
    """
    <h1 style='text-align: center;'>AI RESUME ANALYZER</h1>
    <h4 style='text-align: center;'>
    SMART RESUME MATCHING FOR MODERN JOB ROLES
    </h4>
    """,
    unsafe_allow_html=True
)


# 5️⃣ FUNCTIONS (BACKEND LOGIC)
def read_resume(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()
    return text


def calculate_match(resume_text, job_text):
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([resume_text, job_text])
    score = cosine_similarity(vectors[0:1], vectors[1:2])
    return round(score[0][0] * 100, 2)


# 6️⃣ INPUT SECTION
col1, col2 = st.columns(2)

with col1:
    resume = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])

with col2:
    job_desc = st.text_area("🧾 Paste Job Description", height=170)


# 7️⃣ OUTPUT SECTION (WITH IMPROVEMENT COLUMN)
# 7️⃣ OUTPUT SECTION (WITH COLORED SCORE BOX)
if resume and job_desc:
    resume_text = read_resume(resume)
    match_score = calculate_match(resume_text, job_desc)

    # Decide color based on score
    if match_score >= 70:
        box_class = "match-box match-good"
    elif match_score >= 40:
        box_class = "match-box match-mid"
    else:
        box_class = "match-box match-low"

    left_col, right_col = st.columns([2, 1])

    with left_col:
        st.markdown(
            f"<div class='{box_class}'>🎯 Resume Match Score: <b>{match_score}%</b></div>",
            unsafe_allow_html=True
        )

        if match_score >= 70:
            st.success("🟢 Strong match – Great fit for this role!")
        elif match_score >= 40:
            st.warning("🟡 Moderate match – Some skills align")
        else:
            st.error("🔴 Weak match – Low alignment with role")

    with right_col:
        st.markdown("###  Where to Improve")

        if match_score < 40:
            st.markdown("- Add more role-specific skills")
            st.markdown("- Rewrite project descriptions clearly")
            st.markdown("- Use keywords from the job description")
        elif match_score < 70:
            st.markdown("- Strengthen matching technical skills")
            st.markdown("- Improve project relevance")
            st.markdown("- Reduce generic resume content")
        else:
            st.markdown("- Fine-tune wording for clarity")
            st.markdown("- Customize resume for each role")
            st.markdown("- Prepare for interviews")
