import tkinter as tk
window = tk.Tk()
window.title("Calculator")
window.geometry("400x175")
window.configure(bg="cyan")

def add():
    global result, num1, num2, entrynum1, entrynum2, resultLabel
    num1 = entrynum1.get()
    num2 = entrynum2.get()
    result = int(num1) + int(num2)
    resultLabel.destroy()
    resultLabel = tk.Label(frameResult, text = result, bg = "white", width = 45, padx = 5)
    resultLabel.grid(column = 1, row = 0) 
    
def subtract():
    global result, num1, num2, entrynum1, entrynum2, resultLabel
    num1 = entrynum1.get()
    num2 = entrynum2.get()
    result = int(num1) - int(num2)
    resultLabel.destroy()
    resultLabel = tk.Label(frameResult, text = result, bg = "white", width = 45, padx = 5)
    resultLabel.grid(column = 1, row = 0) 

def multiply():
    global result, num1, num2, entrynum1, entrynum2, resultLabel
    num1 = entrynum1.get()
    num2 = entrynum2.get()
    result = int(num1) * int(num2)
    resultLabel.destroy()
    resultLabel = tk.Label(frameResult, text = result, bg = "white", width = 45, padx = 5)
    resultLabel.grid(column = 1, row = 0) 

def divide():
    global result, num1, num2, entrynum1, entrynum2, resultLabel
    num1 = entrynum1.get()
    num2 = entrynum2.get()
    result = int(num1) / int(num2)  
    resultLabel.destroy()
    resultLabel = tk.Label(frameResult, text = result, bg = "white", width = 45, padx = 5)
    resultLabel.grid(column = 1, row = 0) 
    
frame1 = tk.Frame(master = window, width = 100, height = 100, bg = "cyan", padx = 5, pady = 10)
label1 = tk.Label(frame1, text = "Number 1:", bg = "cyan")
entrynum1 = tk.Entry(frame1, fg="black", bg="white", width=100)
frame1.pack(anchor = "n")
label1.pack(side=tk.LEFT)
entrynum1.pack(side=tk.LEFT)

frame2 = tk.Frame(master = window, width = 100, height = 100, bg = "cyan", padx = 5, pady = 10)
label2 = tk.Label(frame2, text = "Number 2:", bg = "cyan")
entrynum2 = tk.Entry(frame2, fg="black", bg="white", width=100)
frame2.pack(anchor = "n")
label2.pack(side=tk.LEFT)
entrynum2.pack(side=tk.LEFT)

buttons = tk.Frame(master = window, width = 100, height = 100, bg = "cyan", padx = 10, pady = 5)
buttons.propagate(0)
buttons.pack()

butAdd = tk.Button(buttons, text = "+", height=1, width = 10, activebackground = "yellow",
                 activeforeground = "black", bg="light yellow", fg ="black",
                 bd=5, command=add)

butSubtract = tk.Button(buttons, text = "-", height=1, width = 10, activebackground = "green",
                 activeforeground = "black", bg="light green", fg ="black",
                 bd=5, command=subtract)

butMultiply = tk.Button(buttons, text = "*", height=1, width = 10, activebackground = "dark red",
                 activeforeground = "black", bg="red", fg ="black",
                 bd=5, command=multiply)

butDivide = tk.Button(buttons, text = "/", height=1, width = 10, activebackground = "dark grey",
                 activeforeground = "black", bg="grey", fg ="black",
                 bd=5, command=divide)
butAdd.grid(column = 0, row = 0, padx= 5, pady= 5)
butSubtract.grid(column = 1, row = 0, padx= 5, pady= 5)
butMultiply.grid(column = 2, row = 0, padx= 5, pady= 5)
butDivide.grid(column = 3, row = 0, padx= 5, pady= 5) 

frameResult = tk.Frame(master = window, width = 100, height = 100, bg = "cyan", padx = 15, pady = 5)
resultWord = tk.Label(frameResult, text = "Result:", bg = "cyan", padx = 5)
resultLabel = tk.Label(frameResult, text = "", bg = "white", width = 45, padx = 5)
frameResult.pack()
resultWord.grid(column = 0, row = 0)
resultLabel.grid(column = 1, row = 0) 


window.mainloop()
