import os
from funcoes import limpartela,aguardar
while True:
    limpartela ()
    print ("(1)Adicionar Aluno")
    print ("(2) Mostrar Lista")
    opcao = input ()
    if opcao == "0":
        break
    elif opcao == "1":
        nome= input ("Nome:")
        email = input ("Email:")
        arquivo = open("bd.atitus","a") #SEMPRE UTILIZAR "A" (APPEND) PARA BANCO DE DADOS (ADICONAR DADOS)
        arquivo.write (nome + " " + email + "\n")
        arquivo.close()
        print ("dados do aluno salvos")
        aguardar ()
    elif opcao == "2":
        try:
            arquivo = open("bd.atitus")
            dados = arquivo.read()
            print (dados)
            arquivo.close ()
            aguardar () 
        except:
            print ("Sem banco de dados")
            arquivo = open("bd.atitus","w") 
            arquivo.close()
            print ("Banco de dados criado")
    else:
        print ("opcao invalida")
    