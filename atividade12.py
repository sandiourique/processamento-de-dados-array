# Patricia, Sandi, Sandro

from operator import itemgetter
import numpy as np

print("Questao")
print("Qual o id do vendedor que fez o maior valor total em vendas")
#array para armazenar varias notas de varios alunos, possui 2 dimensoes
arr = np.array([[1, 1, 150], [1, 2, 200], [1, 3, 78], [1, 2,50], [2, 1, 150], [2, 2, 200], [2, 3, 78], [2, 2,50]])

#ORDENA O A LISTA PELO INDEX POSIÇÃO 0
arr = sorted(arr, key = itemgetter(0))
#zera variáveis
vendAnterior = 0
vendedor = 0
maiorvalor = float = 0
valor = float = 0
vendedores = []
#percorre lista
for linha in arr:
  #VERIFICA SE LINHA ESTA CARREGADA E SE COD VENDEDOR É IGUAL AO ANTERIOR, SE FOR DIFERENTE FAZ A QUEBRA NO COD VENDEDOR
  if linha[0] != vendAnterior:
    #VERIFICA SE O VALOR É MAIOR Q O MAIOR VALOR PARA GUARDAR O VALOR MAIOR
    if valor >= maiorvalor:
      maiorvalor = valor
      vendedor = vendAnterior
      valor = float = 0
    #RECUPERA O VALOR ANTERIOR E SOMARIZA O VALOR
    vendAnterior = (linha[0])
    valor += (linha[2])
  #SOMARIZA O VALOR REFERENTE AO COD CLIENTE    
  else :
    valor += (linha[2])
    vendedores.append([vendAnterior, np.max(valor)])
    # vendedores.append([linha[0], valor])


for v in vendedores:
      if v[1] == np.max(vendedores):
            print('O vendedor {} com maior total de vendas - R${:.2f}'.format(v[0], v[1]))



print("----------------------------------------------------------------")
   
print('Qual o cliente que fez o maior numero de compras? ')
print("")
#ORDENA O A LISTA PELO INDEX POSIÇÃO 0
arr = sorted(arr, key = itemgetter(1))
clienteAnterior = 0
cliente = 0
qt= int = 0
contador = int = 0
lista = []

for linha in arr:
  if linha[1] != clienteAnterior:
    if contador > qt:
      qt = contador
      cliente = clienteAnterior
      contador = int = 0
    clienteAnterior = (linha[1])
    contador += 1  
  else :
    contador += 1
    lista.append([clienteAnterior, np.max(contador)])

for c in lista:
      if c[1] == np.max(lista):
            print('O cliente {} comprou {} vezes.'.format(c[0], c[1]))






