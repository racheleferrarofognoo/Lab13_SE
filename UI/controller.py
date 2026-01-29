import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """""
        self._view.lista_visualizzazione_1.controls.clear()
        self._model.build_grafo()
        num_nodi, num_archi = self._model.dettagli()
        max, min = self._model.min_max()
        self._view.lista_visualizzazione_1.controls.append(
            ft.Text(f'Numero di vertici: {num_nodi} Numero di archi: {num_archi}'))
        self._view.lista_visualizzazione_1.controls.append(
            ft.Text(f'Informazioni sui pesi degli archi - valore minimo: {min} e valore massimo: {max}'))

        self._view.update()

    def handle_conta_edges(self, e):
        """ Handler per gestire il conteggio degli archi """""
        self._view.lista_visualizzazione_2.controls.clear()
        soglia = int(self._view.txt_name.value)
        minori, maggiori = self._model.conta_archi(soglia)
        self._view.lista_visualizzazione_2.controls.append(
            ft.Text(f'Numero di archi con peso maggiore della soglia: {maggiori} \n'
                    f'Numero di archi con peso minore della soglia: {minori}'))


        self._view.update()

def handle_ricerca(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """""
        # TODO
