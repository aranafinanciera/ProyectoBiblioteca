#windowbiblioteca.py
from PyQt6.QtWidgets import QApplication, QMainWindow
from conexionredis import conectar_redis
from conexionmongodb import conectar_mongodb
from PyQt6.QtCore import Qt
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox

class biblioteca(QMainWindow):
    def __init__(self):
        super(biblioteca, self).__init__()
        loadUi("biblioteca.ui", self)

        # Intentar conexión a Redis
        self.redis = None
        self.mongodb = None
        self.cmb.addItems(["redis", "mongodb"])   
        self.cmb.currentIndexChanged.connect(self.conectar_base_datos)
        self.btnbuscar.clicked.connect(self.buscar_usuario)


    def buscar_usuario(self):
        # Determina el sistema seleccionado en el QComboBox
        seleccion = self.cmb.currentText()

        if seleccion == "redis":
            self.buscar_datos_redis()
        elif seleccion == "mongodb":
            self.buscar_datos_mongodb()
        else:
            QMessageBox.warning(self, "Tipo no válido", "⚠️ Seleccione una opción válida para la conexión.")

    def buscar_datos_mongodb(self):
        """
        Obtiene el número de control desde la interfaz,
        busca en la colección 'usuarios' de MongoDB la información
        del usuario y rellena los campos de la UI si existe.
        """
        # Verifica si hay conexión a MongoDB
        if self.mongodb is None:
            QMessageBox.warning(self, "Sin conexión", "⚠️ No hay conexión a MongoDB.")
            return

        # Obtener el número de control del QPlainTextEdit
        nocontrol_value = self.nocontrol.toPlainText().strip()

        if not nocontrol_value:
            QMessageBox.warning(self, "Campo vacío", "⚠️ Ingresa un número de control.")
            return

        try:
            # Buscar el usuario en la colección 'usuarios'
            usuario_data = self.mongodb.usuarios.find_one({"no_control": nocontrol_value})

            if not usuario_data:
                QMessageBox.information(
                    self, 
                    "Usuario no encontrado", 
                    f"No se encontró el usuario con número de control {nocontrol_value}."
                )
                return

            # Rellenar los campos de la interfaz con los valores obtenidos.
            # Se asume que el documento tiene los campos: nombre, carrera, tipo y telefono.
            self.nombre.setPlainText(usuario_data.get("nombre", ""))
            self.carrera.setPlainText(usuario_data.get("direccion", ""))
            self.tipo.setPlainText(usuario_data.get("tipo", ""))
            self.telefono.setPlainText(usuario_data.get("telefono", ""))

            # Limpiar otros campos (ej: titulo, autor) según tu lógica
            self.titulo.setPlainText("")
            self.autor.setPlainText("")

            QMessageBox.information(self, "Búsqueda exitosa", "Usuario encontrado y campos rellenados.")
            
        except Exception as e:
            QMessageBox.critical(self, "Error de consulta", f"❌ Error al buscar en MongoDB:\n{e}")    

    
    def conectar_base_datos(self):
        seleccion = self.cmb.currentText()

        if seleccion == "redis":
            self.redis = conectar_redis(self)
            


        elif seleccion == "mongodb":
            self.mongodb = conectar_mongodb(self)

        else:
            QMessageBox.warning(self, "Tipo no válido", "⚠️ Seleccione una opción válida.")

    def buscar_datos_redis(self):
        """
        Obtiene el número de control de la interfaz,
        busca en Redis la información del usuario
        y llena los campos si existe.
        """
        # 1. Verificar que tenemos conexión a Redis
        if not self.redis:
            QMessageBox.warning(self, "Sin conexión", "⚠️ No hay conexión a Redis.")
            return

        # 2. Obtener el número de control del QPlainTextEdit
        nocontrol_value = self.nocontrol.toPlainText().strip()

        # 3. Validar que no esté vacío
        if not nocontrol_value:
            QMessageBox.warning(self, "Campo vacío", "⚠️ Ingresa un número de control.")
            return

        # 4. Buscar la información en Redis
        #    Supongamos que guardaste al usuario en 'usuario:<nocontrol>'
        user_key = f"usuario:{nocontrol_value}"
        user_data = self.redis.hgetall(user_key)

        # 5. Validar si existe la clave en Redis
        if not user_data:
            QMessageBox.information(self, "Usuario no encontrado", f"No se encontró el usuario con número de control {nocontrol_value}.")
            return

        # 6. Rellenar los campos de la interfaz con los valores obtenidos
        #    Asegúrate de que en Redis existan campos como "nombre", "carrera", "tipo", "telefono"
        self.nombre.setPlainText(user_data.get("nombre", ""))
        self.carrera.setPlainText(user_data.get("carrera", ""))
        self.tipo.setPlainText(user_data.get("tipo", ""))
        self.telefono.setPlainText(user_data.get("telefono", ""))

        # Puedes dejar los demás campos (titulo, autor, etc.) en blanco
        # o según tu lógica de negocio
        self.titulo.setPlainText("")
        self.autor.setPlainText("")

        # 7. Mensaje opcional de éxito
        QMessageBox.information(self, "Búsqueda exitosa", "Usuario encontrado y campos rellenados.")



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = biblioteca()
    window.show()
    sys.exit(app.exec())
