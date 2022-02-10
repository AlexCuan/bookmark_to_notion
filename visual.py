import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import reader


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Set window title based on ebook's name
        self.setWindowTitle(reader.BOOK_NAME)

        self.setMinimumSize(640, 480)

        self.setLayout(qtw.QVBoxLayout())

        # Ebook's name
        my_label = qtw.QLabel(reader.BOOK_NAME)
        my_label.setFont(qtg.QFont('Arial', 20))

        # Widget for reading the ebook
        text_browser = qtw.QTextBrowser()
        text_browser.setText(reader.ebook_text)

        self.layout().addWidget(my_label)
        self.layout().addWidget(text_browser)
        self.show()

app = qtw.QApplication([])