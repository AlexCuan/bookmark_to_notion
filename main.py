import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup


def epub2thtml(epub_path):
    book = epub.read_epub(epub_path)
    chapters = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append(item.get_content())
    return chapters


blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head',
    'input',
    'script',
    # there may be more elements you don't want, such as "style", etc.
]


def chap2text(chap):
    output = ''
    soup = BeautifulSoup(chap, 'lxml')
    text = soup.find_all(text=True)
    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
    return output


def thtml2ttext(thtml):
    Output = []
    for html in thtml:
        text = chap2text(html)
        Output.append(text)
    return Output


def epub2text(epub_path):
    chapters = epub2thtml(epub_path)
    ttext = thtml2ttext(chapters)
    return ttext


out = epub2text('./enfocate.epub')


# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(800, 600)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget,)
#         self.textBrowser.setGeometry(QtCore.QRect(10, 10, 681, 531))
#         self.textBrowser.setObjectName("textBrowser")
#         self.textBrowser.setText(str(out))
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         MainWindow.layout().addWidget( self.textBrowser)
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#
#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello world")
        self.setLayout(qtw.QVBoxLayout())

        my_label = qtw.QLabel("Enfocate")

        text_browser = qtw.QTextBrowser()
        text_browser.setText(str(out))

        self.layout().addWidget(my_label)
        self.layout().addWidget(text_browser)
        self.show()

app = qtw.QApplication([])

mw = MainWindow()

# Run the app

app.exec_()