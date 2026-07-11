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
# ==========================================

api_key = None

try:
    api_key = st.secrets["GROQ_API_KEY"]
except (StreamlitSecretNotFoundError, KeyError):
    pass

if not api_key:
    api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "❌ GROQ_API_KEY not found.\n"
        "Local: add it to your .env file.\n"
        "Deployment: add it to Streamlit Secrets."
    )

# ==========================================
# INITIALIZE GROQ CLIENT
# ==========================================

client = Groq(api_key=api_key)

# ==========================================
# AI HEALTH RESPONSE
# ==========================================

def get_health_response(symptoms):

    st.write("✅ DEBUG 1: Entered get_health_response()")

    symptoms = symptoms.strip()

    if not symptoms:
        st.write("✅ DEBUG 2: Empty symptoms")
        return "⚠️ Please describe your symptoms before requesting a health assessment."

    prompt = f"""
You are MediLink AI, an AI-powered healthcare education assistant designed specifically for people living in Nigeria.

The user reports the following symptoms:

{symptoms}

Provide educational health information only.

Never diagnose diseases.
Never prescribe medications.

Respond in Markdown.
"""

    try:

        st.write("✅ DEBUG 3: About to call Groq API")

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are MediLink AI. "
                        "Provide educational healthcare information only."
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

        st.write("✅ DEBUG 4: Groq API returned successfully")

        ai_response = response.choices[0].message.content

        st.write("✅ DEBUG 5: Extracted AI response")

        return ai_response

    except Exception as e:

        st.error("❌ DEBUG ERROR")
        st.exception(e)

        return f"ERROR: {str(e)}"