import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFormLayout, QVBoxLayout, QFrame
)
from PyQt6.QtGui import QFont, QColor, QPalette
from PyQt6.QtCore import Qt

class BibliotecaApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestión de Biblioteca")
        self.setGeometry(100, 100, 400, 350)

        # Aplicar paleta de colores minimalista
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#f4f4f4"))
        self.setPalette(palette)

        layout = QVBoxLayout()

        # Estilo de los campos
        self.setStyleSheet("""
            QLabel {
                font-size: 12pt;
                color: #333;
            }
            QLineEdit {
                font-size: 11pt;
                padding: 6px;
                border: 1px solid #bbb;
                border-radius: 5px;
                background-color: white;
            }
            QPushButton {
                font-size: 12pt;
                background-color: #007BFF;
                color: white;
                padding: 8px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)

        form_layout = QFormLayout()

        # Sección de datos del estudiante
        self.no_control = QLineEdit()
        self.no_control.setPlaceholderText("Ej. 18660390")
        form_layout.addRow("No. Control:", self.no_control)

        self.nombre = QLineEdit()
        self.nombre.setPlaceholderText("Ej. Juan Pérez")
        form_layout.addRow("Nombre:", self.nombre)

        self.carrera = QLineEdit()
        self.carrera.setPlaceholderText("Ej. ISC")
        form_layout.addRow("Carrera:", self.carrera)

        # Línea divisora
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        layout.addWidget(line)

        # Sección de datos del libro
        self.codigo = QLineEdit()
        self.codigo.setPlaceholderText("Código del libro")
        form_layout.addRow("Código:", self.codigo)

        self.titulo = QLineEdit()
        self.titulo.setPlaceholderText("Título del libro")
        form_layout.addRow("Título:", self.titulo)

        self.autor = QLineEdit()
        self.autor.setPlaceholderText("Autor del libro")
        form_layout.addRow("Autor:", self.autor)

        # Fechas
        self.fecha_solicitud = QLineEdit()
        self.fecha_solicitud.setPlaceholderText("DD/MM/AAAA")
        form_layout.addRow("Fecha Solicitud:", self.fecha_solicitud)

        self.fecha_devolucion = QLineEdit()
        self.fecha_devolucion.setPlaceholderText("DD/MM/AAAA")
        form_layout.addRow("Fecha Devolución:", self.fecha_devolucion)

        layout.addLayout(form_layout)

        # Botón para registrar préstamo
        self.boton_registrar = QPushButton("Registrar Préstamo")
        layout.addWidget(self.boton_registrar, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = BibliotecaApp()
    ventana.show()
    sys.exit(app.exec())