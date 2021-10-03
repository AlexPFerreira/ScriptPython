#  Parte 2:
#  1) Acesse o NX-API Sandbox do Switch.
#  2) Execute o comando "show version" 
#  3) Copie o código JSON da resposta e cole em um arquivo texto em seu computador.
#  4) Construa em seu computador um script python que leia o conteúdo deste arquivo e retorne um dicionário com o conteúdo do arquivo.

import json # Importação do Json

with open("D:\OneDrive\Scripts\ScriptPython\scriptParaVericaçãoECriação\showVersion.txt") as json_arquivo: # Caminho do arquivo
    dados = json.load(json_arquivo) # Converter o arquivo Jsom em dicionario 

print ("#"*40) 
print ("### Conversão Aquivo Json para Dicionário ###")
print ("#"*40) 
print(type(dados)) # Verificação do tipo da variável
print ("#\n" + "#\n" + "#") 
print (dados) # Imprimir o dicionário (o arquivo Json convertido)
print (" #\n","#\n","#")
print ("#"*40) 
