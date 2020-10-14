from PySide2.QtWidgets import QMainWindow
from ui_MainWindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        self.__ui.pushButton.clicked.connect(self.click_agregar)

    def click_agregar(self):
        self.__ui.pushButton.setText("Guardado")