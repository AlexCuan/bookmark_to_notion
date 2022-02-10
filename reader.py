from ebooklib import epub
from bs4 import BeautifulSoup
import ebooklib

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