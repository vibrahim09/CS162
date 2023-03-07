import sys
import string
from pathlib import Path
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QKeySequence
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout, 
                            QFileDialog, QSpinBox, QPlainTextEdit, QGridLayout, QToolBar, QMessageBox, QCheckBox)


class MainWindow(QMainWindow):
    """Main Window for our program."""
    def __init__(self):
        super().__init__()
        
        self.UI_init()
    
    def UI_init(self):
        """Initialize the main window widgets"""
        
        self.setWindowTitle("Palindrome Test Application")
        self.setFixedSize(400, 200)
        
        # Set the widgets for the main window
        self.textEdit = QPlainTextEdit(parent=self)
        self.testButton = QPushButton("Test", parent=self)
        self.testButton.clicked.connect(self.cleanString)
        self.palindromeLabel = QLabel("Is it a palindrome?", parent=self)
        self.answerLabel = QLabel("")
        self.checkBox = QCheckBox("Include Spaces?", parent=self)
        # Setting the layout for the main Window.
        layout = QGridLayout()
        vBox2 = QVBoxLayout()
        vBox = QVBoxLayout()
        vBox.addWidget(self.textEdit)
        vBox.addWidget(self.palindromeLabel)
        vBox.addWidget(self.answerLabel)
        vBox2.addWidget(self.checkBox)
        vBox2.addWidget(self.testButton)
        layout.addLayout(vBox2, 0, 1)
        layout.addLayout(vBox, 0, 0)
        # Central Widget containing all layouts. 
        centralWidget = QWidget(parent=self)
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
        
    def onLabelChanged(self):
        """Checks if palindrome is true, if so it will display if yes palindrome not otherwise"""
        if self.cleanString() is True:
            return self.palindromeLabel.setText("Yes")
        else:
            self.palindromeLabel.setText("No")
    def cleanString(self):
        """Removes unnecessary characters from the text given by the user"""
        text = self.textEdit.toPlainText()
        if self.checkBox.isChecked():
            translation_table = str.maketrans(string.ascii_lowercase, string.ascii_uppercase, 
                                                string.punctuation + string.digits)
            text = text.translate(translation_table)
            print(text)
            answer = self.isPalindrome(text)
            return answer
        else:
            translation_table = str.maketrans(string.ascii_lowercase, string.ascii_uppercase, 
                                            string.whitespace + string.punctuation + string.digits)
            text = text.translate(translation_table)
            # answer = self.isPalindrome(text)
            # self.onLabelChanged()
            return text
    def isPalindrome(self, text: str) -> bool:
        """Checks if the current string in the text box is a palindrome using recursion"""
        if len(text) <= 1:
            return True
        else:
            if text[0] == text[-1]:
                return self.isPalindrome(text[1:-1])
            else:
                return False

























if __name__ == '__main__':
    app = QApplication(sys.argv)
    palindrome = MainWindow()
    palindrome.show()
    sys.exit(app.exec())
    