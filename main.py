from PyQt6.QtWidgets import *
from pathlib import Path
import PyQt6.QtCore as core
from PyQt6.QtGui import QAction, QTextOption, QIcon, QGuiApplication, QPixmap
import sys
import csv
import re

class Window(QMainWindow):
    """
    Main Window of the application
    """
    def __init__(self):
        super(Window,self).__init__()
######################### Resolution
        windowHeight = int(QGuiApplication.primaryScreen().availableSize().height() * 0.5)
        windowWidth = int(QGuiApplication.primaryScreen().availableSize().width() * 0.5)
        self.resize(windowWidth, windowHeight)
####################################
          

########################### Top Menu Bar  
        menu = self.menuBar()
        fileMenu = menu.addMenu('&File')
        editMenu = menu.addMenu('&Edit')
        helpMenu = menu.addMenu('&Help')
####################################


######################## Central Widget
        w = TabWidget(self) # passing the argument self here so that the widget class can access Window class properties such as menubar menus
        self.setCentralWidget(w)
####################################


class TabWidget(QWidget):
    """
    Widget Containing the tabs
    """
    def __init__(self,mainWindow):
        super(TabWidget, self).__init__()





if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
