

def leitorMsgAviso():
    with open('ArquivosConfiguracao/msgAviso.txt', 'r', encoding='utf-8') as arquivo:
        msgAviso = arquivo.read()
    return msgAviso


def leitorMsgExclusao():
    with open('ArquivosConfiguracao/msgExclusao.txt', 'r', encoding='utf-8') as arquivo:
        msgAviso = arquivo.read()
    return msgAviso

def leitorMsgInclusao():
    with open('ArquivosConfiguracao/msgInclusao.txt', 'r', encoding='utf-8') as arquivo:
        msgAviso = arquivo.read()
    return msgAviso
