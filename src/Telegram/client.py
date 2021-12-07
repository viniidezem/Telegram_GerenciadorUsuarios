from telethon import TelegramClient


class Client:

    def __init__(self, sessao, api_id, api_hash):
        self.client = TelegramClient(sessao, api_id, api_hash)
        self.me = {}
        self.chats_to_listen = []
        self.chats_to_forward = []
        self.chats_titles = []

    def start(self):
        self.client.loop.run_until_complete(self.client.connect())
        self.update_account_info()

    def update_account_info(self):
        self.me = self.client.loop.run_until_complete(self.client.get_me())

    def get_entidade(self, channel):
        self.client.loop.run_until_complete(self.client.get_entity(channel))
