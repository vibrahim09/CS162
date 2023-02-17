import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QLineEdit, QSpinBox


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App.")
        self.setFixedSize(400,300)
        
        # self.button = QPushButton("Click me!", parent=self)
        # self.button.clicked.connect(self.onButtonClicked)
        
        self.spinBoxLabel = QLabel("Value:", parent=self)
        self.spinBoxLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
        # self.label.setStyleSheet("background-color: green;")
        self.spinBox = QSpinBox(parent=self)
        self.spinBox.setMinimum(-10)
        self.spinBox.setMaximum(10)
        self.spinBox.valueChanged.connect(self.onValueChanged)
        
        
        self.valueLabel = QLabel("0", parent=self)
        
        hBox = QHBoxLayout()
        hBox.addWidget(self.spinBoxLabel)
        hBox.addWidget(self.spinBox)
        
        vBox = QVBoxLayout()
        vBox.addLayout(hBox)
        vBox.addWidget(self.valueLabel)
        
        # layout = QVBoxLayout()
        # layout.addWidget(self.button)
        # layout.addWidget(self.label)
        
        centralWidget = QWidget(parent=self)
        centralWidget.setLayout(vBox)
        
        self.setCentralWidget(centralWidget)
        
        
        
    # def onButtonClicked(self):
    #     self.label.setText("You Clicked me: ")
    
    def onValueChanged(self):
        self.valueLabel.setText(str(self.spinBox.value))
            
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()

    window.show()

    sys.exit(app.exec()) # Start the event loop.