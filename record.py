def record():
    root = Tk('D:\puzzlegame\pume')
    root.title("puzzlegame")
    WIDTH = 450
    HEIGHT = 450
    f = open('D:\puzzlegame\pume\\record.txt', 'r')
    lines = f.readlines()
    for line in lines:
        label2 = Label(root, text=line, fg="red", width=40, height=2)
        label2.pack()
    f.close()
    root.mainloop()