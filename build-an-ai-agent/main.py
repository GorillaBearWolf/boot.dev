import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()

    args = sys.argv[1:]

    if not args:
        print("Error, exiting")
        sys.exit(1)
    user_prompt = args[0]

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )

    if " ".join(args).endswith("--verbose"):
        ptokens = response.usage_metadata.prompt_token_count
        rtokens = response.usage_metadata.candidates_token_count

        print(
            f"User prompt: {user_prompt}\nPrompt tokens: {ptokens}\nResponse tokens: {rtokens}\n"
        )
    print(f"Response text: {response.text}")


if __name__ == "__main__":
    main()
