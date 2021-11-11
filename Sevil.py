import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.setWindowIcon(QtGui.QIcon('Sevil/Images/Shellic.png'))
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)
        navbar.setStyleSheet("background: #ffffff");

        back_button = QAction('Back', self)
        back_button.triggered.connect(self.browser.back)
        back_button.setIcon(QIcon('Sevil/Images/back.png'))
        navbar.addAction(back_button)
        
        forward_button = QAction('Forword', self)
        forward_button.triggered.connect(self.browser.forward)
        forward_button.setIcon(QIcon('Sevil/Images/forward.png'))
        navbar.addAction(forward_button)

        reload_button = QAction('Reload', self)
        reload_button.triggered.connect(self.browser.reload)
        reload_button.setIcon(QIcon('Sevil/Images/reload.gif'))
        navbar.addAction(reload_button)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_vell)
        navbar.addWidget(self.url_bar)

        home_button = QAction('Home', self)
        home_button.triggered.connect(self.navigate_home)
        home_button.setIcon(QIcon('Sevil/Images/Shellic.png'))
        navbar.addAction(home_button)

        self.browser.urlChanged.connect(self.update_url)
        

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))


    def navigate_to_vell(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))


    def update_url(self, v):
        self.url_bar.setText(v.toString()) 


app = QApplication(sys.argv)
QApplication.setApplicationName('Sevil Alpha 2')
window = MainWindow()

app.exec_()