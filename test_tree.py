import tkinter as tk
from tkinter import ttk
root = tk.Tk()
style = ttk.Style()
style.theme_use('clam')
style.map('Treeview', background=[('selected', '')], foreground=[('selected', 'yellow')])
t = ttk.Treeview(root)
t.pack()
t.insert('', 'end', text='Test 1', tags=('red',))
t.tag_configure('red', background='red')
t.selection_set(t.get_children()[0])
root.after(1000, root.destroy)
root.mainloop()
