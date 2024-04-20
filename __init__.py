import sys
from qgis.utils import iface
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QFileDialog, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QTextEdit, QDialog, QAction

class MyApplication:
    def __init__(self, app=None, iface=None):
        self.iface = iface
        if iface:
            print(iface)
            self.listC = QComboBox()
            self.editText = QTextEdit()
        else:
            self.app = app  # The QApplication instance is passed into the class constructor
            self.listC = QComboBox()
            self.editText = QTextEdit()

    def button_clickedI(self):
        fileName = QFileDialog.getSaveFileName(None, "File to be created", ".", "Shapefiles (*.shp)")
        if fileName:
            dlg = QMessageBox()
            dlg.setWindowTitle("Result File")
            dlg.setText("Path and file: " + fileName[0])
            self.editText.setText(fileName[0])
            if dlg.exec() == QMessageBox.Ok:
                print("OK!")

    def button_clickedII(self):
        dlg = QMessageBox()
        dlg.setWindowTitle("I have a question!")
        dlg.setText("This is a simple dialog: " + self.listC.currentText())
        if dlg.exec() == QMessageBox.Ok:
            print("OK!")

    def newwindow(self):
        widget = QDialog(iface.mainWindow()) if iface else QDialog()

        layoutI = QHBoxLayout()
        textLabel = QLabel("Cities:")
        listOfCities = ["Coimbra", "Porto", "Lisboa"]
        listOfCities.sort()
        self.listC.addItems(listOfCities)
        layoutI.addWidget(textLabel)
        layoutI.addWidget(self.listC)

        layoutII = QHBoxLayout()
        textLabel = QLabel("Result File:")
        button = QPushButton("...")
        button.clicked.connect(self.button_clickedI)
        layoutII.addWidget(textLabel)
        layoutII.addWidget(button)

        layoutO = QVBoxLayout()
        layoutO.addLayout(layoutI)
        layoutO.addLayout(layoutII)
        self.editText.setPlainText("please select a file")
        layoutO.addWidget(self.editText)

        button = QPushButton("Compute")
        button.clicked.connect(self.button_clickedII)
        layoutO.addWidget(button)

        widget.setGeometry(50, 50, 200, 200)
        widget.setWindowTitle("PyQt5 Example")
        widget.setLayout(layoutO)
        widget.show()
        if iface:
            print(iface)
        else:
            sys.exit(self.app.exec_())

    def initGui(self):
        self.action = QAction('| Go - Plugin |', self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        del self.action

    def run(self):
        self.newwindow()

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create QApplication here
    my_app = MyApplication(app)
    my_app.newwindow()


def classFactory(iface):
    return MyApplication(None, iface)