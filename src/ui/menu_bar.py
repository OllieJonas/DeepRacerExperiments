from tkinter import Menu, messagebox


class MenuBar:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.test_count = 0

        self.menubar = Menu(root)
        self.add_file_menu()

        self.root.config(menu=self.menubar)

    def add_file_menu(self):
        self.test_count += 1
        menu = Menu(self.menubar, tearoff=0)
        menu.add_command(label="Test", command=lambda: print("testing 123 wow"))
        self.menubar.add_cascade(label="File", menu=menu)
