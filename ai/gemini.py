import os
import streamlit as st
from streamlit.errors import StreamlitSecretNotFoundError
from dotenv import load_dotenv
import google.generativeai as genai

# ==========================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================

load_dotenv()

# ==========================================
# GET GEMINI API KEY
# Works both locally (.env) and on Streamlit Cloud (Secrets)
# ==========================================

api_key = None

# Try Streamlit Secrets first
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except (StreamlitSecretNotFoundError, KeyError):
    pass

# If not found, use local .env
if not api_key:
    api_key = os.getenv("GEMINI_API_KEY")

# If still not found, stop the app
if not api_key:
    raise ValueError(
        "❌ GEMINI_API_KEY not found.\n"
        "Local: add it to your .env file.\n"
        "Deployment: add it to Streamlit Secrets."
    )

# ==========================================
# CONFIGURE GEMINI
# ==========================================

genai.configure(api_key=api_key)
st.write("Using API key:", api_key[:10] + "...")

model = genai.GenerativeModel("gemini-2.0-flash")

# ==========================================
# AI HEALTH RESPONSE
# ==========================================

def get_health_response(symptoms):
    """
    Generate educational healthcare guidance using Gemini AI.
    """

    symptoms = symptoms.strip()

    if not symptoms:
        return (
            "⚠️ Please describe your symptoms before requesting a health assessment."
        )

    prompt = f"""
You are MediLink AI, an AI-powered healthcare education assistant designed specifically for people living in Nigeria.

The user reports the following symptoms:

{symptoms}

Your responsibility is to provide EDUCATIONAL HEALTH INFORMATION ONLY.

Respond using this exact format.

# 👋 Summary
Briefly summarize what the user reported.

# 🩺 Possible Health Conditions
List 3–5 possible conditions that may explain the symptoms.

For each condition:
- Give a simple explanation.
- Never state that the user definitely has the condition.

# ❓ Additional Questions
Ask 3–5 follow-up questions that would help a healthcare professional understand the situation better.

# 🏠 Self-Care Tips
Provide safe, general home-care advice.

# 🚨 When to Seek Medical Care
Clearly explain warning signs that require visiting a hospital or emergency department immediately.

# Nigerian Health Advice
Provide practical advice relevant to Nigeria.

Where appropriate mention:
- Primary Health Centres (PHCs)
- Government hospitals
- Mosquito prevention
- Safe drinking water
- Good hygiene
- Routine vaccinations

# ⚠️ Medical Disclaimer
State clearly that:
- This is educational information only.
- It is NOT a medical diagnosis.
- It does NOT replace a qualified healthcare professional.

Rules:
- Never diagnose diseases.
- Never prescribe medications.
- Never recommend drug dosages.
- Use simple English.
- Be supportive and reassuring.
- Use bullet points where appropriate.
- Format your response neatly using Markdown.
"""

    try:

        response = model.generate_content(prompt)
        st.write("DEBUG: Gemini request completed")

        if response and hasattr(response, "text"):
            return response.text

        return (
            "⚠️ MediLink AI could not generate a response at the moment. "
            "Please try again."
        )

    except Exception as e:
        import traceback
        st.error("Gemini Error:")
        st.exception(e)

        traceback.print_exc()

        return f"❌ {str(e)}"
        