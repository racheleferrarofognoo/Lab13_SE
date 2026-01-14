import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """""
        self._model.creaGrafo()

        self._view.lista_visualizzazione_1.controls.clear()
        num_archi = self._model.cerca_numero_archi()
        num_nodi = self._model.cerca_numero_nodi()
        peso_minimo, peso_massimo = self._model.massimo_minimo_peso()
        self._view.lista_visualizzazione_1.controls.append(
            ft.Text(f"Numero di vertici: {num_nodi} e numero di archi: {num_archi}"))
        self._view.lista_visualizzazione_1.controls.append(
            ft.Text(f"Informazioni sui pesi degli archi- Peso minimo: {peso_minimo}, peso massimo: {peso_massimo}"))
        self._view.page.update()

    def handle_conta_edges(self, e):
        """ Handler per gestire il conteggio degli archi """""



    def handle_ricerca(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """""
        # TODO