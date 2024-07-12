import tkinter as tk
import tkinter.filedialog as fd
import sys


class Note(tk.Frame):
    def __init__(self, root, file_name=None):
        super().__init__(root)
        self.file_name = file_name
        self.__create_UI()
        if self.file_name:
            self.__open_file(self.file_name)

    def __create_UI(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.configure(bg="#2E2E2E")
        font_settings = ("Comic Sans MS", 12)

        self.text = tk.Text(self, bg="#1E1E1E", fg="#FFFFFF", insertbackground="#FFFFFF",
                            selectbackground="#555555", selectforeground="#FFFFFF",
                            font=font_settings)
        self.text.grid(row=0, rowspan=2, column=0, columnspan=3, sticky="nsew")

        self.saveasbtn = tk.Button(self, text="зберегти як", command=self.__save_as_file,
                                   bg="#3C3F41", fg="#FFFFFF", activebackground="#555555",
                                   activeforeground="#FFFFFF")
        self.saveasbtn.grid(row=2, column=0, sticky="ew")

        self.savebtn = tk.Button(self, text="зберегти", command=self.__save_file,
                                 bg="#3C3F41", fg="#FFFFFF", activebackground="#555555",
                                 activeforeground="#FFFFFF")
        self.savebtn.grid(row=2, column=1, sticky="ew")

        self.openbtn = tk.Button(self, text="відкрити", command=self.__open_file_dialog,
                                 bg="#3C3F41", fg="#FFFFFF", activebackground="#555555",
                                 activeforeground="#FFFFFF")
        self.openbtn.grid(row=2, column=2, sticky="ew")

    def __open_file_dialog(self):
        file_name = fd.askopenfilename(initialdir="files_for_notes")
        if file_name:
            self.file_name = file_name
            self.__open_file(file_name)

    def __open_file(self, file_name):
        with open(file_name, "r", encoding="utf-8") as file:
            self.text.delete(1.0, tk.END)
            self.text.insert(tk.END, file.read())

    def __save_as_file(self):
        file_name = fd.asksaveasfilename(filetypes=[("Docs", ".txt")], initialdir="files_for_notes")
        if file_name:
            self.file_name = file_name
            self.__save_file()

    def __save_file(self):
        if self.file_name is None:
            self.__save_as_file()
        else:
            with open(self.file_name, "w", encoding="utf-8") as file:
                file.write(self.text.get(1.0, tk.END))


if __name__ == "__main__":
    window = tk.Tk()
    window.title("блокнот")
    window.iconbitmap("AAA.ico")
    window.configure(bg="#2E2E2E")

    file_name = None
    if len(sys.argv) > 1:
        file_name = sys.argv[1]

    app = Note(window, file_name)
    app.pack(expand=True, fill=tk.BOTH)
    window.mainloop()