emails_spam = "fulano@gmail.com,beltrano@gmail.com,ciclano@gmail.com"
email = str(input("Digite o seu email: "))
if email in emails_spam:
    print("O seu email faz parte dos emails do spam!")
else:
    print("O seu email não faz parte dos email do spam!")
