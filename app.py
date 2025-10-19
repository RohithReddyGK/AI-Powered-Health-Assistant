import streamlit as st
import google.generativeai as genai
from streamlit_lottie import st_lottie
import json
import os
import time
from PIL import Image
import base64

# ---------------- CONFIG ----------------
st.set_page_config(page_title="AI Health Assistant", page_icon="🤖", layout="centered")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    st.error("⚠️ Please set your GEMINI_API_KEY environment variable")
else:
    genai.configure(api_key=GEMINI_API_KEY)

# ---------------- AI RESPONSE ----------------
def healthcare_chatbot(user_input):
    prompt = f"You are a medical expert. Answer concisely and directly:\n{user_input}"
    try:
        model = genai.GenerativeModel("gemini-2.5-flash-lite")
        response = model.generate_content(prompt)
        return response.text.strip() if response.text else "No response generated."
    except Exception as e:
        return f"Error generating response: {e}"

def book_appointment():
    return "✅ Your appointment has been successfully booked!"

# ---------------- LOAD LOTTIE ANIMATION ----------------
def load_lottie_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# ---------------- MAIN APP ----------------
def main():
    if "started" not in st.session_state:
        st.session_state.started = False
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # --- Full-Page Doctor Animation ---
    if not st.session_state.started:
        try:
            lottie_json = load_lottie_json("assets/Doctor.json")
            st_lottie(lottie_json, height=500, key="start_anim")
        except:
            st.info("🎬 Animation file not found (Doctor.json)")
        time.sleep(3)
        st.session_state.started = True
        st.rerun()
        return

    # --- Chat Interface ---
    col1, col2 = st.columns([1, 6])
    with col1:
        try:
            lottie_json = load_lottie_json("assets/AI Robot.json")
            st_lottie(lottie_json, height=100, key="chat_anim")
        except:
            st.info("🎬 Chat animation file not found (AI Robot.json)")
    with col2:
        st.markdown("<h1>AI-Health Assistant Chatbot</h1>", unsafe_allow_html=True)

    st.markdown(
        '<div style="text-align:center;"><h4>Know about health, ask related questions or even book appointments by just typing "appointment"!</h4></div>', 
        unsafe_allow_html=True)
    st.markdown("---")

    # CSS for chat bubbles, textarea, and auto-scroll.
    st.markdown("""
    <style>
    @keyframes slideRight {
        from {transform: translateX(100%); opacity:0;}
        to {transform: translateX(0); opacity:1;}
    }
    @keyframes slideLeft {
        from {transform: translateX(-100%); opacity:0;}
        to {transform: translateX(0); opacity:1;}
    }

    .chat-textarea textarea {
        min-height: 60px !important;
        border: 2px solid black !important;
        border-radius: 8px !important;
        padding: 10px !important;
        font-size: 16px !important;
        background-color: white !important;
        width: 100% !important;
    }

    .chat-container {
        max-height: 60vh;
        overflow-y: auto;
    }
    </style>
    """, unsafe_allow_html=True)

    # --- Chat container ---
    chat_container = st.container()
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for chat in st.session_state.chat_history:
        if chat["role"] == "user":
            st.markdown(
                f"""
                <div style='
                    text-align:right; 
                    background-color:#3B82F6; 
                    color:white; 
                    padding:10px; 
                    border-radius:15px; 
                    max-width:70%; 
                    margin-left:auto; 
                    margin-bottom:10px;
                    animation: slideRight 0.5s ease-out;
                '>🧑 {chat['content']}</div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""
                <div style='
                    text-align:left; 
                    background-color:#E5E7EB; 
                    color:black; 
                    padding:10px; 
                    border-radius:15px; 
                    max-width:70%; 
                    margin-right:auto; 
                    margin-bottom:10px;
                    animation: slideLeft 0.5s ease-out;
                '>👨‍⚕️ {chat['content']}</div>
                """,
                unsafe_allow_html=True,
            )
    st.markdown('</div>', unsafe_allow_html=True)  # close chat container

    # --- Chat Input ---
    user_input = st.text_area(
        "Type your health query here...",
        value="",
        height=80,
        key="custom_input",
        placeholder="Type your health query here...",
        label_visibility="hidden"
    )

    # --- Send Button and Download Icon ---
    col1, col2 = st.columns([1, 0.1])
    with col1:
        if st.button("Send") and user_input.strip() != "":
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            with st.spinner("🤖 Thinking..."):
                if "appointment" in user_input.lower():
                    response = book_appointment()
                else:
                    response = healthcare_chatbot(user_input)
                time.sleep(0.5)
            st.session_state.chat_history.append({"role": "assistant", "content": response})
            st.rerun()

    with col2:
        if st.session_state.chat_history:
        
            chat_text = "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in st.session_state.chat_history])
            chat_bytes = chat_text.encode()
            chat_b64 = base64.b64encode(chat_bytes).decode()

  
            with open("assets/File_Download.png", "rb") as f:
                icon_b64 = base64.b64encode(f.read()).decode()

            st.markdown(f"""
            <style>
            .download-icon {{
                width: 40px;
                cursor: pointer;
                transition: transform 0.3s, box-shadow 0.3s;
            }}

            .download-icon:hover {{
                transform: scale(1.8) rotate(15deg);
                box-shadow: 0 0 20px rgba(0,0,0,0.7);
            }}
            </style>

            <a href="data:text/plain;base64,{chat_b64}" download="Health_Chat_History.txt">
                <img src="data:image/png;base64,{icon_b64}" class="download-icon" title="Download Chat History"/>
            </a>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
