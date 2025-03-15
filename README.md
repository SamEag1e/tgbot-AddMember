# Telegram Bot for Adding Members

A Telegram bot that utilizes the **Telethon** library to create a session and add members from one Telegram group to another.

## Description
This bot allows you to create a session using the Telegram API and add members from one group to another. The bot uses the **Telethon** library to interact with Telegram's API. Users can choose to either create a new session or add members from one group to another.

## Features
- **Create a session**: Establish a connection to the Telegram API using your **API_ID** and **API_HASH**.
- **Add members**: Add members from one Telegram group to another.

## Tech Stack
- **Python** (Programming Language)
- **Telethon Library** (Telegram API Client)
- **Telegram API** (For interacting with Telegram)

## Prerequisites
Before you begin, ensure you have the following:
- A Telegram account.
- **API_ID** and **API_HASH** from [Telegram's Developer API](https://my.telegram.org/auth).

## Installation
* Clone the repository:
```bash
git clone https://github.com/SamEag1e/tgbot-AddMember.git
```
* Navigate to the project directory:
```
cd tgbot-AddMember
```
* Create a virtual environment:
```
python -m venv env
```
* Activate the virtual environment:
  * On Windows: ```.\env\Scripts\activate```
  * On macOS and Linux: ```source env/bin/activate```
* Install the required dependencies:
```
pip install -r requirements.txt
```
## Environment Variables
Create a .env file in the project root directory and add the following variables:
```
API_ID=your_api_id
API_HASH=your_api_hash
```
## Usage
Run the bot using:
```
python main.py
```
## Contributing
* Fork the repository.
* Create a new branch (git checkout -b feature-branch).
* Commit your changes (git commit -m 'Add new feature').
* Push to the branch (git push origin feature-branch).
* Open a pull request.
## Contact
For any inquiries, please contact me at:

* **Email**: samadeagle@yahoo.com
* **Telegram**: https://t.me/SamadTnd
* **BotTelegram**(may be down): https://t.me/Roof_real_estate_bot
## License
This project is licensed under the MIT License.
