
from telethon.tl.functions.channels import InviteToChannelRequest, EditBannedRequest
import os
from telethon.tl.types import ChatBannedRights
from src.leitorPlanilha import leitorPlanilha
from src.Telegram.instances import retornaInstancia
from src.leitorMsg import leitorMsgAviso, leitorMsgExclusao, leitorMsgInclusao
from src.config import config_plan


def _confirmacao():
    print("Deseja continuar S/N ?")
    valor = input("R: ")
    if valor.lower() == 's':
        return True
    else:
        return False


async def _removeUsers(client):

    plan = leitorPlanilha('1')
    for x in plan:
        nome = x[0]
        telefone = '+' + str(x[1])
        dataVencimento = x[2]
        plano = x[3]
        print(nome, telefone, dataVencimento, plano)

    confirmacao = _confirmacao()
    if confirmacao:
        for x in plan:
            nome = x[0]
            telefone = '+' + str(x[1])
            dataVencimento = x[2]
            plano = x[3]
            instancias = retornaInstancia(plano)
            await client.client.get_dialogs()

            msgExclusao = leitorMsgExclusao()

            for laco in instancias.split(','):
                channel = await client.client.get_entity(int(laco))
                # await client.client(InviteToChannelRequest(channel, [telefone]))
                await client.client(EditBannedRequest(channel, telefone, ChatBannedRights(
                    until_date=None,
                    view_messages=True
                )))
            await client.client.send_message(telefone, msgExclusao)
        print('Usuarios removidos')
    else:
        print('Ação Cancelada')


def removeUsers(client):
    with client.client:
        client.client.loop.run_until_complete(_removeUsers(client))


async def _avisarUsers(client):
    plan = leitorPlanilha('2')
    for x in plan:
        nome = x[0]
        telefone = '+' + str(x[1])
        dataVencimento = x[2]
        plano = x[3]
        print(nome, telefone, dataVencimento, plano)

    confirmacao = _confirmacao()
    if confirmacao:
        for x in plan:
            telefone = '+' + str(x[1])
            plano = x[3]
            #instancias = retornaInstancia(plano)
            await client.client.get_dialogs()

            msgAviso = leitorMsgAviso()

            await client.client.send_message(telefone, msgAviso)

            print('Usuarios alertados')
    else:
        print('Ação Cancelada')


def avisarUsers(client):
    with client.client:
        client.client.loop.run_until_complete(_avisarUsers(client))


async def _addUsers(client):

    plan = leitorPlanilha('3')
    for x in plan:
        nome = x[0]
        telefone = '+' + str(x[1])
        dataInicio = x[2]
        plano = x[3]
        print(nome, telefone, dataInicio, plano)

    confirmacao = _confirmacao()
    if confirmacao:
        for x in plan:
            telefone = '+' + str(x[1])
            plano = x[3]
            instancias = retornaInstancia(plano)
            await client.client.get_dialogs()
            user = await client.get_entity(telefone)
            msgInclusao = leitorMsgInclusao()

            for laco in instancias.split(','):
                channel = await client.client.get_entity(int(laco))
                await client(InviteToChannelRequest(channel,[user]))
            await client.client.send_message(telefone, msgInclusao)

        print('Usuarios Adicionados')
    else:
        print('Ação Cancelada')


def addUsers(client):
    with client.client:
        client.client.loop.run_until_complete(_addUsers(client))

