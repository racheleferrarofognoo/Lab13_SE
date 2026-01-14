import networkx as nx

from database.dao import DAO


class Model:
    def __init__(self):
        self.Grafo = nx.MultiDiGraph()
        self.dizionario_geni ={}
        self.lista_geni = DAO.read_all_geni()
        for gene in self.lista_geni:
            self.dizionario_geni[gene.id] = gene

    def creaGrafo(self):
        lista_interazioni = DAO.read_all_interazioni()
        print(self.dizionario_geni)
        print(len(lista_interazioni))

        val_edges = {} # key: (g1,g2) val: float - correlazione
        for interazione in lista_interazioni:
            if interazione.id_gene1 not in self.dizionario_geni.keys() or interazione.id_gene2 not in self.dizionario_geni.keys():
                continue
            g1 = self.dizionario_geni[interazione.id_gene1]
            g2 = self.dizionario_geni[interazione.id_gene2]
            if (g1.cromosoma, g2.cromosoma) not in val_edges.keys():
                val_edges[(g1.cromosoma, g2.cromosoma)] = interazione.correlazione
            else:
                val_edges[(g1.cromosoma, g2.cromosoma)] += interazione.correlazione

        for interazione in lista_interazioni:
            if interazione.id_gene1 not in self.dizionario_geni.keys() or interazione.id_gene2 not in self.dizionario_geni.keys():
                continue
            g1 = self.dizionario_geni[interazione.id_gene1]
            g2 = self.dizionario_geni[interazione.id_gene2]
            if g1.cromosoma != g2.cromosoma:
                if not self.Grafo.has_edge(g1.cromosoma, g2.cromosoma):
                    self.Grafo.add_edge(g1.cromosoma, g2.cromosoma, weight = val_edges[g1.cromosoma,g2.cromosoma])
                #else:

                   # self.Grafo[g1.cromosoma][g2.cromosoma]["peso"] += interazione.correlazione

    def cerca_numero_archi(self):
        return len(self.Grafo.edges())

    def cerca_numero_nodi(self):
        return self.Grafo.number_of_nodes()

    def massimo_minimo_peso (self):
        massimo = 0.0
        minimo = float('inf')
        for u,v, weight in self.Grafo.edges(data='weight'):
            if weight > massimo:
                massimo = weight
            if weight < minimo:
                minimo = weight
        return minimo, massimo


