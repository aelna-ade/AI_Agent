import os
import sys
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from functions.prompt import system_prompt
from functions.tools import available_functions
from functions.call_function import call_function


load_dotenv()


api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def main():
    print("Hello from ai-agent!")
    parser = argparse.ArgumentParser(description="Chatbot Agent")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    user_prompt = args.user_prompt
    

    config = types.GenerateContentConfig(
        system_instruction=system_prompt,
        temperature=0,
        tools=[available_functions]
    )
    

    for iteration in range(20):
        if args.verbose:
            print(f"\n--- Iteration {iteration + 1} ---")
        

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=config
        )
        
        if response.usage_metadata is None:
            raise RuntimeError("Failed API request")
        

        if response.candidates is None or len(response.candidates) == 0:
            raise RuntimeError("No candidates in response")
        

        for candidate in response.candidates:
            messages.append(candidate.content)
        

        if response.function_calls is not None and len(response.function_calls) > 0:

            function_responses = []
            
            for function_call in response.function_calls:

                function_call_result = call_function(function_call, verbose=args.verbose)
                

                if not function_call_result.parts or len(function_call_result.parts) == 0:
                    raise RuntimeError("Function call result has no parts")
                

                function_response = function_call_result.parts[0].function_response
                if function_response is None:
                    raise RuntimeError("FunctionResponse is None")
                

                if function_response.response is None:
                    raise RuntimeError("Function response is None")
                

                function_responses.append(function_call_result.parts[0])
                

                if args.verbose:
                    print(f"-> {function_response.response}")
            
            # Ajouter les réponses de fonction à l'historique (role="user")
            messages.append(types.Content(role="user", parts=function_responses))
            

            continue
            
        else:

            if args.verbose:
                print("\nFinal response:")
            print(response.text)
            return  
    

    print("Error: Maximum iterations (20) reached without a final response.")
    sys.exit(1)


if __name__ == "__main__":
    main()