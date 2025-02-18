<h1 align="center">Welcome to 🤖 AI-Powered-Health-Assistant 👋</h1>
<p>
</p>

The **AI-Powered Health Assistant** is a cutting-edge application that leverages artificial intelligence to provide medical assistance and user-friendly healthcare interactions. This project utilizes the **Falcon-7B-Instruct** model from Hugging Face, a powerful instruction-based large language model (LLM), to deliver accurate and context-aware medical responses. The system is designed to answer health-related queries and facilitate medical services such as appointment scheduling.

The project is built with **Streamlit**, offering an intuitive and interactive Chatbot interface that ensures a seamless user experience. The methodology includes model integration using **Hugging Face APIs** and dynamic conversation handling. The Chatbot is capable of processing natural language queries, analyzing symptoms, providing health-related insights, and responding appropriately to user prompts. Additionally, the assistant recognizes specific keywords like "appointment" and facilitates appointment booking functionalities by displaying relevant messages or guidance.

Key results from testing show that the **Falcon-7B-Instruct** model effectively generates relevant, informative, and coherent medical responses, making the AI-powered Chatbot a valuable tool for healthcare accessibility. The appointment scheduling feature further enhances user engagement, providing a personalized and interactive healthcare assistant experience.

### Conclusion
The **AI-Powered Health Assistant** demonstrates the potential of AI-driven healthcare solutions and its scalability, thereby bridging the gap between medical expertise and users seeking reliable health information.

## Installation

```bash
# Clone the repository:
git clone https://github.com/your-username/AI-Health-Assistant.git
cd AI-Health-Assistant

# Create a Virtual Environment (Optional but Recommended):
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows

# Install Dependencies:
pip install -r requirements.txt

# Run the Application:
streamlit run app.py
```

## Usage
Once the installation is complete, follow these steps to use the AI-Powered Health Assistant:

1️⃣ **Start the Application**
Run the following command:
streamlit run app.py

2️⃣ **Interacting with the Chatbot**
Enter health-related questions (e.g., "What are the symptoms of diabetes?").
Ask about medical conditions, treatments, or general health tips.
Use the keyword "appointment" to receive guidance on scheduling medical appointments.

3️⃣ **Expected Output**
The chatbot will generate context-aware responses using the Falcon-7B-Instruct model.
If an "appointment" query is detected, it will just print the pre-defined message.

4️⃣ **Example Query:**
💬 User: "What are the symptoms of flu?"
🤖 Chatbot: "Common flu symptoms include fever, cough, sore throat, muscle aches, fatigue, and headaches..."

### Author
👤 **Rohith Reddy.G.K**

Github: [@RohithReddyGK](https://github.com/RohithReddyGK)  
LinkedIn: [@rohithreddygk](https://linkedin.com/in/rohithreddygk)

### Show your support
Give a ⭐️ if this project helped you!

_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
