import sys
import string
from pathlib import Path
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QKeySequence
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
    QFileDialog,
    QSpinBox,
    QPlainTextEdit,
    QGridLayout,
    QToolBar,
    QMessageBox,
    QCheckBox,
)


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
        self.textEdit.setPlaceholderText("Type a word or phrase to test.")
        self.testButton = QPushButton("Test", parent=self)
        self.testButton.clicked.connect(self.cleanString)
        self.clearButton = QPushButton("Clear", parent=self)
        self.clearButton.clicked.connect(self.onClear)
        self.palindromeLabel = QLabel("Is it a palindrome?", parent=self)
        self.palindromeLabel.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )
        self.answerLabel = QLabel("", parent=self)
        self.answerLabel.setStyleSheet("font-size: 24px")
        self.answerLabel.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
        )
        self.checkBox = QCheckBox("Include Spaces?", parent=self)
        # Setting the layout for the main Window.
        layout = QGridLayout()
        vBox2 = QVBoxLayout()
        vBox = QVBoxLayout()
        hBox = QHBoxLayout()
        vBox.addWidget(self.textEdit)
        hBox.addWidget(self.palindromeLabel)
        hBox.addWidget(self.answerLabel)
        vBox2.addWidget(self.checkBox)
        vBox2.addWidget(self.testButton)
        vBox2.addWidget(self.clearButton)
        layout.addLayout(vBox2, 0, 1)
        layout.addLayout(vBox, 0, 0)
        layout.addLayout(hBox, 1, 0)
        # Central Widget containing all layouts.
        centralWidget = QWidget(parent=self)
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def onClear(self):
        """Clear the text box and the palindrome answer label."""
        self.answerLabel.clear()
        self.textEdit.clear()

    def onLabelChanged(self, answer: bool):
        """Checks if palindrome is true, if so it will display if yes palindrome not otherwise"""
        if answer is True:
            self.answerLabel.setStyleSheet(
                "color: #49d90b; font-weight: bold; font-size: 24px"
            )
            return self.answerLabel.setText("Yes")
        else:
            self.answerLabel.setStyleSheet(
                "color: #f53514; font-weight: bold; font-size: 24px"
            )
            self.answerLabel.setText("No")

    def cleanString(self):
        """Removes unnecessary characters from the text given by the user"""
        text = self.textEdit.toPlainText()
        if self.checkBox.isChecked():
            translation_table = str.maketrans(
                string.ascii_lowercase,
                string.ascii_uppercase,
                string.punctuation + string.digits,
            )
            text = text.translate(translation_table)
            answer = self.isPalindrome(text)
            self.onLabelChanged(answer)
            return answer
        else:
            translation_table = str.maketrans(
                string.ascii_lowercase,
                string.ascii_uppercase,
                string.whitespace + string.punctuation + string.digits,
            )
            text = text.translate(translation_table)
            answer = self.isPalindrome(text)
            self.onLabelChanged(answer)
            return answer

    def isPalindrome(self, text: str) -> bool:
        """Checks if the current string in the text box is a palindrome using recursion"""
        if len(text) <= 1:
            return True
        else:
            if text[0] == text[-1]:
                return self.isPalindrome(text[1:-1])
            else:
                return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    palindrome = MainWindow()
    palindrome.show()
    sys.exit(app.exec())
