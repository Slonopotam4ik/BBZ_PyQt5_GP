from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        if event.buttons() & QtCore.Qt.LeftButton:
            print(event.globalPos().x(), event.globalPos().y())

if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(500, 150, 100, 100)
    window.show()
    sys.exit(app.exec_())