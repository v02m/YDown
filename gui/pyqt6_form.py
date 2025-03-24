from PyQt6.QtWidgets import QApplication, QWidget, QLabel

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt6 Form')
        label = QLabel('Hello, PyQt6!', self)
        label.move(50, 50)
        self.setGeometry(100, 100, 300, 200)

def run():
    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec()
