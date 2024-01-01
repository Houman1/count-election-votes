from tkinter import *
from tkinter import filedialog

def browse_uncounted_folder():
    uncounted_folder = filedialog.askdirectory()
    uncounted_folder_entry.delete(0, END)
    uncounted_folder_entry.insert(0, uncounted_folder)

def browse_counted_folder():
    counted_folder = filedialog.askdirectory()
    counted_folder_entry.delete(0, END)
    counted_folder_entry.insert(0, counted_folder)

root = Tk()
root.title("Ballot Folder Selection")

# Set the window size and add padding
root.geometry("550x400")
root.configure(padx=20, pady=20)

# Uncounted Ballot Folder
uncounted_label = Label(root, text="Uncounted Ballot Folder Location:")
uncounted_label.pack(pady=5)

uncounted_folder_entry = Entry(root, width=40)
uncounted_folder_entry.pack(pady=5)

uncounted_button = Button(root, text="Browse", command=browse_uncounted_folder)
uncounted_button.pack(pady=10)

# Counted and Spoiled Ballot Folder
counted_label = Label(root, text="Counted and Spoiled Ballot Folder Destination:")
counted_label.pack(pady=5)

counted_folder_entry = Entry(root, width=40)
counted_folder_entry.pack(pady=5)

counted_button = Button(root, text="Browse", command=browse_counted_folder)
counted_button.pack(pady=10)

# Submit Button (you can add functionality as needed)
submit_button = Button(root, text="Submit")
submit_button.pack(pady=20)

root.mainloop()
