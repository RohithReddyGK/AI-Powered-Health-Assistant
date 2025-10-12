# Import necessary libraries.
import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini API key.
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  

if not GEMINI_API_KEY:
    st.error("⚠️ Please set your Gemini API key in the environment variable 'GEMINI_API_KEY'")
else:
    genai.configure(api_key=GEMINI_API_KEY)

# Function to get AI-generated response from Gemini.
def healthcare_chatbot(user_input):
    prompt = f"You are a medical expert. Answer concisely and directly:\n{user_input}"
    try:
        model = genai.GenerativeModel("gemini-2.5-flash-lite") 
        response = model.generate_content(prompt)
        return response.text.strip() if response.text else "No response generated."
    except Exception as e:
        return f"Error generating response: {e}"

# Function to book an appointment(Just a pre-fixed message).
def book_appointment():
    return "✅ Your appointment has been successfully booked!"

# Streamlit Web App User Interface.
def main():
    st.title("🤖 AI-Powered Health Assistant (Gemini)")
    st.subheader("Ask health-related questions, book appointments, and get instant AI responses!")

    user_input = st.text_area("💬 Enter Your Health Query:")

    if st.button("Submit"):
        if user_input.strip():
            with st.spinner("Generating response..."):
                if "appointment" in user_input.lower():
                    response = book_appointment()
                else:
                    response = healthcare_chatbot(user_input)

            st.success("AI Assistant:")
            st.write(response)
        else:
            st.warning("Please enter a valid query!!")

if __name__ == "__main__":
    main()
