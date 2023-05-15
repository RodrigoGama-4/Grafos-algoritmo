from math import inf

class Grafo:
    n = 0
    matriz = None

    def __init__(self, n):
        self.n = n
        self.lista = [None]*n
        for i in range(self.n):
            self.lista[i] = []
    
    def __str__(self):
        graph = ' '
        for i in range(self.n):
            graph += ' v'+str(i)+' -> '
            for j in range(len(self.lista[i])):
                graph += str(self.lista[i][j])+ ' '
            graph += '\n'
        return graph
    
    def criar_aresta(self, vi, vj):
        self.lista[vi].append(vj)
        self.lista[vj].append(vi)
    
    def visita(self, g, u, tempo, vertices):
        tempo += 1
        print('vertice', u, '- tempo:', tempo)
        vertices[u]['dist'] = tempo
        vertices[u]['cor'] = 'cinza'

        for v in g.lista[u]:
            if vertices[v]['cor'] == 'branco':
                vertices[v]['pai'] = u
                tempo = self.visita(g, v, tempo, vertices)
        vertices[u]['cor'] = 'preto'
        return tempo


    def busca_profundidade(self):
        vertices = {}
        for i in range(self.n):
            vertices[i] = {'label': i, 'cor':'branco', 'dist':inf, 'pai':None}
        
        tempo = 0

        for u in range(self.n):
            if vertices[u]['cor'] == 'branco':
                tempo = self.visita(self, u, tempo, vertices)

# Exemplo de uso
g = Grafo(5)
g.criar_aresta(0, 1)
g.criar_aresta(0, 2)
g.criar_aresta(1, 3)
g.criar_aresta(2, 4)
print(g)

g.busca_profundidade()