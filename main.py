import os
from dotenv import load_dotenv
from mastodon import Mastodon, StreamListener

class Bot(StreamListener):

  def __init__(self):
    super(Bot, self).__init__()

  def on_update(self, status):
    mastodon = setup()
    bot_dict = mastodon.account_verify_credentials()
    content = status['content'].replace('<p>', '').replace('</p>', '')
    account = status['account']['username']
    if bot_dict['username'] != account and content.startswith('にゃ'):
      if len(content) > 500:
        mastodon.toot(account + 'に壊されちゃったにゃー')
      else:
        mastodon.toot(content)


def setup():
  load_dotenv()
  mastodon = Mastodon(
    api_base_url  = os.environ['INSTANCE_URL'],
    client_id     = os.environ['CLIENT_KEY'],
    client_secret = os.environ['CLIENT_SECRET'],
    access_token  = os.environ['ACCESS_TOKEN']
  )
  return mastodon


def main():
  mastodon = setup()
  bot = Bot()
  mastodon.stream_local(bot)


if __name__ == '__main__':
  main()