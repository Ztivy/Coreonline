import customtkinter as ctk

# Documentación de CustomTkinter: https://customtkinter.tomschimansky.com/documentation/

class Frame(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master,fg_color="transparent" ,**kwargs)

        self.label = ctk.CTkLabel(self, text="Hello, CustomTkinter!")
        self.label.grid(row=0, column=0, padx=20, pady=20)

        self.button = ctk.CTkButton(self, text="Click Me")
        self.button.grid(row=1, column=0, padx=20, pady=20)

class App(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        self.geometry("1800x500")
        self.title("Coronline")

        self.frame = Frame(master=self)
        self.frame.pack(padx=10, pady=20)
        

app = App()
app.mainloop()