from PyQt6.QtWidgets import *
import PyQt6.QtCore as core
from PyQt6.QtGui import QAction, QTextOption, QIcon, QGuiApplication, QPixmap
import sys
from pathlib import Path
import business_logic
from functools import  partial


"""
Style Guide:
    Function Names = snake_case
    Variable Names = camelCase
    Class Name = CapitalizeEachWord
    Tabs = 4 spaces
    Wrap Code blocks in ####
    Function Docstring with Description, Parameters, Return
"""




############################Constants
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 600
BUTTON_HEIGHT = 80
BUTTON_WIDTH = 80
ERROR_MSG = "ERROR"
HOME_DIR = str(Path.home())
####################################


class Window(QMainWindow):
    """
    Main Window of the application
    """
    def __init__(self):
        super(Window,self).__init__()
######################### Resolution
        windowHeight = int(QGuiApplication.primaryScreen().availableSize().height() * 0.5)
        windowWidth = int(QGuiApplication.primaryScreen().availableSize().width() * 0.5)
        #update screen height and width constants
        WINDOW_WIDTH = windowWidth
        WINDOW_HEIGHT = windowHeight
        self.resize(windowWidth, windowHeight)
        self.setWindowTitle("PyQt6 Samples")
####################################
          

########################### Top Menu Bar  
        menu = self.menuBar()
        #linking the following menus to self so they are easier to access by other widget classes
        self.fileMenu = menu.addMenu('&File')
        self.editMenu = menu.addMenu('&Edit')
        self.utilities = menu.addMenu('&Utilities')
        self.helpMenu = menu.addMenu('&Help')
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
    Widget containing the tabs
    """
    def __init__(self,mainWindow):
        super(TabWidget, self).__init__()

#################################### Assign main window to instance 
        self.mainWindow = mainWindow
        #mainWindow.statusBar().showMessage("This is working")
#################################### END Assign main window

####################### Init Properties
        """
        Some variables need to be properties of the class so they can be easily accessed by functions different from the scope
        Python does not make properties private. To "Hide" certain properties from outside the Class, consider naming them with an __ at the start. Eg __resourceCount is hidden.
        """
        self.__clickyButtonTab1 = None
        self.__userSpooked = False
        self.counter = 0
        self.counterText = QLabel(f"Counter: {self.counter}")
        self.calc = None
####################################
    

############################## Statusbar Elements (Permanent)
        """
