# Responsive Chatbot

## Overview
This is an AI-powered chatbot built using **Streamlit**, **LangChain**, and **Groq API**. The chatbot leverages the `Gemma2-9b-It` model to provide intelligent and interactive responses to user queries in real-time.

## Features
- **Conversational AI**: Uses Groq API to generate human-like responses.
- **Streamlit UI**: Provides a simple and interactive web-based interface.
- **Environment Variable Support**: Uses `.env` files to manage API keys securely.
- **State Management**: Maintains conversation history for better interactions.

## Tech Stack
- **Python**
- **Streamlit**
- **LangChain**
- **Groq API**
- **dotenv** (for environment variables)

## Installation & Setup

### 1. Clone the Repository
```sh
git clone https://github.com/your-username/chatbot.git
cd chatbot
```

### 2. Set Up a Virtual Environment
```sh
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Set Up API Key
Create a `.env` file in the project root and add your Groq API key:
```sh
GROQ_API_KEY=your_api_key_here
```

### 5. Run the Chatbot
```sh
streamlit run main.py
```
This will open the chatbot interface in your browser.

## Usage
1. Start the chatbot using `streamlit run main.py`.
2. Enter your query in the input field.
3. The chatbot will generate responses using the Groq API.
4. Type "exit" to end the conversation.

## File Structure
```
chatbot/
├── .venv/               # Virtual environment (ignored in Git)
├── .env                 # Environment variables (ignored in Git)
├── main.py              # Main Streamlit application
├── requirements.txt     # Dependencies
├── README.md            # Project documentation
```

## Troubleshooting
- **Missing API Key Error**: Ensure you have added `GROQ_API_KEY` in `.env`.
- **Streamlit Not Found**: Install dependencies using `pip install -r requirements.txt`.
- **Web App Not Opening**: Try manually opening the URL displayed in the terminal.

## Contributing
Feel free to fork this repository, make changes, and submit pull requests. Contributions are welcome!

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for more details.

## Author
[Your Name](https://github.com/your-username)

