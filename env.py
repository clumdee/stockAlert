import os

# search for .env file with respect to the location of execution
# i.e. os.getcwd()
if os.path.exists("../.env"):
    from dotenv import load_dotenv
    load_dotenv(override=True)

# Line target
CHANNEL_ACCESS_TOKEN = os.getenv("CHANNEL_ACCESS_TOKEN")
TO_UID = os.getenv("TO_UID")