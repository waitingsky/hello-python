import tkinter as tk
from tkinter import *
from tkinter import messagebox

def say_hi():
    print("Hello World!")
    messagebox.askokcancel('Hello', 'Hello World!')

def test():
    print(e2.get())
    if e2.get() == "123":
        messagebox.askokcancel('Prompt', '正确!')
        return True
    else:
        messagebox.askokcancel('Prompt', '错误!')
        e1.delete(0, END)
        return False

# 创建一个主窗口，用于容纳整个GUI程序
root = tk.Tk()
# 设置主窗口对象的标题栏
root.title("HelloWorld")

# label
lbl = tk.Label(root, text="HelloWorld")
# 然后调用Label组建的pack()方法，用于自动调节组件自身的尺寸
lbl.pack()

# button
btn = tk.Button(root, text="Hello", fg="blue", command=say_hi)
btn.pack(side=tk.LEFT)

# checkbutton
options = ["中文", "英文"]
v = []
for option in options:
    v.append(IntVar())
    b = Checkbutton(root, text=option, variable=v[-1])
    b.pack(anchor=W)

# Radiobutton
v = IntVar()
Radiobutton(root, text="男性", variable=v, value=1).pack(anchor=W)
Radiobutton(root, text="女性", variable=v, value=2).pack(anchor=W)
rb1 = Radiobutton(root, text="男性", variable=v, value=1, indicatoron=False)
rb1.pack(fill=X)
rb2 = Radiobutton(root, text="女性", variable=v, value=2, indicatoron=False)
rb2.pack(fill=X)


# LabelFrame
group = LabelFrame(root, text="LabelFrame", padx=5, pady=5)
group.pack(padx=10, pady=10)

# Entry
e1 = Entry(group)
e1.pack(padx=20, pady=20)
e1.delete(0, END)
e1.insert(0, "请输入您的姓名...")

v = StringVar()
e2 = Entry(group, textvariable=v, validate="focusout", validatecommand=test)
e2.pack(padx=10, pady=10)

# Listbox
lb = Listbox(root, setgrid=True)
lb.pack()
# 往列表里添加数据
for item in ["篮球", "足球", "乒乓球", "羽毛球"]:
    lb.insert(END, item)
theButton = Button(root, text="删除", command=lambda x=lb: x.delete(ACTIVE))
theButton.pack()

# Scrollbar
sb = Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)
lb = Listbox(root, yscrollcommand=sb.set)
for i in range(1000):
    lb.insert(END, str(i))
lb.pack(side=LEFT, fill=BOTH)
sb.config(command=lb.yview)

# Scale
Scale(root, from_=-100, to=42).pack()
Scale(root, from_=0, to=200, orient=HORIZONTAL).pack()

#让根窗口进入事件循环
root.mainloop()