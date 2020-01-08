import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setGeometry(100, 100, 1400, 600)
        self.con = sqlite3.connect('coffee')
        self.cur = self.con.cursor()
        self.tableWidget.setColumnCount(7)
        names = [i[0] for i in self.con.execute(
            '''SELECT * FROM sorts''').description]
        self.tableWidget.setHorizontalHeaderLabels(names)
        data = self.cur.execute('''SELECT * FROM sorts''').fetchall()
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()


app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
