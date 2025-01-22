from telethon.sync import TelegramClient


# ---------------------------------------------------------------------
def create_session(api_id, api_hash, session_name: str = "session"):
    """
    Logs in the user and generates a session file.
    Args:
        session_name (str): The name of the session file to be created.
    Returns:
        None
    """
    if not api_id or not api_hash:
        raise ValueError(
            "API_ID and API_HASH must be set as environment variables!"
        )

    client = TelegramClient(session_name, api_id, api_hash)

    # Start the login process
    print("Starting login process...")
    with client:
        try:
            client.start()
            print(f"Logged in successfully! Session name: {session_name}")
        except Exception as e:
            print(f"An error occurred during login: {e}")
