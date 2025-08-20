from posixpath import basename
# --- Calculadora --- #

import os
import time

# -- Função para simular um programa com diferentes menus (arquivo.py) -- #
def limparTela():
  os.system("cls" if os.name == 'nt' else 'clear') #garante que funcione em Windows e Linux


# -- Função de adição -- #
def adicao():
  limparTela()
  resultado = 0
  
  print("\nAdição\n")
  print("Digite um número (ou 0 para parar)")

  while True: #permite ao usuário digitar números até digitar 0, para encerrar
    try: 
      numero = float(input("\n- "))
      if numero == 0:
        break
      
      print(f"{resultado} + {numero} = {resultado + numero}")
      resultado += numero

    except ValueError:
      print("Inválido. Digite um número inteiro ou casas decimais após ponto[.]")
      time.sleep(2)
      continue
    
  print(f"\nResultado final da soma = {resultado}")
  input("\n\nPressione ENTER para voltar ao menu...")
  menu()
  

# -- Função de Subtração -- #
def subtracao():
  limparTela()
  
  print("\nSubtração\n")
  print("Digite um número (ou 0 para parar)")

  resultado = None #sem valor inicial

  while True: #permite ao usuário digitar números até digitar 0, para encerrar
    try: 
      numero = float(input("\n- "))
      if numero == 0:
        break
      
      if resultado is None:
        resultado = numero
      #após alterar o valor do resultado, fazemos ele menos o próximo input    
      else:
        if numero < 0:
          print(f"{resultado} - ({numero}) = {resultado - numero}")
        else:
          print(f"{resultado} - {numero} = {resultado - numero}")
                
        # Atualiza o resultado
        resultado -= numero

    except ValueError:
        print("Inválido. Digite um número inteiro ou casas decimais após ponto[.]")
        time.sleep(2)
        continue
    
  print(f"\nResultado final da subtração = {resultado}")
  input("\n\nPressione ENTER para voltar ao menu...")
  menu()


# -- Função de Multiplicação -- #
def multiplicacao():
  limparTela()
  resultado = 1

  print("\nMultiplicação\n")
  print("Digite um número (ou 0 para parar)")

  while True: #permite ao usuário digitar números até digitar 0, para encerrar
    try: 
      numero = float(input("\n- "))
      if numero == 0:
        break
      
      print(f"{resultado} * {numero} = {resultado * numero}")
      resultado *= numero

    except ValueError:
      print("Inválido. Digite um número inteiro ou casas decimais após ponto[.]")
      time.sleep(2)
      continue
    
  print(f"\nResultado final da multiplicação = {resultado}")
  input("\n\nPressione ENTER para voltar ao menu...")
  menu()


# -- Função de Exponenciação -- #
def exponenciacao():
  limparTela()
  expoente = 1

  print("\nExponenciação\nTodo número elevado à 0 é igual a 1.\n\n")
  print("Digite um número (ou 0 para parar)")

  while True: #permite ao usuário digitar números até digitar 0, para encerrar
    try: 
      base = float(input("\nDigite a base: "))
      if base == 0:
        break
      expoente = float(input("Digite o expoente: "))
      
      print(f"{base} ^ {expoente} = {base ** expoente}")
      resultado = base ** expoente

    except ValueError:
      print("Inválido. Digite um número inteiro ou casas decimais após ponto[.]")
      time.sleep(2)
      continue
    
  print(f"\nResultado final da multiplicação = {resultado}")
  input("\n\nPressione ENTER para voltar ao menu...")
  menu()


# -- Função de Média Simples -- #
def mediaSimples():
  limparTela()
  
  print("\nMédia Simples\n")

  while True: #permite ao usuário digitar quantos números farão parte da média; 0 ou 1 para encerrar
    try:
      lista = []
      numero = int(input("\nDigite a quantidade de números (0 ou 1 para parar): "))
      
    except ValueError:
      print("Inválido. Digite um número inteiro ou casas decimais após ponto[.]")
      time.sleep(2)
      continue

    if numero == 0 or numero == 1:
        break
     
    else:
      for i in range(numero):
        num = float(input("Digite um número: "))
        lista.append(num)
      
      print(f"Média = {sum(lista) / numero}")


  input("\n\nPressione ENTER para voltar ao menu...")
  menu()


# -- Função Menu - gerencia todo o algoritmo -- #
def menu():
  limparTela()
  while True:
    try:
      menuOpcao = int(input("Qual operação deseja realizar?\n\n"
                                "1 - Adição\n"
                                "2 - Subtração\n"
                                "3 - Multiplicação\n"
                                "4 - Exponenciação\n"
                                "5 - Cálculo de Média Simples\n"
                                "0 - Sair"
                                "\n Opção: "))
    except ValueError:
      (print("\nOpção inválida. Digite uma das opções do menu"))
      time.sleep(3)
      continue
      
    if menuOpcao == 1:
      adicao()
      break
      
    elif menuOpcao == 2:
      subtracao()
      break

    elif menuOpcao == 3:
      multiplicacao()
      break

    elif menuOpcao == 4:
      exponenciacao()
      break

    elif menuOpcao == 5:
      mediaSimples()
      break
      
    #opção Sair e encerrar o programa após 3s
    elif menuOpcao == 0:
      limparTela()
      print("Obrigado por usar a Calculadora do Miguel! Até a próxima!\n\n")
            
      for i in range(3, 0, -1):
        print(f"Saindo em {i}...")
        time.sleep(1)
      exit()

    else:
      print("\nOpção inválida! Digite uma das opções do menu")
      time.sleep(2)


# -- Algoritmo -- #
menu()
