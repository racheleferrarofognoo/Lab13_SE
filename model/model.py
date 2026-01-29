import networkx as nx

from database.dao import DAO


class Model:
    def __init__(self):
        self.G = nx.DiGraph()
        self.dao = DAO()
        self.id_map = {}
        self.nodi = []

    def build_grafo(self):
        self.G.clear()
        cromosomi = self.dao.read_all_cromosomi()
        for cromosoma in cromosomi:
            self.G.add_node(cromosoma)

        edges = {}
        archi = self.dao.read_connessioni()

        for a in archi:
            # Aggiungiamo l'arco orientato con l'attributo 'weight'
            self.G.add_edge(a[0], a[1], weight=float(a[2]))


    def dettagli(self):
        return self.G.number_of_nodes(), self.G.number_of_edges()

    def min_max(self):
        peso_max = -100000
        peso_min = float('inf')
        for u,v,p in self.G.edges(data=True):
            peso = p['weight']
            if peso > peso_max:
                peso_max = peso
            if peso < peso_min:
                peso_min = peso
        return peso_max, peso_min

    def conta_archi(self, soglia):

        num_archi_minori = 0
        num_archi_maggiori = 0
        for u,v,p in self.G.edges(data=True):
            peso = p['weight']
            if peso > soglia:
                num_archi_maggiori += 1
            elif peso < soglia:
                num_archi_minori += 1
        return num_archi_minori, num_archi_maggiori



