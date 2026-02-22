import customtkinter as ctk
import tkinter.messagebox as messagebox
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app=ctk.CTk()
app.geometry("500x500")
app.title("Exit Check")

def trigger_error():
    response=messagebox.askyesno("Confirm","Are you sure you want to log out?")

    if response == True:
        app.destroy()
    else:
        pass

btn=ctk.CTkButton(app,text="Log Out",command=trigger_error)
btn.pack(pady=12,padx=10)

app.mainloop()