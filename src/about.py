from rich.console import Console
from rich.panel import Panel

def sobre():
    console = Console()
    console.print('Sobre', f'''\nContato\n\nE-mail: viniciuseduardo03@gmail.com\nWhatsapp: (16) 98244-6230\n''')
    console.input(' Pressione Enter para sair.')
