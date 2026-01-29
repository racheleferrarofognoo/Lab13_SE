
from database.DB_connect import DBConnect

class DAO:

    @staticmethod
    def read_all_cromosomi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct cromosoma 
                    from gene
                    where cromosoma <> 0 """

        cursor.execute(query)

        for row in cursor:
            result.append(row['cromosoma'])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_connessioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ WITH GeniUnivoci AS (
                        SELECT DISTINCT id, cromosoma
                        FROM gene
                        WHERE cromosoma > 0
                    )
                    SELECT g1.cromosoma AS c1, g2.cromosoma AS c2, SUM(i.correlazione) AS peso
                    FROM interazione i
                    JOIN GeniUnivoci g1 ON i.id_gene1 = g1.id
                    JOIN GeniUnivoci g2 ON i.id_gene2 = g2.id
                    WHERE g1.cromosoma <> g2.cromosoma
                    GROUP BY g1.cromosoma, g2.cromosoma"""

        cursor.execute(query)

        for row in cursor:
            result.append((row['c1'], row['c2'], float(row['peso'])))

        cursor.close()
        conn.close()
        return result