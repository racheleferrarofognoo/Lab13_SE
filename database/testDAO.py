from database.dao import DAO
from model import model
dao =DAO()
model = model.Model()
print(dao.read_all_cromosomi())
print(dao.read_connessioni())

model.build_grafo()
print(model.dettagli())
print(model.conta_archi(3))
print(model.min_max())