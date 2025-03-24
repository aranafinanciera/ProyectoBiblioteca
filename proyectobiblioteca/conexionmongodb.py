#conexionmongodb.py
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
from PyQt6.QtWidgets import QMessageBox

def conectar_mongodb(parent=None):
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["biblioteca"]
        QMessageBox.information(parent, "Conexión Exitosa", "✅ Conexión a MongoDB exitosa.")
        return db
    except Exception as e:
        QMessageBox.critical(parent, "Error de BD", f"❌ No se pudo conectar a MongoDB:\n{e}")
        return None


"""
# Crear colecciones si no existen
colecciones = ["autores", "libros", "ejemplares", "usuarios", "prestamos"]
for coleccion in colecciones:
    if coleccion not in db.list_collection_names():
        db.create_collection(coleccion)

# Insertar un autor
autor_id = db.autores.insert_one({
    "codigo": "A001",
    "nombre": "Autor Ejemplo"
}).inserted_id

# Insertar un libro con referencia al autor
libro_id = db.libros.insert_one({
    "codigo": "L001",
    "titulo": "Libro de Ejemplo",
    "ISBN": "978-3-16-148410-0",
    "editorial": "Editorial Ejemplo",
    "paginas": 300,
    "autores": [autor_id]  # Relación con autores
}).inserted_id

# Insertar un ejemplar con referencia al libro
ejemplar_id = db.ejemplares.insert_one({
    "codigo": "E001",
    "localizacion": "Estantería A3",
    "libro": libro_id  # Relación con libro
}).inserted_id

# Insertar un usuario
usuario_id = db.usuarios.insert_one({
    "codigo": "U001",
    "nombre": "Usuario Ejemplo",
    "telefono": "123456789",
    "direccion": "Calle Falsa 123",
    "tipo": "usuario"  # Diferenciación para herencia
}).inserted_id

# Insertar un bibliotecario (subtipo de usuario)
bibliotecario_id = db.usuarios.insert_one({
    "codigo": "B001",
    "nombre": "Bibliotecario Ejemplo",
    "telefono": "987654321",
    "direccion": "Av. Biblioteca 456",
    "tipo": "bibliotecario",  # Indica que es un bibliotecario
    "permisos": ["gestionar_libros", "administrar_prestamos"]  # Atributo extra para bibliotecarios
}).inserted_id

# Insertar un préstamo relacionando usuario y ejemplar
db.prestamos.insert_one({
    "usuario": usuario_id,  # Relación con usuario
    "ejemplar": ejemplar_id,  # Relación con ejemplar
    "fecha_prestamo": datetime(2025, 3, 21),
    "fecha_devolucion": datetime(2025, 4, 21)
})

print("Base de datos creada") 
"""