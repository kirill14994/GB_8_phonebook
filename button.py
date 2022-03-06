import tkinter as tk

def create_button(name, do_command, i):
	button = tk.Button(text=name,          # текст кнопки
					background='#555',     # фоновый цвет кнопки
					foreground='#ccc',     # цвет текста
					padx='20',             # отступ от границ до содержимого по горизонтали
					pady='8',              # отступ от границ до содержимого по вертикали
					font='12',)
	print(i)
	button.bind("<Button-1>", do_command)
	button.grid(row = 1, column = i+1)
	return button


def main_button():
	name_buttons = (('import', $$$ ), ('export', $$$ ), ('add', $$$ ), ('exit', $$$ ))
	[create_button(text[0], text[1], name_buttons.index((text[0], text[1]))) for text in name_buttons]

# name_buttons_in_line = (('edit', e_d.export_file) , ('remove', e_d.export_file))
# main_button()

