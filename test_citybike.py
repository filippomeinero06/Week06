import mysql.connector

def main():
    conn = mysql.connector.connect(option_files="db.cnf")

    query = """
            SELECT *
            FROM trip
            ORDER BY duration_seconds
            LIMIT 10
            """
            # LIMIT prende solo le prime 10 righe

    cursor = conn.cursor()
    cursor.execute(query)

    for trip in cursor:
        print(trip)
main()