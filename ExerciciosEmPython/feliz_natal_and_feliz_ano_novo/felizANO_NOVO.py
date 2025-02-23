import datetime

def feliz_ano_novo():
    ano_atual = datetime.date.today().year
    # Considerando que o ano novo é sempre no dia 1° de Janeiro do ano atual
    data_ano_novo = datetime.date(ano_atual, 1, 1)

    hoje = datetime.date.today()
    if hoje == data_ano_novo:
        return hoje.strftime('%d/%m/%Y') + ' - FELIZ ANO NOVO!'
    else:
        return hoje.strftime('%d/%m/%Y') + ' - Ainda não é ano novo!'

print(feliz_ano_novo())