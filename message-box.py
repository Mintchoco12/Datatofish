#DataToFish: https://datatofish.com/message-box-python/

import tkinter as tk # Importeer de tkinter package
from tkinter import messagebox # Importeer de messagebox uit de tkinter package

root = tk.Tk() # Maakt een nieuwe instance van tk aan

canvas1 = tk.Canvas(root, width = 300, height = 300) # Maak een canvas met een bepaalde hoogte en breedte
canvas1.pack() # Organiseerd widgets in blokken voordat ze in de parent gaan

def ExitApplication():
    # Maakt een nieuwe messagebox aan met de volgende vraag
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')

    if MsgBox == 'yes': 
       root.destroy() # Sluit het applicatie
    else:
        tk.messagebox.showinfo('Return','You will now return to the application screen') # Laat een informatie box zien
        
# Maak een nieuwe knop aan die de volgende functie uitvoert als je erop klikt
button1 = tk.Button (root, text='Exit Application',command=ExitApplication,bg='brown',fg='white')

# Laat de knoop zien op de volgende positie
canvas1.create_window(150, 150, window=button1)
  
# Voer het bestand uit totdat het applicatie geen userinput meer verwacht
root.mainloop()