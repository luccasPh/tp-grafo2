from cavaleiros.home import Home
from PyQt5 import QtWidgets, QtCore, QtGui

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Home()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())