import tkinter as tk
import tkinter.filedialog as fd

def get_adress():
	path = fd.Open(filetypes = [('*.txt files', '.txt'), ('*.csv files', '.csv')]).show()
	return path

def get_adress_to_save():
	root = tk.Tk()
	path = fd.SaveAs(root, filetypes = [('*.txt files', '.txt'), ('*.csv files', '.csv')]).show()
	return path

def input_con(title):
	return input(f'{title}: ')


# def textarea():
# 	textFrame = tk.Frame(height = 340, width = 600)
# 	textFrame.grid(row = 2, column = 1)
# 	textbox = tk.Text(textFrame, font='Arial 14', wrap='word')
# 	scrollbar = tk.Scrollbar(textFrame)
# 	scrollbar['command'] = textbox.yview
# 	textbox['yscrollcommand'] = scrollbar.set