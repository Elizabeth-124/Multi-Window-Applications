import customtkinter as ctk
import tkinter.messagebox as messagebox

app=ctk.CTk()
ctk.set_appearance_mode("dark")
app.geometry("300x200")

def trigger_error():
    messagebox.showerror("Critical!!!","Action blocked: Cant delete system file!!")

btn=ctk.CTkButton(app,text="Delete System32",command=trigger_error)
btn.pack(padx=10,pady=10)

app.mainloop()

