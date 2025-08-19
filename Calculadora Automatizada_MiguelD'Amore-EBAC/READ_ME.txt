---------------------------Miguel D'Amore----------------------------------


Olá! Você está acessando meu primeiro projeto do curso profissionalizante 
da EBAC para Analista de Dados


Montei um projeto em Python permitindo ao usuário fazerdiversos tipos de 
cálculo em um sistema com interface simples gerenciados por meio de menus. 

É possível fazer cálculos de Adição, Subtração,Multiplicação, Exponenciação 
e Média Simples até o momento.



O sistema conta com uma automação que garante que o usuário tenha o Python3
instalado/atualizado para garantir o funcionamento do arquivo.py.


>> Para executar o arquivo de automação "autoCalculadora.sh" <<

Primeiramente, tenha acesso ao terminal Linux

-- caso você utilize o sistema operacional Windows, assim
como eu, você pode utilizar o Subsistema do Windows para
Linux (WSL):

• Abrir Windows PowerShell 
		no modo administrador (Botão direito) 
• Listar as distribuições: 
		wsl --list --online 
• Instalar distribuição: 
		wsl --install --distribution <nome_distribuição>
			recomendado: última versão disponível Ubuntu


Salve o arquivo "CalculadoraEBAC.py" e o arquivo "autoCalculadora.sh"
em uma mesma pasta (evite espaços no nome) e acesse o terminal Linux. 
Você precisará ter o caminho dessa pasta. Você pode verificar no Explorador 
de Arquivos ou utilizar o comando abaixo no terminal Linux:
	
	find / -name "autoCalculadora.sh" 2>/dev/null

--aguarde até ele encontrar, o que pode demorar alguns segundos
	selecione o caminho completo e utilize o comando 'cd' caminho -
	exemplo:
		cd /mnt/c/Users/seu_usuário/Desktop/Nome_da_Pasta (no meu caso a pasta está salva na Área de Trabalho)

Com o repositório correto acessado, utilize o comando
	. autoCalculadora.sh

Siga as instruções e utilize minha calculadora python!




