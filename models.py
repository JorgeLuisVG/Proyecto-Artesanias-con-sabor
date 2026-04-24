from database import conectar

def insertarCliente(nombre, direccion, telefono, descuento):
    con = conectar()
    cur = con.cursor()

    cur.execute("""
    INSERT INTO clientes (nombre, direccion, telefono, descuento)
    VALUES (?, ?, ?, ?)
    """, (nombre, direccion, telefono, descuento))

    con.commit()
    con.close()

def obtenerClientes():
    con = conectar()
    cur = con.cursor()

    cur.execute("SELECT * FROM clientes")
    datos = cur.fetchall()

    con.close()
    return datos

def insertarReceta(nombre, procedimiento, precio):
    con = conectar()
    cur = con.cursor()

    cur.execute("""
    INSERT INTO recetas (nombre, procedimiento, precio)
    VALUES (?, ?, ?)
    """, (nombre, procedimiento, precio))

    con.commit()
    con.close()

def insertarIngrediente(recetaID, nombre, cantidad):
    con = conectar()
    cur = con.cursor()

    cur.execute("""
    INSERT INTO ingredientes (recetaID, nombre, cantidad)
    VALUES (?, ?, ?)
    """, (recetaID, nombre, cantidad))

    con.commit()
    con.close()

def obtenerRecetas():
    con = conectar()
    cur = con.cursor()

    cur.execute("SELECT * FROM recetas")
    datos = cur.fetchall()

    con.close()
    return datos 

def insertarPedido(clienteID, direccion, fecha, anticipo, subtotal, total, tipo):
    con = conectar()
    cur = con.cursor()

    cur.execute("""
    INSERT INTO pedidos (clienteID, direccion, fecha, anticipo, subtotal, total, tipo)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (clienteID, direccion, fecha, anticipo, subtotal, total, tipo))

    pedidoID = cur.lastrowid

    con.commit()
    con.close()

    return pedidoID 


def insertarPedidoReceta(pedidoID, recetaID, cantidad):
    con = conectar()
    cur = con.cursor()

    cur.execute("""
    INSERT INTO pedidoReceta (pedidoID, recetaID, cantidad)
    VALUES (?, ?, ?)
    """, (pedidoID, recetaID, cantidad))

    con.commit()
    con.close()

def insertarEvento(pedidoID, nombreEvento, extras):
    con = conectar()
    cur = con.cursor()

    cur.execute("""
    INSERT INTO eventos (pedidoID, nombreEvento, extras)
    VALUES (?, ?, ?)
    """, (pedidoID, nombreEvento, extras))

    con.commit()
    con.close()