from src.config import *
from src.Telegram.client import Client
from src.menu import menu
import sys


def main():
    cfg_api = config_api()
    client = Client('anon', cfg_api.get('api_id'), cfg_api.get('api_hash'))
    client.start()
    client.update_account_info()
    menu(client)


if __name__ == '__main__':
    main()
