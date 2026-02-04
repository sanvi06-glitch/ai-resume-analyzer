# AI Resume Analyzer

This project is a web-based application that analyzes how well a resume matches a given job description.

It is designed for students and job seekers to understand resume relevance and identify areas for improvement.

## Features
- Upload resume in PDF format
- Paste job description
- Calculates resume–job match percentage
- Displays improvement areas based on match score
- Clean and simple UI built with Streamlit

## Tech Stack
- Python
- Streamlit
- scikit-learn
- PDFPlumber

## How It Works
The application extracts text from the uploaded resume and compares it with the job description using TF-IDF vectorization and cosine similarity.

Based on the similarity score, it categorizes the resume alignment and provides improvement suggestions.

## How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
