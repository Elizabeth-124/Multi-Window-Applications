import customtkinter as ctk

app=ctk.CTk()
app.geometry("500x500")
app.title("Main Window")

def open_settings():
    setting_window=ctk.CTkToplevel(app)
    setting_window.geometry("250x250")
    setting_window.title("Setting Window")
    setting_window.grab_set()

    ctk.CTkLabel(setting_window,text="Preferrence",font=("roboto",24,"bold")).pack(pady=12,padx=10)

    def toggle_mode():
        if mode_switch.get()==1:
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")
    mode_switch=ctk.CTkSwitch(setting_window,text="Dark Mode",command=toggle_mode)
    mode_switch.pack(pady=12,padx=10)

btn=ctk.CTkButton(app,text="Open Setting",command=open_settings)
btn.pack(pady=12,padx=10)

app.mainloop()
