import tkinter as tk
from tkinter import filedialog, messagebox

class NotepadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Flow - Notepad")
        self.text_area = tk.Text(root, undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=1)
        self.current_file = None
        self.create_menu()
        self.root.bind('<Command-z>', lambda e: self.text_area.edit_undo())
        self.root.bind('<Command-Shift-z>', lambda e: self.text_area.edit_redo())

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=lambda: self.root.focus_get().event_generate('<<Cut>>'))
        edit_menu.add_command(label="Copy", command=lambda: self.root.focus_get().event_generate('<<Copy>>'))
        edit_menu.add_command(label="Paste", command=lambda: self.root.focus_get().event_generate('<<Paste>>'))
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        self.root.config(menu=menu_bar)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.current_file = None
        self.root.title("Untitled - Text Flow")

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, content)
            self.current_file = file_path
            self.root.title(f"{file_path} - Text Flow")

    def save_file(self):
        if self.current_file:
            content = self.text_area.get(1.0, tk.END)
            with open(self.current_file, "w") as file:
                file.write(content)
            messagebox.showinfo("Saved", "File saved successfully.")
        else:
            self.save_as()

    def save_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.current_file = file_path
            self.root.title(f"{file_path} - Text Flow")

if __name__ == "__main__":
    root = tk.Tk()
    app = NotepadApp(root)
    root.mainloop()