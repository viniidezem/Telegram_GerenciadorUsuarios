from rich.console import Console
from rich.style import Style
from rich.panel import Panel
from src.Telegram.gerenciarUsuarios import removeUsers, avisarUsers, addUsers
from src.about import sobre


def menu(client):
    console = Console()
    console.clear()
    console.print('\nTelegram Control\n')

    console.print(
        '\n [1] Incluir Novos\n [2] Remover Vencidos\n [3] Enviar Mensagem de Vencimento\n [4] Sobre\n [5] Sair\n')
    value = console.input(' R: ')

    if value == '1':
        addUsers(client)
        console.input('Pressione qualquer tecla para continuar ...')
        console.clear()
        menu(client)

    elif value == '2':
        removeUsers(client)
        console.input('Pressione qualquer tecla para continuar ...')
        console.clear()
        menu(client)

    elif value == '3':
        avisarUsers(client)
        console.input('Pressione qualquer tecla para continuar ...')
        console.clear()
        menu(client)

    elif value == '4':
        sobre()
        console.input('Pressione qualquer tecla para continuar ...')
        console.clear()
        menu(client)

    elif value == '5':
        quit()
