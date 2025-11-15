import os
import google.generativeai as genai  # ✅ correct import

# Set API Key (you can also set permanently in system environment variables)
os.environ["GEMINI_API_KEY"] = "AIzaSyBDlo4HrZmdHn6JvB56ohtp3-KcEKl_KJg"

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create a model
model = genai.GenerativeModel("gemini-1.5-flash")

# Send a test message
response = model.generate_content("Hello Gemini! Are you working?")

print("API Key is working! Here's the response:")
print(response.text)
