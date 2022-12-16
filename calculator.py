import tkinter as tk
# importing tkinter and setting up the window
window = tk.Tk()
window.title("Calculator")
window.geometry("400x175")
window.configure(bg="cyan") # change full background

# Functions to do math
def add():
    global result, num1, num2, entrynum1, entrynum2, resultLabel # global variables to use inside the function from outside
    num1 = entrynum1.get() # reading entry values
    num2 = entrynum2.get()
    
    if num1.isdigit() and num2.isdigit(): # checking if entry is a number
        result = int(num1) + int(num2) # doing the math
        answer()
    else:
        numError()
    
def subtract():
    global result, num1, num2, entrynum1, entrynum2, resultLabel
    num1 = entrynum1.get()
    num2 = entrynum2.get()
    if num1.isdigit() and num2.isdigit():
        result = int(num1) - int(num2)
        answer()
    else:
        numError()
        
def multiply():
    global result, num1, num2, entrynum1, entrynum2, resultLabel
    num1 = entrynum1.get()
    num2 = entrynum2.get()
    if num1.isdigit() and num2.isdigit():
        result = int(num1) * int(num2)
        answer()
    else:
        numError()
        
def divide():
    global result, num1, num2, entrynum1, entrynum2, resultLabel
    num1 = entrynum1.get()
    num2 = entrynum2.get()
    if num1.isdigit() and num2.isdigit():
        result = int(num1) / int(num2)  
        answer()
    else:
        numError()
    
def numError(): # error window if entries do not = digits
        winOPEN = tk.Toplevel()
        winOPEN.geometry("200x100")
        winOPEN.title("Error")
        winOPEN.configure(background = "cyan")
        winOPEN.focus()
        errorSentence = tk.Label(master = winOPEN, text = "Please Use Numbers", bg = "cyan", width = 45, padx = 5, pady = 5, font = 4)
        errorSentence2 = tk.Label(master = winOPEN, text = "In The Input Boxes", bg = "cyan", width = 45, padx = 5, pady = 5, font = 4)
        errorSentence.pack()
        errorSentence2.pack()
        exitButton = tk.Button(master = winOPEN, text = "OK", font = 24, command = winOPEN.destroy) # If button clicked close window
        exitButton.pack()
        winOPEN.transient(window) # Make second window ontop of first
        winOPEN.grab_set() #freeze main window
        window.wait_window(winOPEN) # pause all main window actions until child window closes
        
def answer(): # writing the answer on the screen
    global result, num1, num2, entrynum1, entrynum2, resultLabel
    resultLabel.destroy()  # remove old answer
    resultLabel = tk.Label(frameResult, text = result, bg = "white", width = 45, padx = 5) # add new answer
    resultLabel.grid(column = 1, row = 0)    
        


# Entry Boxes
frame1 = tk.Frame(master = window, width = 100, height = 100, bg = "cyan", padx = 5, pady = 10)
label1 = tk.Label(frame1, text = "Number 1:", bg = "cyan")
entrynum1 = tk.Entry(frame1, fg="black", bg="white", width=100)
frame1.pack(anchor = "n")
label1.pack(side=tk.LEFT)
entrynum1.pack(side=tk.RIGHT)

frame2 = tk.Frame(master = window, width = 100, height = 100, bg = "cyan", padx = 5, pady = 10)
label2 = tk.Label(frame2, text = "Number 2:", bg = "cyan")
entrynum2 = tk.Entry(frame2, fg="black", bg="white", width=100)
frame2.pack(anchor = "n")
label2.pack(side=tk.LEFT)
entrynum2.pack(side=tk.RIGHT)




# Choice Buttons
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
