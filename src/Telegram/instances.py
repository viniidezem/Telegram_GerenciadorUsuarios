from configparser import ConfigParser
from telethon.tl.functions.channels import InviteToChannelRequest


def retornaInstancia(plano):
    parser = ConfigParser()
    parser.read('ArquivosConfiguracao/instances.cfg')

    instancias = parser[plano]['para']
    return instancias
