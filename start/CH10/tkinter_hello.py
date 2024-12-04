# First tkinter script
# Create by Sak

# Import tkinter
import tkinter

# Create the GUI main window
window = tkinter.Tk()

# Add widgets
label = tkinter.Label(
  window, 
  text = "Hello World", 
  font = ("Arial Bold", 25),
  fg = "white",
  bg = "black"
)
label.pack()

# Enter the main event loop
window.mainloop()