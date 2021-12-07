from configparser import ConfigParser

def _get_config_api():
    parser = ConfigParser()
    parser.read('ArquivosConfiguracao/config.cfg')
    sections = parser.has_section('CONFIG_API')
    if sections == False:
        return {}
    api_id = parser.get('CONFIG_API', 'api_id')
    api_hash = parser.get('CONFIG_API','api_hash')
    return {
        'api_id': api_id,
        'api_hash': api_hash
    }

def _set_config_api(cfg):
    parser = ConfigParser()
    parser.read('ArquivosConfiguracao/config.cfg')
    parser.add_section('CONFIG_API')
    parser.set('CONFIG_API', 'api_id', cfg.get('api_id'))
    parser.set('CONFIG_API', 'api_hash', cfg.get('api_hash'))
    with open('config.cfg', 'w') as file:
        parser.write(file)
    file.close()


def _get_config_plan():
    parser = ConfigParser()
    parser.read('ArquivosConfiguracao/config.cfg')
    sections = parser.has_section('CONFIG_PLANILHA')
    if sections == False:
        return {}
    key_sheets = parser.get('CONFIG_PLANILHA', 'key_sheets')
    json_file = parser.get('CONFIG_PLANILHA', 'json_file')
    nome_planilha = parser.get('CONFIG_PLANILHA', 'nome_planilha')
    coluna_nome = parser.get('CONFIG_PLANILHA', 'coluna_nome')
    coluna_telefone = parser.get('CONFIG_PLANILHA', 'coluna_telefone')
    coluna_plano = parser.get('CONFIG_PLANILHA', 'coluna_plano')
    coluna_datainicio = parser.get('CONFIG_PLANILHA', 'coluna_datainicio')
    coluna_datafim = parser.get('CONFIG_PLANILHA', 'coluna_datafim')

    return {
        'key_sheets': key_sheets,
        'json_file': json_file,
        'nome_planilha': nome_planilha,
        'coluna_nome': coluna_nome,
        'coluna_telefone': coluna_telefone,
        'coluna_plano': coluna_plano,
        'coluna_datainicio': coluna_datainicio,
        'coluna_datafim': coluna_datafim}


def _set_config_plan(cfg):
    parser = ConfigParser()
    parser.add_section('CONFIG_PLANILHA')
    parser.read('ArquivosConfiguracao/config.cfg')
    parser.set('CONFIG_PLANILHA', 'key_sheets', cfg.get('key_sheets'))
    parser.set('CONFIG_PLANILHA', 'json_file', cfg.get('json_file'))
    parser.set('CONFIG_PLANILHA', 'nome_planilha', cfg.get('nome_planilha'))
    parser.set('CONFIG_PLANILHA', 'coluna_nome', cfg.get('coluna_nome'))
    parser.set('CONFIG_PLANILHA', 'coluna_telefone', cfg.get('coluna_telefone'))
    parser.set('CONFIG_PLANILHA', 'coluna_plano', cfg.get('coluna_plano'))
    parser.set('CONFIG_PLANILHA', 'coluna_datafim', cfg.get('coluna_datafim'))
    parser.set('CONFIG_PLANILHA', 'coluna_datainicio', cfg.get('coluna_datainicio'))
    with open('config.cfg', 'w') as file:
        parser.write(file)
    file.close()



def config_api():
    cfg = _get_config_api()
    if cfg != { }:
        return cfg
    api_id = input('Digite seu API_ID: ')
    api_hash = input('Digite seu API_HASH: ')
    _set_config_api({
        'api_id': api_id,
        'api_hash': api_hash })


def config_plan():
    cfg = _get_config_plan()
    if cfg != {}:
        return cfg
    key_sheets = input('Digite a chave da planilha: ')
    json_file = input('Digite o nome do arquivo json (secret): ')
    nome_planilha = input('Digite o nome da planilha: ')
    coluna_nome = input('Digite a letra da coluna "Nome": ')
    coluna_telefone = input('Digite a letra da coluna "Telefone": ')
    coluna_plano = input('Digite a letra da coluna "Plano": ')
    coluna_datainicio = input('Digite a letra da coluna "Data Inicio": ')
    coluna_datafim = input('Digite a letra da coluna "Data Fim": ')
    _set_config_plan({
        'key_sheets': key_sheets,
        'json_file': json_file,
        'nome_planilha': nome_planilha,
        'coluna_nome': coluna_nome,
        'coluna_telefone': coluna_telefone,
        'coluna_plano': coluna_plano,
        'coluna_datainicio': coluna_datainicio,
        'coluna_datafim': coluna_datafim})

