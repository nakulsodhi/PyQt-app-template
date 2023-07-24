from PyQt6.QtWidgets import *
from pathlib import Path
import PyQt6.QtCore as core
from PyQt6.QtGui import QAction, QTextOption, QIcon, QGuiApplication, QPixmap
import sys
import csv
import re
import business_logic


"""
Style Guide:
    Function Names = snake_case
    Variable Names = camelCase
    Class Name = CapitalizeEachWord
    Tabs = 4 spaces
    Wrap Code blocks in ####
    Function Docstring with Description, Parameters, Return
"""



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
        self.setWindowTitle("PyQt6 Samples")
####################################
          

########################### Top Menu Bar  
        menu = self.menuBar()
        fileMenu = menu.addMenu('&File')
        editMenu = menu.addMenu('&Edit')
        helpMenu = menu.addMenu('&Help')
####################################


####################### Statusbar
        statusbar = self.statusBar()
        statusbar.showMessage("Ready")
####################################


######################## Central Widget
        w = TabWidget(self) # passing the argument self here so that the widget class can access Window class properties such as menubar menus
        self.setCentralWidget(w)
####################################


#################################### CLASS Window END


class TabWidget(QWidget):
    """
    Widget Containing the tabs
    """
    def __init__(self,mainWindow):
        super(TabWidget, self).__init__()

####################### Init Properties
        """
        Some variables need to be properties of the class so they can be easily accessed by functions different from the scope
        Python does not make properties private. To "Hide" certain properties from outside the Class, consider naming them with an __ at the start. Eg __resourceCount is hidden.
        """
        self.clickyButtonTab1 = None
        self.userSpooked = False

####################################
    

#################################### Assign main window to instance 
        self.mainWindow = mainWindow
        #mainWindow.statusBar().showMessage("This is working")
####################################


############################## Initialize Tabs
        self.tabs = QTabWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        self.setLayout(layout)
####################################


############################### Tab 1 (Display Markdown and HTML Text)
        tab1 = QWidget()
        layoutTab1 = QVBoxLayout()
        clickyButton = QPushButton("This is a tab with a \"Vertical\" Layout")
        clickyButton.clicked.connect(self.clicky_button_func)
        layoutTab1.addWidget(clickyButton)
        self.clickyButtonTab1 = clickyButton
        tab1TextBox1 = self.create_text_object()
        tab1TextBox1.setMarkdown(business_logic.sample_md_text())
        tab1TextBox2 = self.create_text_object()
        tab1TextBox2.setHtml(business_logic.sample_html_text())
        layoutTab1.addWidget(tab1TextBox1)
        layoutTab1.addWidget(tab1TextBox2)
        tab1.setLayout(layoutTab1)
        self.tabs.addTab(tab1, "Vertical")
####################################


################################ Tab 2 
        tab2 = QWidget()
        layoutTab2 = QHBoxLayout()
####################################


#################################### Functions for TabWidget
    def clicky_button_func(self):
        text = business_logic.testing_func()
        self.mainWindow.statusBar().showMessage(text)
        if not self.userSpooked:
            self.clickyButtonTab1.setText("This is a tab with a \"Vertical\" Layout (Look at the status)")
            self.mainWindow.setWindowTitle("Look Behind You")
            self.userSpooked = True
        else:
            self.clickyButtonTab1.setText("This is a tab with a \"Vertical\" Layout")
            self.mainWindow.setWindowTitle("PyQt6 Samples")
            self.userSpooked = False
        return text


    def create_text_object(self):
        textBox = QTextEdit()
        textBox.setReadOnly(True)
        textBox.setWordWrapMode(QTextOption.WrapMode.WordWrap)
        return textBox
####################################


#################################### CLASS TabWidget END




if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
