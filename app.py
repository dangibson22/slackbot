import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

load_dotenv()

test_var = os.getenv('test')
print(f'env test: {test_var}')

app = App(token=os.getenv('bot_token'))

test_channel_id="C02R31VRR9C"

result = app.client.chat_postMessage(
    channel=test_channel_id,
    text="Hello world!"
)

if __name__ == "__main__":
    SocketModeHandler(app, os.getenv('app_token')).start()
