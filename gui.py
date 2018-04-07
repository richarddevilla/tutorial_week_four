import sys
import web_scraping
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QTableWidget,QTableWidgetItem
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Web Browser'
        self.left = 120
        self.top = 120
        self.width = 1200
        self.height = 700
        self.init_win()

    def init_win(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
        self.button1 = QPushButton('Show Webpage', self)
        self.button1.move(450, 10)
        self.button1.clicked.connect(self.show_webpage)
        self.button1.show()
        self.button2 = QPushButton('Extract <li>', self)
        self.button2.move(550, 10)
        self.button2.clicked.connect(self.show_list)
        self.button2.show()


    def show_webpage(self):
        self.webpage = web_scraping.get_html()
        self.web = QWebEngineView(self)
        self.web.load(QUrl('file:///C:/Users/Chase/PycharmProjects/tutorial_week_four/my_html.html'))
        self.web.move(40, 40)
        self.web.show()

    def show_list(self):
        self.webpage = web_scraping.get_html()
        self.html_list = web_scraping.get_list(self.webpage)
        self.table = QTableWidget(self)
        self.table_row = len(self.html_list)
        self.table.setRowCount(self.table_row)
        self.table.setColumnCount(1)
        i=0
        for each in self.html_list:
            self.table.setItem(i, 0, QTableWidgetItem(each))
            i+=1
        self.table.move(900,40)
        self.table.resizeColumnsToContents()
        self.table.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = App()
    sys.exit(app.exec_())
