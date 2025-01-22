import os
from dotenv import load_dotenv


# ---------------------------------------------------------------------
def get_env():
    load_dotenv()
    env_data = {
        "api_id": os.getenv("API_ID"),
        "api_hash": os.getenv("API_HASH"),
    }
    if not env_data["api_id"] or not env_data["api_hash"]:
        raise ValueError("API_ID and API_HASH must be set in the .env file!")
    return env_data
