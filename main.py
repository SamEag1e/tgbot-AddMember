from src.cfg import get_env
from src.session import create_session
from src.member import add_members


# ---------------------------------------------------------------------
def main():
    env_data = get_env()
    api_id = env_data["api_id"]
    api_hash = env_data["api_hash"]

    print("Welcome! What would you like to do?")
    print("1. Create a session")
    print("2. Add members from one group to another")

    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        session_name = (
            input("Enter a session name (default: 'session'): ").strip()
            or "session"
        )
        create_session(api_id, api_hash, session_name)
        return

    if choice == "2":
        session_name = input("Enter the session name: ").strip() or "session"
        add_members(api_id, api_hash, session_name)
        return

    print("Invalid choice! Please choose 1 or 2.")


# ---------------------------------------------------------------------
if __name__ == "__main__":
    main()
