import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def main(argv):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001", contents=argv[1]
        )
        ptokens = response.usage_metadata.prompt_token_count
        rtokens = response.usage_metadata.candidates_token_count

        print(
            f"{response.text}\n\nPrompt tokens: {ptokens}\nResponse tokens: {rtokens}"
        )

    except IndexError:
        print("Error, exiting")
        exit(1)


if __name__ == "__main__":
    main(sys.argv)
