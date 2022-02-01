import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

def main():
    load_dotenv()

    app = App(token=os.getenv('bot_token'))

    test_channel_id="C02R31VRR9C"

    app.client.chat_postMessage(
        channel=test_channel_id,
        text="Hello world!"
    )

if __name__ == "__main__":
    # SocketModeHandler(app, os.getenv('app_token')).start()
    main()
