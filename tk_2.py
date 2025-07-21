import tkinter as tk

win = tk.Tk()

win.title("標題")

frame1 = tk.Frame(win)
frame1.pack()

label1 = tk.Label(frame1, text="文字標籤", font=("Arial", 16))
entry1 = tk.Entry(frame1)

label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)

frame2 = tk.Frame(win)
frame2.pack()

button1 = tk.Button(frame2, text="確定", font=("Arial", 16))
button2 = tk.Button(frame2, text="取消", font=("Arial", 16))
button1.grid(row=0, column=0, padx=20)
button2.grid(row=0, column=1, padx=20)

win.mainloop()
