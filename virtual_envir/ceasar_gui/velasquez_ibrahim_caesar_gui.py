import sys
from pathlib import Path
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QLineEdit, QSpinBox, QPlainTextEdit, QGridLayout, QToolBar



class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.setWindowTitle("Caesar Cipher")
        self.setFixedSize(700,600)
        # Text Widget
        self.textEdit = QPlainTextEdit("Hello", self)
        #Buttons Widget
        self.buttonEncrypt = QPushButton("Encrypt", parent=self)
        self.buttonEncrypt.setFixedSize(60, 40)
        self.buttonEncrypt.clicked.connect(self.onButtonClicked)
        self.buttonDecrypt = QPushButton("Decrypt", parent=self)
        self.buttonDecrypt.setFixedSize(60, 40)
        #Spin Box Widget
        self.spinBox = QSpinBox(parent=self)
        self.spinBox.setMinimum(-26)
        self.spinBox.setMaximum(26)
        self.spinBox.valueChanged.connect(self.spinBoxValueChanged)
        #Labels Widget
        self.label = QLabel("Rotations:", parent=self)
        self.valueLabel = QLabel("0", parent=self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.label.setStyleSheet("background-color: green") #Color of the label
        
        #Layout
        layout = QGridLayout()
        hBox = QHBoxLayout()
        hBox.addWidget(self.buttonEncrypt)
        hBox.addWidget(self.buttonDecrypt)
        hBox.addWidget(self.label)
        hBox.addWidget(self.spinBox)
        hBox.addWidget(self.valueLabel)
        
        
        layout.addWidget(self.textEdit, 0, 0)
        layout.addLayout(hBox, 1, 0)
        # layout.addWidget(self.label2)
        
        # Actions
        self.actionFileOpen = QAction("&Open", parent=self)
        self.actionFileOpen.setShortcut(QKeySequence("Ctrl+O"))
        self.actionFileOpen.triggered.connect(self.onFileOpenClicked)
        
        self.actionFileSaveAs = QAction("Save &As...", parent=self)
        self.actionFileSaveAs.setShortcut(QKeySequence("Ctrl+Shift+s"))
        self.actionFileSaveAs.triggered.connect(self.onFileSaveAsClicked)
        
        self.actionFileExit = QAction("E&xit", parent=self)
        self.actionFileExit.triggered.connect(self.onFileExitClicked)
        
        #Menu bar
        self.menu = self.menuBar()
        self.menuFile = self.menu.addMenu("&File")
        self.menuFile.addAction(self.actionFileOpen)
        self.menuFile.addAction(self.actionFileSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionFileExit)
        
        
        
        centralWidget = QWidget(parent=self)
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
    
    def UIBuild(self):
        """Create the UI for the main window."""
        
        # Menu

    
    def onButtonClicked(self):
        self.label.setText("You clicked me")
        
    def onFileOpenClicked(self):
        self.valueLabel.setText("You clicked File Open.")
        
    def onFileExitClicked(self):
        QApplication.exit()
    
    def onFileSaveAsClicked(self):
        QApplication.exit()
        
    def spinBoxValueChanged(self):
        self.valueLabel.setText(str(self.spinBox.value()))
        


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()

    window.show()

    sys.exit(app.exec()) # S