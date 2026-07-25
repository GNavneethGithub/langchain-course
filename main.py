import os

from dotenv import load_dotenv
load_dotenv()

def main():
    gemini_api_key = os.getenv("Gemini_API_Key")
    print(f"Hello from langchain-course! Your API key is: {gemini_api_key}")

if __name__ == "__main__":
    main()
