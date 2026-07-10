import os
import streamlit as st
from streamlit.errors import StreamlitSecretNotFoundError
from dotenv import load_dotenv
from groq import Groq

# ==========================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================

load_dotenv()

# ==========================================
# GET GROQ API KEY
# Works both locally (.env) and on Streamlit Cloud (Secrets)
# ==========================================

api_key = None

# Try Streamlit Secrets first
try:
    api_key = st.secrets["GROQ_API_KEY"]
except (StreamlitSecretNotFoundError, KeyError):
    pass

# If not found, use local .env
if not api_key:
    api_key = os.getenv("GROQ_API_KEY")

# If still not found, stop the app
if not api_key:
    raise ValueError(
        "❌ GROQ_API_KEY not found.\n"
        "Local: add it to your .env file.\n"
        "Deployment: add it to Streamlit Secrets."
    )

# ==========================================
# CONFIGURE GROQ
# ==========================================

client = Groq(api_key=api_key)

# ==========================================
# AI HEALTH RESPONSE
# ==========================================

def get_health_response(symptoms):
    """
    Generate educational healthcare guidance using Groq AI.
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

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are MediLink AI, an AI healthcare assistant designed for Nigeria. "
                        "Provide educational health information only. Never diagnose diseases "
                        "or prescribe medications."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.4,
            max_tokens=1200,
        )

        return response.choices[0].message.content

    except Exception as e:
        st.error(
            "⚠️ Sorry, the AI service is temporarily unavailable. Please try again in a few moments."
        )
        return f"❌ {str(e)}"