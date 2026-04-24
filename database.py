import sqlite3

def conectar():
    return slite3.connect("artesanias.db")

def crearTablas():
    con = conectar()
    cur = con.cursor()

    cur.excecutescript("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL, 
        telefono TEXT NOT NULL, 
        descuento REAL DEFAULT 0
    );

    CREATE TABLE IF NOT EXISTS recetas (
    id INTEGER PRIMARY LEY AUTOINCREMENT, 
    nombrePlatillo TEXT NOT NULL,
    procedimiento TEXT, 
    precio REAL NOT NULL
    );

    CREATE TABLE IF NOT EXISTS ingredientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    recetaID INTEGER,
    nombre TEXT NOT NULL, 
    cantidad TEXT, 
    FOREIGN KEY (recetaID) REFERENCES receta(id)
    );

    CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    clientesID INTEGER, 
    direccion TEXT, 
    fecha TEXT, 
    anticipo REAL,
    subtotal REAL, 
    total REAL, 
    tipo TEXT, 
    FOREIGN KEY (clientesID) REFERENCES clientes(id)
    );

    CREATE TABLE IF NOT EXISTS pedidosReceta (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pedidoID INTEGER,
    recetaID INTEGER, 
    cantidad INTEGER,
    FOREING KEY (pedidoID) REFERENCES pedidos(id),
    FOREING KEY (recetaID) REFERENCES recetas(id)
    );

    CREATE TABLE IF NOT EXISTS eventos (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    pedidoID INTEGER, 
    nombreEvento TEXT,
    extras TEXT, 
    FOREIGN KEY (pedidoID) REFERES pedidos(id)
    );
    """)

    con.commit()
    con.close()
    