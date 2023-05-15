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
                graph += str(self.lista[i][j])
            graph += '\n'
        return graph

    def criar_aresta(self, vi, vj):
        self.lista[vi].append(vj)
        self.lista[vj].append(vi)
    
    def remover_aresta(self, vi, vj):
        self.lista[vi].remove(vj)
        self.lista[vj].remove(vi)
    
    def existe_aresta(self, vi, vj):
        return (vi in self.list[vj])
    
    def grauaresta(self, vi):
        return len(self.lista[vi])

    def grauGrafo(self):
        grau = 0
        for n in range(self.n):
            grau += self.grauaresta(n)
        return grau

    def temLoop(self):
        for i in range(self.n):
            for j in range(len(self.lista[i])):
                if self.lista[i][j] == i:
                    return True
        return False        

    def temArestaParalela(self):
        for i in range(self.n):
            for j in range(len(self.lista[i])):
                if self.lista[i][j].count(self.lista[i][j]) >1:
                    return True
        return False   
