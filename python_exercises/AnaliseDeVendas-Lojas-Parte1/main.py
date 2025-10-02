import pandas as pd
tabela_vendas = pd.read_excel('baseDeDados-VendasLojas.xlsx')
pd.set_option("display.max_columns", None)
print(tabela_vendas)

faturamento = tabela_vendas[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
print(faturamento)

quantidade = tabela_vendas[["ID Loja", "Quantidade"]].groupby("ID Loja").sum()
print(quantidade)

print("-" * 50)
ticket_medio = (faturamento["Valor Final"] / quantidade["Quantidade"]).to_frame()
ticket_medio = ticket_medio.rename(columns={0: "Ticket Médio"})
print(ticket_medio)

import win32com.client as win32

outlook = win32.Dispatch("outlook.application")
mail = outlook.CreateItem(0)
mail.to = "limad9786@gmail.com"
mail.Subject = "Relatório de Vendas por Loja - Morada Nova - CE"
mail.HTMLBody = f"""

      <p>BOM DIA</p>
      <p>Prezados, segue em anexo o relatório de vendas das lojas de Morada Nova - CE</p>

      <p>FATURAMENTO</p>
      {faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}
      <p>QUANTIDADE</p>
      {quantidade.to_html()}
      <p>TICKET MÉDIO DOS PRODUTOS: </p>
      {ticket_medio.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}

      <p>QUALQUER DÚVIDA É SÓ RESPONDER A ESSE EMAIL :)</p>
      <p>ATENCIOSAMENTE,</p>
      <p>DAVI OLIVEIRA - SOFTWARE ENGINNER</p>

"""

mail.Send()
print("EMAIL ENVIADO!!!")
