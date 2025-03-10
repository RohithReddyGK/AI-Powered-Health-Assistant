# Import necessary libraries.
import streamlit as st
import os
import requests
# THE FOLLOWING PACKAGES CAN BE IMPORTED IF TRANSFORMERS WERE USED. 
#from transformers import AutoTokenizer, AutoModelForCausalLM
#import torch
#import nltk

# METHOD 1.
# Use a pipeline as a high-level helper
# from transformers import pipeline

# messages = [
#     {"role": "user", "content": "Who are you?"},
# ]
# pipe = pipeline("text-generation", model="tiiuae/falcon-7b-instruct", trust_remote_code=True)
# pipe(messages)

# METHOD 2.
# Load model directly.
# from transformers import AutoTokenizer, AutoModelForCausalLM

# tokenizer = AutoTokenizer.from_pretrained("tiiuae/falcon-7b-instruct", trust_remote_code=True)
# model = AutoModelForCausalLM.from_pretrained("tiiuae/falcon-7b-instruct", trust_remote_code=True)

# METHOD 3.
# 'API' method is used instead of'Tranformers'.
#This method directly deploys the model via api_url from "Hugging Face".No worries about 'model loading'.
HF_ACCESS_TOKEN = os.getenv("HF_ACCESS_TOKEN")  # Here,the token is stored in the environment variables as "HF_ACCESS_TOKEN".

# Using the model named: "tiiuae/falcon-7b-instruct" from Hugging Face.
API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
HEADERS = {"Authorization": f"Bearer {HF_ACCESS_TOKEN}"}

# Function to query Hugging Face API.
def query_huggingface_api(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    if response.status_code == 200:
        result = response.json()
        if isinstance(result, list) and result:
            return result[0].get("generated_text", "No response generated.")
        return "Unexpected API response format."
    return f"Error {response.status_code}: {response.text}"

# Function to get AI-generated response.
def healthcare_chatbot(user_input):
    prompt = f"You are a medical expert. Answer concisely and directly:\n{user_input}"
    payload = {
        "inputs": prompt,
        "parameters": {"max_length": 500}
    }
    
    response = query_huggingface_api(payload)
    
    # Remove the prompt from the response if it's included.
    if response.startswith(prompt):
        response = response[len(prompt):].strip()
    
    return response

# Function to book an appointment.
def book_appointment():
    return "Your appointment has been successfully booked!! You will receive further details via email."

# Streamlit Web App User-Interface.
def main():
    st.title("🤖 AI-Powered Health Assistant")
    st.subheader("Ask health-related questions, book appointments, and get AI-generated responses instantly!!")

    user_input = st.text_area("Enter Your Health Query:")
    
    if st.button("Submit"):
        if user_input.strip():
            with st.spinner("Generating response..."):
                if "appointment" in user_input.lower():
                    response = book_appointment()
                else:
                    response = healthcare_chatbot(user_input)

            st.success("AI Assistant: ")
            st.write(response)
        else:
            st.warning("Please enter a valid query!!")

if __name__ == "__main__":
    main()

#Fetching the Real-time data from the Public API.
# def fetch_health_data(query):
#     """Fetch Real-Time World Data from a Public API."""
#     url=f"https://api.healthdata.gov/v1/query?search={query}"
#     try:
#         response=requests.get(url)
#         if response.status_code==200:
#             data=response.json()
#             return data["results"][:3]  #Get top 3 results.
#         else:
#             return "No relevant health data found!!!!!"
#     except Exception as e:
#         return f"Error fetching data :{e}"

