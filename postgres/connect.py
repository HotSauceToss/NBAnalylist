import psycopg2

def connect(dbName, user, password):
    return psycopg2.connect("dbname=" + dbName + " user=" + user + " password=" + password)
    