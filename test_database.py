import mysql.connector
from mysql.connector import errorcode


def main():
    try:
        # Stabilisco la connessione con il DB
        conn = mysql.connector.connect(user='root',
                                      password='',
                                      host='localhost',
                                      port=3306,
                                      database='products_suppliers')

        print("Connected to database")

        # Mi faccio dare dalla connessione un cursore
        my_cursor = conn.cursor() # Creo il cursore
        cursore_dizionario = conn.cursor(dictionary=True)

        # Scrivo la query
        #query = ("SELECT * FROM S")

        # Come creare una query parametrica / parametrizzata
        citta = input("Per quale città estrarre i fornitori: ")

        #query = f"""SELECT `S#`, `STATUS`
        #           FROM S
        #           WHERE CITY = '{citta}' """

        query = f"""SELECT `S#`, `STATUS`
                    FROM S
                    WHERE CITY = '%s' """




        # La eseguo attraverso il cursore
        #my_cursor.execute(query) # Eseguo la query
        cursore_dizionario.execute(query, (citta,))

        # Il cursore è un container di Python, quindi posso iterare su di esso (for, while, ...)
        """
        # Estrae le righe come tuple
        for riga in my_cursor:
            print(riga)
        """

        """
        # Estrare le righe come dizionari con come chiavi i nomi delle colonne
        """
        for riga in cursore_dizionario:
            print(riga)




    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ERROR: Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("ERROR: Database does not exist")
        else:
            print(err)
    else:
        conn.close()



main()