Permanent widgets are added on the right side of the statusbar. 
        """
        self.mainWindow.statusBar().addPermanentWidget(self.counterText)
####################################



############################## Initialize Tabs
        self.tabs = QTabWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        self.setLayout(layout)
#################################### END Initialize Tabs


############################### Tab 1 (Display Markdown and HTML Text in vertically aligned text boxes)
        tab1 = QWidget()
        layoutTab1 = QVBoxLayout()
        clickyButton = QPushButton("This is a tab with a \"Vertical\" Layout")
        clickyButton.clicked.connect(self.clicky_button_func)
        clickyButton.clicked.connect(self.increment_counter)
        layoutTab1.addWidget(clickyButton)
        self.__clickyButtonTab1 = clickyButton
        tab1TextBox1 = self.create_text_object()
        tab1TextBox1.setMarkdown(business_logic.sample_md_text())
        tab1TextBox2 = self.create_text_object()
        tab1TextBox2.setHtml(business_logic.sample_html_text())
        layoutTab1.addWidget(tab1TextBox1)
        layoutTab1.addWidget(tab1TextBox2)
        tab1.setLayout(layoutTab1)
        self.tabs.addTab(tab1, "Vertical")
#################################### END Tab 1 


################################ Tab 2  (Display Markdown and HTML Text in horizontally aligned text boxes)
        tab2 = QWidget()
        layoutTab2 = QHBoxLayout()
        #i did not add the  tab1 text boxes here instead of making my own because those text boxes are assigned to tab1. if I had used them here instead of creating new ones, they would have disconnected from tab 1
        #Moreover .copy() didnt work.
        tab2TextBox1 = self.create_text_object()
        tab2TextBox1.setMarkdown(business_logic.sample_md_text())
        tab2TextBox2 = self.create_text_object()
        tab2TextBox2.setHtml(business_logic.sample_html_text())
        layoutTab2.addWidget(tab2TextBox1)
        layoutTab2.addWidget(tab2TextBox2)
        tab2.setLayout(layoutTab2)
        self.tabs.addTab(tab2, "Horizontal")
################################### END Tab 2 Horizontal Layout


############################# Calculator Launcher
        tab3 = QWidget()
        # We will use a nested layout
        layoutTab3 = QVBoxLayout()
        buttonLaunchCalc = QPushButton("Click to launche calculator")
        buttonLaunchCalc.clicked.connect(self.launch_calc)
        #textTab3 = QLabel("Click to launch Calculator", alignment=core.Qt.AlignmentFlag.AlignCenter)
        #layoutTab3.addWidget(textTab3)
        layoutTab3.addWidget(buttonLaunchCalc)
      
        
        tab3.setLayout(layoutTab3)
        self.tabs.addTab(tab3, "Calculator")
#################################### END Tab 3 Calculator Launcher


############################ Tab 4 (Notepad Clone)
        tab4 = QWidget()
        layoutTab4 = QVBoxLayout()
        self.textEditor = self.create_text_object()
        self.textEditor.setReadOnly(False)
        layoutTab4.addWidget(self.textEditor)
        tab4.setLayout(layoutTab4) 
        self.tabs.addTab(tab4, "Text Editor")
        #self.open_file_in_editor()
        openFileAction = QAction("&Open File",self)
        openFileAction.triggered.connect(self.open_file_in_editor)
        self.mainWindow.fileMenu.addAction(openFileAction)
        saveFileAction = QAction("&Save Changes", self)
        saveFileAction.triggered.connect(self.save_file)
        self.mainWindow.fileMenu.addAction(saveFileAction)
        restoreAction = QAction("&Open Last File", self)
        restoreAction.triggered.connect(self.restore_notepad_session)
        self.mainWindow.editMenu.addAction(restoreAction)
#################################### END Tab 4


#################################### Functions for TabWidget
    def clicky_button_func(self):
        """
           Description: Handles the behavior of the button on Tab 1 
           Parameters: self
           Return: String from business_logic.testing_func() 
           """   
        text = business_logic.testing_func()
        self.mainWindow.statusBar().showMessage(text)
        if not self.__userSpooked:
            self.__clickyButtonTab1.setText("This is a tab with a \"Vertical\" Layout (Look at the status)")
            self.mainWindow.setWindowTitle("Look Behind You")
            self.__userSpooked = True
        else:
            self.__clickyButtonTab1.setText("This is a tab with a \"Vertical\" Layout")
            self.mainWindow.setWindowTitle("PyQt6 Samples")
            self.__userSpooked = False
        return text

    def create_text_object(self):
        """
           Description: Create a read only text object
           Parameters: self
           Return:  QTextEdit Object with word wrap and read only properties
           """   
        textBox = QTextEdit()
        textBox.setReadOnly(True)
        textBox.setWordWrapMode(QTextOption.WrapMode.WordWrap)
        return textBox

    def increment_counter(self):
        """
        Description: increment the variable __counter and update the widget
        Parameters: self
        Return: None
        """
        self.counter += 1
        self.counterText.setText(f"Counter: {self.counter}")
        if self.counter >= 15:
            self.counterText.setText("You can stop now")
        if self.counter >= 30:
            self.counterText.setText("OKAY STOP. PLEASE")
        #self.mainWindow.statusBar().reformat()
        self.update_permanent_widget(self.counterText)

    def launch_calc(self):
        """
           Description: Create a calculator widget if it does not exist and show it
           Parameters: self
           Return: none 
           """   
        if not self.calc:
           self.calc = CalculatorWidget()
        self.calc.show()

    def update_permanent_widget(self, widget):
        """
        Description: Takes a widget that is permanent in the statusbar and updates it.
        Parameters: self, widget: QWidget
        Return: None  

        Suggestion: If dealing with multiple permanent widgets, put them in a list and order them in the order you want them to appear left and right. Then, whenever any of the widgets need to be updated. call the method for each element in the list. I am not doing so in this template as I only have 1 permanent widget
        """ 
        self.mainWindow.statusBar().removeWidget(widget)
        self.mainWindow.statusBar().addPermanentWidget(widget)
        widget.show()
        #self.mainWindow.statusBar().reformat()



    def open_file_in_editor(self, filename=None):
        """
           Description: Let the user select a file and open it in the text editor
           Parameters: self
           Return: none 
           """
        # You can make a property, function etc private
        # by adding two underscores before the name
        if not filename:
            self.__currentlyOpenFilePath = self.get_file_name()
            self.mainWindow.statusBar().showMessage(f"File {filename} opened ")
        else:
            self.__currentlyOpenFilePath = filename
        with open(self.__currentlyOpenFilePath) as file:
            self.textEditor.setText(file.read())
        self.tabs.setCurrentIndex(3)
        business_logic.append_file_history(self.__currentlyOpenFilePath)

    def get_file_name(self):
        """
           Description: Prompts the user with a file dialog to select a file to open
           Parameters: self 
           Return: Path to the file that was selected 
           """ 
        fname = QFileDialog.getOpenFileName(self, "Open File", HOME_DIR, filter="*.txt")
        return fname[0]
         
    def save_file(self):
        """
           Description: Save the file being currently edited.
           Parameters: self
           Return: none 
           """   
        with open(self.__currentlyOpenFilePath, 'w') as f:
            f.write(self.textEditor.toPlainText())
            business_logic.append_file_history(self.__currentlyOpenFilePath)
        self.mainWindow.statusBar().showMessage(f"File { business_logic.return_filename(self.__currentlyOpenFilePath) } Saved")

    def restore_notepad_session(self):
        """
        Description: Opens the text file that was edited last
        Parameters: self
        Return: None 
        """
        (filename, path, dateModified) = business_logic.get_last_file()
        self.open_file_in_editor(path)
        self.mainWindow.statusBar().showMessage(f"File {filename} opened   Last Modified {dateModified} ")
        
        
####################################


#################################### CLASS TabWidget END


class CalculatorWidget(QWidget):
    """docstring for CalculatorWidget."""
    def __init__(self):
        super(CalculatorWidget, self).__init__()


########################## Creating the Main Layout and Display
        layoutMain = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setFixedHeight(BUTTON_HEIGHT)
        layoutMain.addWidget(self.display)


####################################
        layoutButtons = QGridLayout()
        buttons = {}
        keyboard = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
        ["0", "00", ".", "+", "="],
        ]

        for row,keys in enumerate(keyboard):
            for col, key in enumerate(keys):
                buttons[key] = QPushButton(key)
                # Setting the size of buttons to 80px * 80px
                buttons[key].setFixedSize(BUTTON_WIDTH, BUTTON_HEIGHT)
                layoutButtons.addWidget(buttons[key], row, col) 
        # Nested Layout Example
        layoutMain.addLayout(layoutButtons) 
        self.setLayout(layoutMain)
        self.setFixedSize(BUTTON_WIDTH * 5 + 20, BUTTON_HEIGHT * 5 + 20)
        # 5 times as wide and high as the buttons + a 20px Padding
        self.connect_buttons(buttons)
####################################
        


    def connect_buttons(self, buttons):
        """
        Connect the calculator button objects to their corresponding functions
        """
        for key, buttonObj in buttons.items():
            if key not in ["=","C"]:
                buttonObj.clicked.connect(
                        # To connect a function to a button while passing it an argument
                        partial( self.button_press, key)
                        )
            if key == "C":
                buttonObj.clicked.connect(self.clear_text)
            if key == "=":
                buttonObj.clicked.connect(self.evaluate)

    def button_press(self, buttonLabel):
        """
        Append display with the button that was pushed
        """
        if self.display.text() == ERROR_MSG:
            self.clear_text()
        self.set_display_text(f"{self.display.text()}{buttonLabel}")  
    
    def clear_text(self):
        """
        Clear the text display
        """
        self.display.setText("")

    def set_display_text(self, text):
        """
        Description: Set calculator display to the passed argument text
        Parameters: self, text (to set the display to)
        Return: None
        """
        self.display.setText(text)
        self.display.setFocus()


    def evaluate(self):
        """
        evaluate the displayed expression
        """
        output = business_logic.eval_expression( self.display.text() ) 
        self.set_display_text(str(output))


        




if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()

    sys.exit(app.exec())
