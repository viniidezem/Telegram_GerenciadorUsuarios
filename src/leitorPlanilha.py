from src.funcoesSimples import *
from datetime import date, datetime

import gspread
from src.config import config_plan


def leitorPlanilha(opcao):
    cfg_plan = config_plan()
    print(cfg_plan)
    # Parametros Planilha
    gc = gspread.service_account(filename=('ArquivosConfiguracao/' + cfg_plan.get('json_file')))
    sh = gc.open_by_key(cfg_plan.get('key_sheets'))
    worksheet = sh.worksheet(cfg_plan.get('nome_planilha'))
    colunaNome = cfg_plan.get('coluna_nome');
    colunaTelefone = cfg_plan.get('coluna_telefone')
    colunaPlano = cfg_plan.get('coluna_plano')
    colunaDtaFim = cfg_plan.get('coluna_datafim')
    colunaDtaInicio = cfg_plan.get('coluna_datainicio')

    lista = []

    val = 'a'
    linha = '1'
    today = date.today().strftime("%Y-%m-%d")

    while val is not None:

        linha = int(linha) + 1

        cellNome = colunaNome + str(linha)
        cellTelefone = colunaTelefone + str(linha)
        cellDtaFim = colunaDtaFim + str(linha)
        cellPlano = colunaPlano + str(linha)
        cellDtaInicio = colunaDtaInicio + str(linha)

        nome = worksheet.acell(cellNome).value
        if nome is None:
            break
        telefone = worksheet.acell(cellTelefone).value
        DtaFim = date.strftime(datetime.strptime(worksheet.acell(cellDtaFim).value, '%d/%m/%Y'), "%Y-%m-%d")
        DtaInicio = date.strftime(datetime.strptime(worksheet.acell(cellDtaInicio).value, '%d/%m/%Y'), "%Y-%m-%d")
        plano = worksheet.acell(cellPlano).value

        if opcao == '1':  # RETORNA OS VENCIDOS
            if DtaFim == today:
                lista.append([nome, telefone, DtaFim, plano])

        if opcao == '2':  # RETORNA OS QUE IRÃO VENCER
            if days_between(today, DtaFim) == 1:
                lista.append([nome, telefone, DtaFim, plano])

        if opcao == '3':  # RETORNA OS QUE SERÃO ADICIONADOS HOJE
            if DtaInicio == today:
                lista.append([nome, telefone, DtaInicio, plano])

    return lista
