import random
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCore
from ui import Ui_MainWindow

QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.Ceil)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.doinger)
        self.ui.first.clicked.connect(self.first)
        self.ui.generator.clicked.connect(self.generator)

    def first(self):
        f = open('bonus.txt', 'x')
        f.close()

    def generator(self):
        min = int(self.ui.min.toPlainText())
        max = int(self.ui.max.toPlainText())
        array = list(range(min,max+1))
        strarr = [str(x) for x in array]
        sth = "\n".join(strarr)
        with open('bonus.txt',"w") as f:
            f.write(sth)
    
    def doinger(self):
        percival = int(self.ui.inputer.toPlainText())
        with open('bonus.txt') as doing:
            doinging = doing.read().split('\n')
        samples = random.sample(doinging, percival)
        self.ui.outputer.setText(";".join(samples))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())