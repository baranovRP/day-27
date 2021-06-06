from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)

label = Label(text="Label", font=("Arial", 24, "bold"))
label.pack()

# label["text"] = "New test"
label.config(text="New text")


# Button
def button_clicked():
    print("clicked")
    new_text = input.get()
    label.config(text=new_text)


button = Button(text="Click", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()

window.mainloop()
