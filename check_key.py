# check_key.py
import os
from openai import OpenAI
from openai import AuthenticationError, RateLimitError
from dotenv import load_dotenv

load_dotenv()  # loads .env if available

api_key = os.getenv("OPENAI_API_KEY")

def test_key_validity(key: str):
    try:
        client = OpenAI(api_key=key)
        # List available models; auth failure or quota issues may throw error
        result = client.models.list()
        print("✅ API key is valid. Models fetched:", [m.id for m in result.data][:3])
        return True
    except AuthenticationError:
        print("❌ API key is invalid or unauthorized.")
        return False
    except RateLimitError as e:
        print("⏱ Rate limit error or quota exhausted:", e)
        return False
    except Exception as e:
        print("⚠️ Other error occurred:", e)
        return False

if __name__ == "__main__":
    test_key_validity(api_key)
