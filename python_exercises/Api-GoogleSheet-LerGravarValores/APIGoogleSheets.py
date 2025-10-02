import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SAMPLE_SPREADSHEET_ID = "1oH0TzxN6OCKYcuLtBfnpuHzl415y7fwYjqjV82m727w"
SAMPLE_RANGE_NAME = "Página1!A1:C14"

def main():

  creds = None
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
        if os.path.exists(r'C:\Users\Davil\OneDrive\Documentos\Education\Ensino - Hard Skills\HashtagProgramação\Python\PythonImpressionador\modulo33-integracaoPythonApisJson\aula12-apiGoogleSheets-PythonComGoogleSheets\credentials.json'):
            flow = InstalledAppFlow.from_client_secrets_file(
                r'C:\Users\Davil\OneDrive\Documentos\Education\Ensino - Hard Skills\HashtagProgramação\Python\PythonImpressionador\modulo33-integracaoPythonApisJson\aula12-apiGoogleSheets-PythonComGoogleSheets\credentials.json', scopes=SCOPES
            )
            creds = flow.run_local_server(port=0)
    with open("token.json", "w") as token:
        token.write(creds.to_json())

  try:

    service = build("sheets", "v4", credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()

    valores = result['values']
    print(valores)

    valores_adicionar = [
      ['Imposto'],
    ]
    
    for i, linha in enumerate(valores):
      if i > 0:
        vendas = linha[1]
        vendas = vendas.replace("R$ ", "").replace(".", "").replace(",", ".").strip()
        try:
          vendas = float(vendas)
          imposto = vendas * 0.1
          valores_adicionar.append([imposto])
        except ValueError:
          print(f"Erro ao converter {vendas} para float")

    result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="C1", valueInputOption="USER_ENTERED", body={'values': valores_adicionar}).execute()

    # valores_adicionar = [
    #   ['dezembro', 'R$150.500,45'],
    #   ['janeiro', 'R$125.700,50'],
    # ]

    # result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='A13',valueInputOption='USER_ENTERED', body={'values': valores_adicionar}).execute()
    # print(f"{result.get('updatedCells')} células atualizadas")

  except HttpError as err:
    print(err)

if __name__ == "__main__":
  main()