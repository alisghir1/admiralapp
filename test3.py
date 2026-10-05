import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style()
style.theme_use('clam')
style.map('Treeview', background=[('selected', '#005A9E')], foreground=[('selected', '')])

t = ttk.Treeview(root)
t.pack()
t.insert('', 'end', iid='1', text='Test 1', tags=('terminee_sel',))
t.insert('', 'end', iid='2', text='Test 2', tags=('terminee',))
t.tag_configure('terminee', background='#388E3C', foreground='white')
t.tag_configure('terminee_sel', foreground='#66BB6A', font=('', 10, 'bold'))

t.selection_set('1')
root.after(3000, root.destroy)
root.mainloop()
