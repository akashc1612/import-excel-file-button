import tkinter as tk
from tkinter import filedialog
import pandas as pd
root = tk.Tk()
canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised' )
canvas1.pack()
def getexcel():
    global df

    import_file_path = filedialog.askopenfilename()
    df = pd.read_excel(import_file_path)
    print(df)

browseButton_excel = tk.Button(text = "     Import excel file         ",
                               command = getexcel, bg = 'blue', fg = 'black', font =
                               ('helvetica', 14, 'bold'))
canvas1.create_window(150, 150, window = browseButton_excel)
root.mainloop()
