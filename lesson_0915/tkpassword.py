def checkPw():
    if pw.get() == 1234:
        msg.set("密碼正確,請登入")
    else:
        msg.set("密碼錯誤,請修改")


import tkinter as tk

win = tk.Tk()
pw = tk.StringVar()
msg = tk.StringVar()
label = tk.Label(win, text="請輸入密碼")
label.pack()
entry = tk.Entry(win, textvariable=pw)
entry.pack()
button = tk.Button(win, text="登入", command=checkPw)
button.pack()
lblmsg = tk.Label(win, fg="red", textvariable=msg)
lblmsg.pack()
win.mainloop()
