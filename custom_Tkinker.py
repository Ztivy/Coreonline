import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("500x400")
app.title("Asistente de Voz")

# Título
title = ctk.CTkLabel(app, text="ASISTENTE PERSONAL", font=("Arial", 20, "bold"))
title.pack(pady=15)

# Estado
status = ctk.CTkLabel(app, text="Estado: Inactivo")
status.pack(pady=5)

# Área de texto
chat = ctk.CTkTextbox(app, width=450, height=200)
chat.pack(pady=15)

# Botones
frame = ctk.CTkFrame(app)
frame.pack(pady=10)

listen_btn = ctk.CTkButton(frame, text="🎤 Escuchar", width=150)
listen_btn.grid(row=0, column=0, padx=10)

exit_btn = ctk.CTkButton(frame, text="Salir", width=150)
exit_btn.grid(row=0, column=1, padx=10)

app.mainloop()
