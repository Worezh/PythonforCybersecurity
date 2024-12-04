# third tkinter script
# Get people in space
# Create by 

# Import tkinter
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests

# Functions
class PeopleInSpaces(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("People in Space")
    self.geometry("1000x700")
    self.iconbitmap(r'C:\Users\Rexh\Desktop\Main Art\Art\4chins\LISTENTOTHISGUY.ico')

    # Load the image
    image = Image.open(r'C:\Users\Rexh\Desktop\Main Art\Art\4chins\Reaction\2-General\dap 1.png')
    photo = ImageTk.PhotoImage(image)

    # Create a label with the image
    label = tk.Label(self, image=photo)
    label.image = photo  # Keep a reference to the image
    label.pack()

    # Create button
    self.label = tk.Button(self, text="People in Space", command=self.get_people_in_space)
    self.label.pack()

  def get_people_in_space(self):
    request_uri = "http://api.open-notify.org/astros.json"   
    response = requests.get(request_uri)
    items = response.json()
    message = f"Number of people in space: {items['number']}"
    messagebox.showinfo("People in Space", message)

# Create the GUI main window
window = PeopleInSpaces()

# Enter the main event loop
window.mainloop()