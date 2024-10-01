import sqlite3

# Connessione al database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Esegui una query per selezionare tutti i dati dalla tabella
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Stampa i risultati
if rows:
    for row in rows:
        print(row)
else:
    print("Nessun dato trovato nel database.")

# Chiudi la connessione
conn.close()

# Attendi che l'utente prema Enter prima di chiudere
input("Premi Enter per chiudere...")
