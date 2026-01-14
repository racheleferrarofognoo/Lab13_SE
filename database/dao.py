from database.DB_connect import DBConnect
from model.gene import Gene
from model.interazione import Interazione


class DAO:

    @staticmethod
    def read_all_geni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
        select * from gene g
            where g.cromosoma > 0
        """

        cursor.execute(query)

        for row in cursor:
            gene = Gene(row["id"],
                                  row["funzione"],
                                  row["essenziale"],
                                  row["cromosoma"])
            result.append(gene)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_all_interazioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
            select * from interazione 
        """

        cursor.execute(query)

        for row in cursor:
            interazione = Interazione(row["id_gene1"],
                                      row["id_gene2"],
                                      row["tipo"],
                                      row["correlazione"])
            result.append(interazione)
        cursor.close()
        conn.close()
        return result