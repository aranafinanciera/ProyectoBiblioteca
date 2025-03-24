from pymongo import MongoClient
from datetime import datetime
import random

# Conectar a MongoDB (Windows)
client = MongoClient("mongodb://localhost:27017/")
db = client["biblioteca"]

def generar_no_control():
    return f"2266{random.randint(1000, 9999)}"

def agregar_alumno(nombre, telefono, direccion):
    alumno = {
        "no_control": generar_no_control(),
        "nombre": nombre,
        "telefono": telefono,
        "direccion": direccion,
        "tipo": "alumno"
    }
    
    # Insertar en MongoDB
    alumno_id = db.usuarios.insert_one(alumno).inserted_id
    
    print(f"Alumno agregado con No. de Control {alumno['no_control']}")

agregar_alumno("Juan Pérez	","612345678	","Calle del Sol 12, Madrid")
agregar_alumno("María López	","698765432	","Calle Real 8, Sevilla")
agregar_alumno("Ana Martínez	","612398745","Plaza Mayor 3, Valencia")
agregar_alumno("Luis Gómez	","699123456","Paseo de la Reforma 27, Bilbao")
agregar_alumno("Carmen Rodríguez","688554433	","Calle Nueva 15, Zaragoza")
agregar_alumno("Carlos Ramírez", "5551234567", "Av. Reforma 101")
agregar_alumno("Ana Torres", "5557654321", "Calle Morelos 202")
agregar_alumno("Luis Gómez", "5559876543", "Blvd. Insurgentes 303")
agregar_alumno("Sofía Herrera", "5556789012", "Calle Juárez 404")
agregar_alumno("Ricardo Méndez", "5552345678", "Avenida Hidalgo 505")
