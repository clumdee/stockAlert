import os

# search for .env file with respect to the location of execution
# i.e. os.getcwd()
if os.path.exists("../.env"):
    from dotenv import load_dotenv
    load_dotenv(override=True)

# Line target
LINE_TOKEN = os.getenv("LINE_TOKEN")
LINE_USERS = [u for u in os.getenv("LINE_USERS").split(",")]