import ebook
from scripts import editor


def fix_ebook(filename):
    book = ebook.EBook(filename)
    book.open_book()
    book.fix_book()
    book.rebuild_book()


filename = 'Grancrest Senki 1 - Rainbow Mage Siluca.epub'
fix_ebook(filename)
