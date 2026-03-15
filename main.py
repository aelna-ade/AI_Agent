import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types


load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    print("Hello from ai-agent!")
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    user_prompt = args.user_prompt
    print(f"User prompt: {user_prompt}")
    print("--------------------------------")
    response = client.models.generate_content(
    model="gemini-2.5-flash", contents=messages
    )
    if response.usage_metadata is None:
        raise RuntimeError("Failed API request")
    else: 
        print("Prompt tokens: ",response.usage_metadata.prompt_token_count)
        print("Response tokens: ", response.usage_metadata.candidates_token_count)
        
    print(response.text)

if __name__ == "__main__":
    main()



