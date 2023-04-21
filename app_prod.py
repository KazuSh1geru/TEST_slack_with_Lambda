# export SLACK_BOT_TOKEN=xoxb-518476454566-5144335884597-xzztfTIhPhLnmrSoQmCgotTN
# export SLACK_CLIENT_ID=518476454566.5140670230534
# export SLACK_CLIENT_SECRET=29482127ff5151eab499e6846e5fe091
# export SLACK_SIGNING_SECRET=fb3f0dc5de8bddcb41f289c7bb64bc1b
# npm install -g serverless
# serverless plugin install -n serverless-python-requirements
# serverless deploy --aws-profile data-root-user


import os

from slack_bolt import App
from slack_bolt.adapter.aws_lambda import SlackRequestHandler


# Install the Slack app and get xoxb- token in advance
app = App(
    # リクエストの検証に必要な値
    # Settings > Basic Information > App Credentials > Signing Secret で取得可能な値
    signing_secret=os.environ["SLACK_SIGNING_SECRET"],
    token=os.environ.get("SLACK_BOT_TOKEN"),
    # AWS Lamdba では、必ずこの設定を true にしておく必要があります
    process_before_response=True,
)

@app.command("/hello-socket-mode")
def hello_command(ack, body):
    user_id = body["user_id"]
    ack(f"Hi, <@{user_id}>!")

@app.event("app_mention")
def event_test(say):
    say("Hi there!")

def handler(event, context):
    slack_handler = SlackRequestHandler(app=app)
    return slack_handler.handle(event, context)