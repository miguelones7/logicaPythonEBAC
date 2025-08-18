#!/bin/bash

# Verifica se o Python 3 está instalado
if ! command -v python3 &> /dev/null
then
    echo "Python3 não encontrado, instalando..."
    sudo apt update && sudo apt install -y python3
fi

# Pergunta nome no Bash
read -p "Olá! Digite seu nome para continuar: " nome
echo "Boas-vindas, $nome! Vamos acessar a calculadora do Miguel em 3 segundos."

# Contagem regressiva
for i in 3 2 1
do
    echo "Acessando em $i..."
    sleep 1
done

# Executa o programa Python, usando o diretório onde o .sh está
python3 "$(dirname "$0")/Calculadora_EBAC.py"
