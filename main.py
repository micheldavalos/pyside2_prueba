from PySide2.QtWidgets import QPushButton, QApplication
import sys

# Aplicación de Qt
app = QApplication()
# Se crea un botón con la palabra Hola
button = QPushButton('Hola')
# Se hace visible el botón
button.show()
# Qt loop
sys.exit(app.exec_())