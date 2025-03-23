import datetime

def feliz_natal():
    ano_atual = datetime.date.today().year
    dia_do_natal = datetime.date(ano_atual, 12, 25)

    hoje = datetime.date.today()
    if hoje == dia_do_natal:
        return hoje.strftime('%d/%m/%Y') + ' - FELIZ NATAL!'
    else:
        return hoje.strftime('%d/%m/%Y') + ' -  Ainda não é natal!'

print(feliz_natal())