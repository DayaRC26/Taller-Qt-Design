import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QWidget
from PyQt5 import uic
from PyQt5.uic import loadUi

import recursos_rc

class VentanaExito(QDialog):
    def __init__(self, mensaje, ventana_principal):
        QDialog.__init__(self)
        uic.loadUi(r'Ventana Productor Agregado.ui', self)

        self.ventana_principal = ventana_principal
        self.mensaje_exito.setText(mensaje)
        self.buttonBoxExito.accepted.connect(self.aceptar)
        self.buttonBoxExito.rejected.connect(self.cancelar)

    def aceptar(self):
        self.ventana_principal.limpiar_campos_propietario()
        self.ventana_principal.limpiar_campos_finca()
        self.accept()

    def cancelar(self):
        self.reject()


class VentanaError(QDialog):
    def __init__(self, mensaje, ventana_principal):
        QDialog.__init__(self)
        uic.loadUi(r'Ventana Error Productor.ui', self)

        self.ventana_principal = ventana_principal
        self.mensaje_error.setText(mensaje)
        self.buttonBoxError.accepted.connect(self.aceptar)
        self.buttonBoxError.rejected.connect(self.cancelar)

    def aceptar(self):
        self.ventana_principal.limpiar_campos_propietario()
        self.ventana_principal.limpiar_campos_finca()
        self.accept()

    def cancelar(self):
        self.reject()

    def cambiar_texto(self, mensaje):
        self.mensaje_exito.setText(mensaje)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('Taller - Interfaz Grafica P4.ui', self)
        self.bt_agregar_propietario.clicked.connect(self.pop_out_validacion_productor)
        self.bt_agregar_finca.clicked.connect(self.pop_out_validacion_finca)

    def obtener_informacion_productor(self):
        dni = self.box_text_dni.text().strip()
        nombre = self.box_text_name.text().strip()
        tel = self.box_text_tel.text().strip()
        apellido = self.box_text_nickname.text().strip()
        correo = self.box_text_mail.text().strip()

        return dni, nombre, tel, apellido, correo

    def obtener_informacion_finca(self):
        cultivo = self.comboBox_cultivo.currentText().strip()
        registro_castral = self.box_text_reg_castral.text().strip()
        municipio = self.box_text_municipio.text().strip()

        return cultivo, registro_castral, municipio
    
    def pop_out_validacion_productor(self):
        dni, nombre, tel, apellido, correo = self.obtener_informacion_productor()

        if not dni or not nombre or not tel or not apellido or not correo:
            self.ventana_error = VentanaError("Error al ingresar productor", self)
            self.ventana_error.show()
        else:
            self.ventana_exito = VentanaExito("¡Productor Agregado!", self)
            self.ventana_exito.show()

    def pop_out_validacion_finca(self):
        cultivo, registro_castral, municipio = self.obtener_informacion_finca()

        if not cultivo or not registro_castral or not municipio :
            self.ventana_error = VentanaError("Error al ingresar la Finca", self)
            self.ventana_error.show()
        else:
            self.ventana_exito = VentanaExito("¡Finca Agregada!", self)
            self.ventana_exito.show()

    def limpiar_campos_propietario(self):
        self.box_text_dni.clear()
        self.box_text_name.clear()
        self.box_text_tel.clear()
        self.box_text_nickname.clear()
        self.box_text_mail.clear()

    def limpiar_campos_finca(self):
        self.comboBox_cultivo.setCurrentIndex(0)
        self.box_text_reg_castral.clear()
        self.box_text_municipio.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = VentanaPrincipal()
    mi_app.show()
    sys.exit(app.exec_())



        



