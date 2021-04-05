from fila import Fila
from pilha import Pilha 
from listaencadeada import Lista_Encadeada



#Teste da fila
print('Teste da fila')
f = Fila()
f.inserir(10)
f.inserir(20)
f.inserir(30)
print(f.retornar_lista())
f.remover()
print(f.retornar_lista())

# Teste da pilha
print('Teste da pilha')
p = Pilha()
p.inserir(10)
p.inserir(20)
p.inserir(30)
print(p.retornar_lista())
p.remover()
print(p.retornar_lista())

#Teste da lista encadada
print('Teste da lista encadada')
e = Lista_Encadeada()
e.inserir(0, 10)
e.inserir(0, 20)
e.inserir(1, 30)
print(e.retornar_lista())
e.remover(2)
print(e.retornar_lista())