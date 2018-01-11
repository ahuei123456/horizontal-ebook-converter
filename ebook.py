import os
import shutil
import zipfile

from scripts import editor


class EBook:

    def __init__(self, filename):
        self.book_name = filename
        self.book_path = os.path.join(os.getcwd(), os.path.splitext(filename)[0])
        self.text_directory = os.path.join(self.book_path, 'item', 'xhtml')

    def open_book(self):
        with zipfile.ZipFile(self.book_name, 'r') as ebook:
            ebook.extractall(self.book_path)
            print(os.getcwd())

    def rebuild_book(self):
        new_name = self.get_new_book()
        shutil.make_archive(new_name, 'zip', self.book_path)
        shutil.rmtree(self.book_path)
        os.rename(new_name + '.zip', new_name)

    def get_new_book(self):
        return self.book_path + '-updated.epub'

    def fix_book(self):
        pages = self.get_pages()
        editor.edit_html(pages)

    def get_pages(self):
        pages = []
        for filename in os.listdir(self.text_directory):
            if 'xhtml' in filename.split('.'):
                pages.append(os.path.join(self.text_directory, filename))

        return pages