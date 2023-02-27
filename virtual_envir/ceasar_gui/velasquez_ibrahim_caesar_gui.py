import sys
from pathlib import Path
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QKeySequence
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout, 
                            QFileDialog, QSpinBox, QPlainTextEdit, QGridLayout, QToolBar, QMessageBox)



class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.UIBuild()
    def UIBuild(self):
        """Create the UI for the main window."""
        # Main window
        self.setWindowTitle("Caesar Cipher")
        self.setFixedSize(700,600)
        # Text Widget
        self.textEdit = QPlainTextEdit(self)
        self.textEdit.setPlaceholderText("Type your own text to encrypt/decrypt or open a .txt file....")
        #Buttons Widget
        self.buttonEncrypt = QPushButton("Encrypt", parent=self)
        self.buttonEncrypt.setFixedSize(60, 40)
        self.buttonEncrypt.clicked.connect(self.onEncryptClicked)
        self.buttonDecrypt = QPushButton("Decrypt", parent=self)
        self.buttonDecrypt.setFixedSize(60, 40)
        self.buttonDecrypt.clicked.connect(self.onDecryptClicked)
        #Spin Box Widget
        self.spinBox = QSpinBox(parent=self)
        self.spinBox.setRange(1, 26)
        #Labels Widget
        self.label = QLabel("Rotations:", parent=self)
        self.valueLabel = QLabel("Max rotations: 26", parent=self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.statusLabel = QMessageBox(text="Yes", parent=self)
        self.statusLabel.setStyleSheet("font-size: 12px")
        self.statusLabel.setWindowTitle("Success")
        # self.statusLabel.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        #Layout
        layout = QGridLayout()
        hBox = QHBoxLayout()
        vBox = QVBoxLayout()
        hBox.addWidget(self.buttonEncrypt)
        hBox.addWidget(self.buttonDecrypt)
        hBox.addWidget(self.label)
        hBox.addWidget(self.spinBox)
        hBox.addWidget(self.valueLabel)
        # vBox.addWidget(self.statusLabel)
        layout.addWidget(self.textEdit, 0, 0)
        layout.addLayout(hBox, 2, 0)
        layout.addLayout(vBox, 1, 0)
        
        # Actions
        self.actionFileOpen = QAction("&Open", parent=self)
        self.actionFileOpen.setShortcut(QKeySequence("Ctrl+O"))
        self.actionFileOpen.setStatusTip("Opens a .txt file")
        self.actionFileOpen.triggered.connect(self.onFileOpenClicked)

        self.actionFileEncrypt = QAction("&Encrypt", parent=self)
        self.actionFileEncrypt.setShortcut(QKeySequence("Ctrl+E"))
        self.actionFileEncrypt.setStatusTip("Encrypts a .txt file")
        self.actionFileEncrypt.triggered.connect(self.onEncryptClicked)

        self.actionFileDecrypt = QAction("&Decrypt", parent=self)
        self.actionFileDecrypt.setShortcut(QKeySequence("Ctrl+D"))
        self.actionFileDecrypt.setStatusTip("Decrypts a .txt file")
        self.actionFileDecrypt.triggered.connect(self.onDecryptClicked)
        
        
        self.actionFileSaveAs = QAction("Save &As...", parent=self)
        self.actionFileSaveAs.setShortcut(QKeySequence("Ctrl+Shift+s"))
        self.actionFileSaveAs.setStatusTip("Save the file")
        self.actionFileSaveAs.triggered.connect(self.onFileSaveAsClicked)
        
        self.actionFileExit = QAction("E&xit", parent=self)
        self.actionFileExit.setStatusTip("Exit the program")
        self.actionFileExit.triggered.connect(self.onFileExitClicked)
        
        # Status Bar
        self.statusBar = self.statusBar()
        
        #Menu bar
        self.menu = self.menuBar()
        self.menuFile = self.menu.addMenu("&File")
        self.menuFile.addAction(self.actionFileOpen)
        self.menuFile.addAction(self.actionFileSaveAs)
        self.menuFile.addAction(self.actionFileEncrypt)
        self.menuFile.addAction(self.actionFileDecrypt)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionFileExit)
        
        # Toolbar
        self.toolbar = QToolBar("Main Toolbar", parent=self)
        self.addToolBar(self.toolbar)
        self.toolbar.addAction(self.actionFileOpen)
        self.toolbar.addAction(self.actionFileEncrypt)
        self.toolbar.addAction(self.actionFileDecrypt)
        self.toolbar.addAction(self.actionFileSaveAs)
        self.toolbar.addAction(self.actionFileExit)
        
        centralWidget = QWidget(parent=self)
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)        
    def onFileOpenClicked(self):
        """Opens a .txt file and displays it in the GUI."""
        if sys.platform.startswith("win32"):
            initial_directory = Path.home() / "Desktop"
        else:
            initial_directory = Path.home()
        filePath = QFileDialog().getOpenFileName(caption="Open File", directory=str(initial_directory), 
                                                filter="Text files (*.txt)", parent=self)[0]
        if filePath:
            with open(filePath, "r") as f:
                user_text = f.read()
            self.textEdit.setPlainText(user_text)
    
    def onFileSaveAsClicked(self):
        """Grabs the text form the GUI and saves it as a .txt file."""
        if sys.platform.startswith("win32"):
            initial_directory = Path.home() / "Desktop"
        else:
            initial_directory = Path.home()
        filePath = QFileDialog().getSaveFileName(caption= "Save As", directory=str(initial_directory), 
                                                filter="Text files (*.txt)", parent=self)[0]
        if filePath:
            if not filePath.endswith(".txt"):
                filePath += ".txt"
            with open(filePath, "w") as f:
                f.write(self.textEdit.toPlainText())
        
        self.valueLabel.setText(str(self.spinBox.value()))
    
    def onEncryptClicked(self):
        """Encrypts the text file using the rotations provided by the user."""
        source_text = self.textEdit.toPlainText()
        rotations = self.spinBox.value()
        encrypted_string = ""
        for char in source_text:
            if char.isupper():
                encrypted_string += chr((ord(char) + rotations - 65) % 26 + 65)
            elif char.islower():
                encrypted_string += chr((ord(char) + rotations - 97) % 26 + 97)
            else:
                encrypted_string += char
        self.textEdit.clear()
        self.textEdit.setPlainText(encrypted_string)
        self.statusLabel.setText(f"Encryption completed with {rotations} rotations.")
        self.statusLabel.show()
        
    def onDecryptClicked(self):
        """Decrypts the text file using the rotations provided by the user."""
        source_text = self.textEdit.toPlainText()
        rotations = self.spinBox.value()
        decrypted_string = ""
        for char in source_text:
            if char.isupper():
                decrypted_string += chr((ord(char) - rotations - 65) % 26 + 65)
            elif char.islower():
                decrypted_string += chr((ord(char) - rotations - 97) % 26 + 97)
            else:
                decrypted_string += char
        self.textEdit.clear()
        self.textEdit.setPlainText(decrypted_string)
        self.statusLabel.setText(f"Decryption completed with {rotations} rotations.")
        self.statusLabel.show()
        
        
    def close_widget(self):
        """Use to close widgets after being displayed."""
        self.statusLabel.clear()
        self.statusLabel.setParent(None)
        self.statusLabel.deleteLater()
        self.statusLabel = None
        
    def onFileExitClicked(self):
        """Exits the program."""
        QApplication.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec()) # Close Window