import os
import shutil
import tkinter as tk
from tkinter import filedialog

class FileReplaceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Replacement Tool")

        self.source_dir = tk.StringVar()
        self.destination_dir = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Source directory selection
        tk.Label(self.root, text="Source Directory:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.source_dir, state='readonly', width=40).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Select", command=self.select_source_directory).grid(row=0, column=2, padx=10, pady=10)

        # Destination directory selection
        tk.Label(self.root, text="Destination Directory:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.destination_dir, state='readonly', width=40).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Select", command=self.select_destination_directory).grid(row=1, column=2, padx=10, pady=10)

        # Replace files button
        tk.Button(self.root, text="Replace Files", command=self.replace_files).grid(row=2, column=1, pady=20)

    def select_source_directory(self):
        selected_dir = filedialog.askdirectory()
        self.source_dir.set(selected_dir)

    def select_destination_directory(self):
        selected_dir = filedialog.askdirectory()
        self.destination_dir.set(selected_dir)

    def replace_files(self):
        source_dir = self.source_dir.get()
        destination_dir = self.destination_dir.get()

        if not (source_dir and destination_dir):
            tk.messagebox.showerror("Error", "Please select source and destination directories.")
            return

        try:
            # Iterate through files in source directory
            for filename in os.listdir(source_dir):
                source_file_path = os.path.join(source_dir, filename)
                destination_file_path = os.path.join(destination_dir, filename)

                # Replace the file in the destination directory if it exists
                if os.path.exists(destination_file_path):
                    shutil.copy2(source_file_path, destination_file_path)

            tk.messagebox.showinfo("Success", "Files replaced successfully.")
        except Exception as e:
            tk.messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileReplaceApp(root)
    root.mainloop()
