import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from PyQt5 import uic
import reader


class Ui(qtw.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()

        # Load Ui
        uic.loadUi('loader.ui', self)

        # Define widgets
        self.setWindowTitle("Lector")
        self.textBrowser = self.findChild(qtw.QTextBrowser, "textBrowser")
        self.menu = self.findChild(qtw.QMenu, "menuMenu")
        self.openArchive = self.findChild(qtw.QAction, "openArchive")
        self.openArchive.triggered.connect(self.open_file)

        self.show()

    def open_file(self):
        ebook_name = qtw.QFileDialog.getOpenFileName(self, "Open file", "", "Epub Files(*.epub)")
        if ebook_name:
            self.textBrowser.setText(reader.epub2text(ebook_name[0]))

        # self.setWindowTitle(ebook_name[0])


app = qtw.QApplication([])
