import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get API key
API_KEY = os.getenv('GEMINI_API_KEY')
print(f"API Key loaded: {API_KEY[:20]}..." if API_KEY else "API Key not found!")

# Configure Gemini
try:
    genai.configure(api_key=API_KEY)
    print("[OK] API key configured successfully")
    
    # List available models
    print("\nAvailable models:")
    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods:
            print(f"  - {model.name}")
    
    # Test a simple generation
    print("\nTesting API with a simple prompt...")
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Say hello")
    print(f"[OK] API is working! Response: {response.text}")
    
except Exception as e:
    print(f"[ERROR] {e}")
    print("\nPossible issues:")
    print("1. API key is invalid or expired")
    print("2. API key doesn't have proper permissions")
    print("3. Gemini API is not enabled for this project")
    print("4. Network connectivity issues")
    print("\nPlease verify your API key at: https://makersuite.google.com/app/apikey")
