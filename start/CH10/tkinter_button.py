# Seconder tkinter script
# Add a button and command
# Create By sak

# Import tkinter
import tkinter

# Functions
def button_clicked():
  tkinter.Label(window, text = "Button was clicked").pack()

# Create the GUI main window
window = tkinter.Tk()

# Add widgets
label = tkinter.Label(window, text = "Hello World", font = ("Arial Bold", 50))
label.pack()
button = tkinter.Button(window, text = "Click Here", command = button_clicked)
button.pack()

# Enter the main event loop
window.mainloop()