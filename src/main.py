import datetime

from linebot.v3.messaging import ApiClient, Configuration, MessagingApi, TextMessage
from linebot.v3.messaging.models.push_message_request import PushMessageRequest

import add_path
from env import LINE_TOKEN, LINE_USERS
from tickers import tickers
from utils import get_stock_info


def main():
    # get stock info and construct message
    date_now = datetime.datetime.now().strftime("%Y-%m-%d")
    summary = f"$ Daily summary $ ({date_now}) \n"
    for title, (ticker, info) in tickers.items():
        dt, val = get_stock_info(ticker, info)
        s = f"{title} ({info}) = {val}"
        summary = "\n".join([summary, s])

    # send Line message
    configuration = Configuration(access_token = LINE_TOKEN)
    api_client = ApiClient(configuration) 
    line_bot_api = MessagingApi(api_client)
    
    line_text = TextMessage(
        text=summary,
        emojis=[
            {"index": 0, "productId": "5ac21542031a6752fb806d55", "emojiId": "180"},
            {"index": 16, "productId": "5ac21542031a6752fb806d55", "emojiId": "214"},
        ],
    )
    for u in LINE_USERS:
        line_bot_api.push_message(PushMessageRequest(to=u, messages=[line_text]))


if __name__ == "__main__":
    main()
