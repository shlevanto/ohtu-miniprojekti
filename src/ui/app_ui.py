from ui.console_io import console_io as default_console_io
from entities.bookmark import Bookmark
from repositories.bookmarks_repository import bookmark_repository as default_bookmark_repository


class AppUi:
    def __init__(self, ui=default_console_io, repository=default_bookmark_repository):
        self.ui = ui
        self.repository = repository

    def read_input(self):
        return self.ui.read("Give command: ")

    def parse_command(self, input):
        input = input.strip()
        if input == "add":
            self.add()
        elif input == "show":
            self.show()
        elif input == "edit":
            self.ui.write("Edit-command is not yet implemented")
        elif input == "search":
            self.search()
        else:
            self.usage()

    def welcome(self):
        self.ui.write("Welcome to Bookmarker!")

    def add(self):
        title = self.ui.read("Title: ")
        self.add_bookmark(title)
    
    def add_bookmark(self, title):
        bookmark = Bookmark(title)
        self.repository.insert(bookmark.as_dict())
        self.ui.write(f'Bookmark "{title}" created!')

    def show(self):
        bookmarks = self.repository.get_all()
        if not bookmarks:
            self.ui.write("No bookmarks")
        else:
            for bookmark in bookmarks:
                self.ui.write(bookmark["title"])
    
    def search(self):
        term = self.ui.read("Term: ")
        self.search_by_title(term)
    
    def search_by_title(self, title):
        self.ui.write(
            "\n".join(
                [bookmark["title"] for bookmark in self.repository.find_by_title(title)]
                )
            )

    def edit(self):
        self.ui.write("Edit-command is not yet implemented")

    def usage(self):
        self.ui.write("""
            Acceptable commands:
            'q' - quit,
            'add' - add a new bookmark,
            'show' - show given amount of bookmarks,
            'edit' - edit a bookmark
        """)

app_ui = AppUi()