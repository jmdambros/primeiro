import os
from funcoes import limpartela
while True:
    limpartela ()
    print ("(1) Abrir Calculadora")
    print ("(2) Desligar Computador")
    print ("(3) Abrir VSCODE")
    print ("(4) Abrir Google Chrome")
    opcao = input ()
    if opcao == "0":
        break
    elif opcao == "1":
        os.system("calc")
    elif opcao == "2":
        os.system("shutdown/a") 
    elif opcao == "3":
        os.system ("code ." )
    elif opcao == "4":
        os.system ("start chrome.exe")
    else:
        print ("opcao invalida")
    