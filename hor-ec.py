import ebook
import sys
from scripts import editor


def fix_ebook(filename):
    book = ebook.EBook(filename)
    book.open_book()
    book.fix_book()
    book.rebuild_book()


filename = sys.argv[-1]
fix_ebook(filename)
