import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

BOOK_NAME = "Enfocate"


def epub2thtml(epub_path: str) -> list:
    """
    Read the epub and extract readable items
    :param epub_path:
    :return: List containing chapters content(in html)
    """
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


def chap2text(chap: str) -> str:
    """
    Parse the html and return a clean list of content
    :param chap:
    :return: str
    """
    output = ''
    soup = BeautifulSoup(chap, 'html.parser')
    text = soup.find_all(text=True)
    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
    return output


def thtml2ttext(thtml: list) -> str:
    """
    Iterate over the chapter's list, parse it and append clean text into an str
    :param thtml: List of raw html
    :return: Clean text ready for reading
    """
    # Output = []
    text = ""
    for html in thtml:
        text += chap2text(html)
        # Output.append(text)
    return text


def epub2text(epub_path: str) -> str:
    chapters = epub2thtml(epub_path)
    ttext = thtml2ttext(chapters)
    return ttext


ebook_text = epub2text('./enfocate.epub')


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Set window title based on ebook's name
        self.setWindowTitle(BOOK_NAME)

        self.setMinimumSize(640, 480)

        self.setLayout(qtw.QVBoxLayout())

        # Ebook's name
        my_label = qtw.QLabel(BOOK_NAME)
        my_label.setFont(qtg.QFont('Arial', 20))

        # Widget for reading the ebook
        text_browser = qtw.QTextBrowser()
        text_browser.setText(ebook_text)

        self.layout().addWidget(my_label)
        self.layout().addWidget(text_browser)
        self.show()

app = qtw.QApplication([])

mw = MainWindow()

# Run the app

app.exec_()