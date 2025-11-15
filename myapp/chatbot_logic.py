import os
from google import genai
from dotenv import load_dotenv
from pathlib import Path
import traceback

# Get the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file
load_dotenv(os.path.join(BASE_DIR, '.env'))

# Initialize chat as None
chat = None

# Configure the Gemini API key
def initialize_api():
    global chat
    
    try:
        debug_mode = getattr(settings, 'CHATBOT_DEBUG', True)
        if debug_mode:
            print("Chatbot Debug: Starting API initialization")
        api_key = os.getenv("GEMINI_API_KEY", "").strip()
        if debug_mode:
            print("Chatbot Debug: Creating Gemini client")
            
        # Add error handling for production
        if not api_key:
            raise ValueError("Gemini API key not found in environment variables")
            
        if not api_key:
            print("Chatbot Debug: Checking for .env file...")
            env_path = os.path.join(BASE_DIR, '.env')
            if os.path.exists(env_path):
                print(f"Chatbot Debug: .env file found at {env_path}")
                try:
                    with open(env_path, 'r') as f:
                        env_content = f.read().strip()
                        print(f"Chatbot Debug: .env file content (first line): {env_content.split(chr(10))[0]}")
                except Exception as e:
                    print(f"Chatbot Debug: Error reading .env file: {str(e)}")
                print("Chatbot Debug: Please ensure GEMINI_API_KEY is correctly set in the .env file")
            else:
                print(f"Chatbot Debug: No .env file found at {env_path}")
            return False
            
        print(f"Chatbot Debug: API key found (length: {len(api_key)})")
        
        if len(api_key) < 30:  # Basic validation - API keys are typically longer
            print("Chatbot Debug: API key appears too short - likely invalid")
            return False
            
        try:
            # Initialize Gemini client
            client = genai.Client(api_key=api_key)
            
            # Create a chat with the model
            chat = client.chats.create(model="gemini-2.0-flash")
            
            # Test the chat
            test_response = chat.send_message("Test connection")
            if test_response and hasattr(test_response, 'text'):
                print("Chatbot Debug: Chat initialization successful")
                return True
            else:
                print("Chatbot Debug: Chat initialization failed - no valid response")
                return False
        except Exception as config_error:
            print(f"Chatbot Debug: Configuration error: {str(config_error)}")
            return False
        
    except Exception as e:
        print(f"Chatbot Debug: API initialization failed with error: {str(e)}")
        print("Chatbot Debug: Stack trace:", traceback.format_exc())
        return False

# Initialize the API when the module is loaded
initialize_api()


def get_bot_response(user_input):
    """
    Gets a response from the Gemini LLM based on user input.
    Includes a specific prompt for photography questions.
    """
    global chat
    
    print("Chatbot Debug: Starting response generation")
    print(f"Chatbot Debug: User input received: {user_input}")
    
    # Try to initialize the API if chat is None
    if chat is None:
        print("Chatbot Debug: Chat is None, attempting to initialize")
        if not initialize_api():
            print("Chatbot Debug: API initialization failed")
            return "Chatbot is not configured. Please ensure your API key is correct."

    # Prepare the prompt with photography context
    context = """You are a helpful photography assistant for CamFiesta, a camera e-commerce website. 
    Please provide clear, concise advice about photography, cameras, and equipment. 
    Keep answers under 100 words unless more detail is needed.
    Only answer photography-related questions."""
    
    prompt = f"{context}\n\nUser's question: {user_input}"
    
    try:
        print("Chatbot Debug: Attempting to send message")
        response = chat.send_message(prompt)
        print("Chatbot Debug: Message sent successfully")
        return response.text.strip()
    except Exception as e:
        print(f"Chatbot Debug: First attempt failed with error: {str(e)}")
        print("Chatbot Debug: Attempting to reinitialize API")
        
        if initialize_api():
            try:
                print("Chatbot Debug: Second attempt to send message")
                response = chat.send_message(prompt)
                print("Chatbot Debug: Second attempt successful")
                return response.text.strip()
            except Exception as e2:
                print(f"Chatbot Debug: Second attempt failed with error: {str(e2)}")
                print("Chatbot Debug: Please check if your API key is valid")
        else:
            print("Chatbot Debug: API reinitialization failed")
        
        return "I'm having trouble connecting to the API. Please check if your API key is valid and try again."