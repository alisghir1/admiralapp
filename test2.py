import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style()
style.theme_use('clam')
style.map('Treeview', background=[('selected', '')], foreground=[('selected', '')])

t = ttk.Treeview(root)
t.pack()
t.insert('', 'end', iid='1', text='Test 1', tags=('terminee',))
t.insert('', 'end', iid='2', text='Test 2', tags=('terminee',))

t.tag_configure('terminee', background='#388E3C')
t.tag_configure('terminee_sel', background='#4CAF50', font=('', 10, 'bold'))

def on_sel(e):
    sel = t.selection()
    for i in t.get_children():
        tags = t.item(i, 'tags')
        base = tags[0].replace('_sel', '')
        new_t = base + '_sel' if i in sel else base
        t.item(i, tags=(new_t,))

t.bind('<<TreeviewSelect>>', on_sel)
t.selection_set('1')

root.after(2000, root.destroy)
root.mainloop()
