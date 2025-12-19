import customtkinter as ctk
from tkinter import filedialog
import json
import os

# Documentación de CustomTkinter: https://customtkinter.tomschimansky.com/documentation/

class ConfiguracionFrame(ctk.CTkFrame):
    """Frame para configuración general del asistente"""
    def __init__(self, master, app_instance, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.app = app_instance
        
        # Título de la sección
        titulo = ctk.CTkLabel(
            self, 
            text="⚙️ Configuración General", 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        titulo.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 30), sticky="w")
        
        # Nombre del asistente
        label_asistente = ctk.CTkLabel(
            self, 
            text="Nombre del Asistente:", 
            font=ctk.CTkFont(size=14)
        )
        label_asistente.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        
        self.entry_asistente = ctk.CTkEntry(
            self, 
            placeholder_text="Ej: Jarvis, Alexa, Coreonline",
            width=300
        )
        self.entry_asistente.grid(row=1, column=1, padx=20, pady=10, sticky="w")
        
        # Nombre del usuario
        label_usuario = ctk.CTkLabel(
            self, 
            text="¿Cómo llamar al usuario?:", 
            font=ctk.CTkFont(size=14)
        )
        label_usuario.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        
        self.entry_usuario = ctk.CTkEntry(
            self, 
            placeholder_text="Ej: Jefe, Señor, tu nombre",
            width=300
        )
        self.entry_usuario.grid(row=2, column=1, padx=20, pady=10, sticky="w")
        
        # Ruta para notas
        label_notas = ctk.CTkLabel(
            self, 
            text="Carpeta para Notas:", 
            font=ctk.CTkFont(size=14)
        )
        label_notas.grid(row=3, column=0, padx=20, pady=10, sticky="w")
        
        frame_notas = ctk.CTkFrame(self, fg_color="transparent")
        frame_notas.grid(row=3, column=1, padx=20, pady=10, sticky="w")
        
        self.entry_notas = ctk.CTkEntry(
            frame_notas, 
            placeholder_text="Selecciona una carpeta",
            width=250
        )
        self.entry_notas.grid(row=0, column=0, padx=(0, 10))
        
        btn_notas = ctk.CTkButton(
            frame_notas, 
            text="📁", 
            width=40,
            command=self.seleccionar_carpeta_notas
        )
        btn_notas.grid(row=0, column=1)
        
        # Ruta para tareas
        label_tareas = ctk.CTkLabel(
            self, 
            text="Carpeta para Tareas:", 
            font=ctk.CTkFont(size=14)
        )
        label_tareas.grid(row=4, column=0, padx=20, pady=10, sticky="w")
        
        frame_tareas = ctk.CTkFrame(self, fg_color="transparent")
        frame_tareas.grid(row=4, column=1, padx=20, pady=10, sticky="w")
        
        self.entry_tareas = ctk.CTkEntry(
            frame_tareas, 
            placeholder_text="Selecciona una carpeta",
            width=250
        )
        self.entry_tareas.grid(row=0, column=0, padx=(0, 10))
        
        btn_tareas = ctk.CTkButton(
            frame_tareas, 
            text="📁", 
            width=40,
            command=self.seleccionar_carpeta_tareas
        )
        btn_tareas.grid(row=0, column=1)
        
        # Botón guardar
        btn_guardar = ctk.CTkButton(
            self, 
            text="💾 Guardar Configuración",
            command=self.guardar_configuracion,
            height=40,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        btn_guardar.grid(row=5, column=0, columnspan=2, padx=20, pady=30)
    
    def seleccionar_carpeta_notas(self):
        carpeta = filedialog.askdirectory(title="Seleccionar carpeta para Notas")
        if carpeta:
            self.entry_notas.delete(0, 'end')
            self.entry_notas.insert(0, carpeta)
    
    def seleccionar_carpeta_tareas(self):
        carpeta = filedialog.askdirectory(title="Seleccionar carpeta para Tareas")
        if carpeta:
            self.entry_tareas.delete(0, 'end')
            self.entry_tareas.insert(0, carpeta)
    
    def guardar_configuracion(self):
        config = {
            "nombre_asistente": self.entry_asistente.get(),
            "nombre_usuario": self.entry_usuario.get(),
            "ruta_notas": self.entry_notas.get(),
            "ruta_tareas": self.entry_tareas.get()
        }
        self.app.guardar_config(config)
        self.app.mostrar_mensaje("✅ Configuración guardada exitosamente")
    
    def cargar_valores(self, config):
        """Carga los valores guardados en los campos"""
        self.entry_asistente.delete(0, 'end')
        self.entry_asistente.insert(0, config.get("nombre_asistente", ""))
        
        self.entry_usuario.delete(0, 'end')
        self.entry_usuario.insert(0, config.get("nombre_usuario", ""))
        
        self.entry_notas.delete(0, 'end')
        self.entry_notas.insert(0, config.get("ruta_notas", ""))
        
        self.entry_tareas.delete(0, 'end')
        self.entry_tareas.insert(0, config.get("ruta_tareas", ""))


class VozFrame(ctk.CTkFrame):
    """Frame para configuración de voz"""
    def __init__(self, master, app_instance, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.app = app_instance
        
        # Título de la sección
        titulo = ctk.CTkLabel(
            self, 
            text="🎤 Configuración de Voz", 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        titulo.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 30), sticky="w")
        
        # Selector de voz
        label_voz = ctk.CTkLabel(
            self, 
            text="Tipo de Voz:", 
            font=ctk.CTkFont(size=14)
        )
        label_voz.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        
        self.combo_voz = ctk.CTkComboBox(
            self,
            values=["Masculina - Grave", "Masculina - Normal", "Femenina - Normal", "Femenina - Aguda"],
            width=300,
            state="readonly"
        )
        self.combo_voz.grid(row=1, column=1, padx=20, pady=10, sticky="w")
        
        # Velocidad de voz
        label_velocidad = ctk.CTkLabel(
            self, 
            text="Velocidad de Habla:", 
            font=ctk.CTkFont(size=14)
        )
        label_velocidad.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        
        frame_velocidad = ctk.CTkFrame(self, fg_color="transparent")
        frame_velocidad.grid(row=2, column=1, padx=20, pady=10, sticky="w")
        
        self.slider_velocidad = ctk.CTkSlider(
            frame_velocidad,
            from_=0.5,
            to=2.0,
            number_of_steps=15,
            width=200
        )
        self.slider_velocidad.set(1.0)
        self.slider_velocidad.grid(row=0, column=0, padx=(0, 10))
        
        self.label_valor_velocidad = ctk.CTkLabel(
            frame_velocidad,
            text="1.0x",
            width=50
        )
        self.label_valor_velocidad.grid(row=0, column=1)
        
        self.slider_velocidad.configure(command=self.actualizar_velocidad)
        
        # Volumen
        label_volumen = ctk.CTkLabel(
            self, 
            text="Volumen:", 
            font=ctk.CTkFont(size=14)
        )
        label_volumen.grid(row=3, column=0, padx=20, pady=10, sticky="w")
        
        frame_volumen = ctk.CTkFrame(self, fg_color="transparent")
        frame_volumen.grid(row=3, column=1, padx=20, pady=10, sticky="w")
        
        self.slider_volumen = ctk.CTkSlider(
            frame_volumen,
            from_=0,
            to=100,
            number_of_steps=20,
            width=200
        )
        self.slider_volumen.set(80)
        self.slider_volumen.grid(row=0, column=0, padx=(0, 10))
        
        self.label_valor_volumen = ctk.CTkLabel(
            frame_volumen,
            text="80%",
            width=50
        )
        self.label_valor_volumen.grid(row=0, column=1)
        
        self.slider_volumen.configure(command=self.actualizar_volumen)
        
        # Motor de voz
        label_motor = ctk.CTkLabel(
            self, 
            text="Motor de Síntesis:", 
            font=ctk.CTkFont(size=14)
        )
        label_motor.grid(row=4, column=0, padx=20, pady=10, sticky="w")
        
        self.combo_motor = ctk.CTkComboBox(
            self,
            values=["pyttsx3 (Offline)", "gTTS (Google)", "Azure TTS", "Amazon Polly"],
            width=300,
            state="readonly"
        )
        self.combo_motor.grid(row=4, column=1, padx=20, pady=10, sticky="w")
        
        # Botón probar voz
        btn_probar = ctk.CTkButton(
            self, 
            text="🔊 Probar Voz",
            command=self.probar_voz,
            height=35
        )
        btn_probar.grid(row=5, column=0, columnspan=2, padx=20, pady=20)
        
        # Botón guardar
        btn_guardar = ctk.CTkButton(
            self, 
            text="💾 Guardar Configuración de Voz",
            command=self.guardar_configuracion_voz,
            height=40,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        btn_guardar.grid(row=6, column=0, columnspan=2, padx=20, pady=10)
    
    def actualizar_velocidad(self, value):
        self.label_valor_velocidad.configure(text=f"{value:.1f}x")
    
    def actualizar_volumen(self, value):
        self.label_valor_volumen.configure(text=f"{int(value)}%")
    
    def probar_voz(self):
        self.app.mostrar_mensaje("🔊 Reproduciendo voz de prueba...")
        # Aquí iría el código para probar la voz
    
    def guardar_configuracion_voz(self):
        config_voz = {
            "tipo_voz": self.combo_voz.get(),
            "velocidad": self.slider_velocidad.get(),
            "volumen": self.slider_volumen.get(),
            "motor": self.combo_motor.get()
        }
        self.app.guardar_config_voz(config_voz)
        self.app.mostrar_mensaje("✅ Configuración de voz guardada")
    
    def cargar_valores(self, config):
        """Carga los valores guardados"""
        self.combo_voz.set(config.get("tipo_voz", "Masculina - Normal"))
        self.slider_velocidad.set(config.get("velocidad", 1.0))
        self.actualizar_velocidad(config.get("velocidad", 1.0))
        self.slider_volumen.set(config.get("volumen", 80))
        self.actualizar_volumen(config.get("volumen", 80))
        self.combo_motor.set(config.get("motor", "pyttsx3 (Offline)"))


class AparienciaFrame(ctk.CTkFrame):
    """Frame para configuración de apariencia"""
    def __init__(self, master, app_instance, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.app = app_instance
        
        # Título de la sección
        titulo = ctk.CTkLabel(
            self, 
            text="🎨 Configuración de Apariencia", 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        titulo.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 30), sticky="w")
        
        # Tema de color
        label_tema = ctk.CTkLabel(
            self, 
            text="Tema:", 
            font=ctk.CTkFont(size=14)
        )
        label_tema.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        
        frame_tema = ctk.CTkFrame(self, fg_color="transparent")
        frame_tema.grid(row=1, column=1, padx=20, pady=10, sticky="w")
        
        self.radio_var_tema = ctk.StringVar(value="light")
        
        radio_claro = ctk.CTkRadioButton(
            frame_tema,
            text="☀️ Claro",
            variable=self.radio_var_tema,
            value="light",
            command=self.cambiar_tema
        )
        radio_claro.grid(row=0, column=0, padx=10)
        
        radio_oscuro = ctk.CTkRadioButton(
            frame_tema,
            text="🌙 Oscuro",
            variable=self.radio_var_tema,
            value="dark",
            command=self.cambiar_tema
        )
        radio_oscuro.grid(row=0, column=1, padx=10)
        
        # Esquema de color
        label_color = ctk.CTkLabel(
            self, 
            text="Esquema de Color:", 
            font=ctk.CTkFont(size=14)
        )
        label_color.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        
        self.combo_color = ctk.CTkComboBox(
            self,
            values=["blue", "green", "dark-blue"],
            width=200,
            state="readonly"
        )
        self.combo_color.grid(row=2, column=1, padx=20, pady=10, sticky="w")
        
        # Tamaño de fuente
        label_fuente = ctk.CTkLabel(
            self, 
            text="Tamaño de Fuente:", 
            font=ctk.CTkFont(size=14)
        )
        label_fuente.grid(row=3, column=0, padx=20, pady=10, sticky="w")
        
        frame_fuente = ctk.CTkFrame(self, fg_color="transparent")
        frame_fuente.grid(row=3, column=1, padx=20, pady=10, sticky="w")
        
        self.slider_fuente = ctk.CTkSlider(
            frame_fuente,
            from_=10,
            to=18,
            number_of_steps=8,
            width=200
        )
        self.slider_fuente.set(14)
        self.slider_fuente.grid(row=0, column=0, padx=(0, 10))
        
        self.label_valor_fuente = ctk.CTkLabel(
            frame_fuente,
            text="14pt",
            width=50
        )
        self.label_valor_fuente.grid(row=0, column=1)
        
        self.slider_fuente.configure(command=self.actualizar_fuente)
        
        # Información del tema actual
        self.info_tema = ctk.CTkLabel(
            self,
            text="Tema actual: Claro",
            font=ctk.CTkFont(size=12),
            text_color="gray"
        )
        self.info_tema.grid(row=4, column=0, columnspan=2, padx=20, pady=20)
        
        # Botón guardar
        btn_guardar = ctk.CTkButton(
            self, 
            text="💾 Guardar Configuración de Apariencia",
            command=self.guardar_configuracion_apariencia,
            height=40,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        btn_guardar.grid(row=5, column=0, columnspan=2, padx=20, pady=10)
    
    def cambiar_tema(self):
        tema = self.radio_var_tema.get()
        ctk.set_appearance_mode(tema)
        texto_tema = "Claro" if tema == "light" else "Oscuro"
        self.info_tema.configure(text=f"Tema actual: {texto_tema}")
        self.app.mostrar_mensaje(f"🎨 Tema cambiado a {texto_tema}")
    
    def actualizar_fuente(self, value):
        self.label_valor_fuente.configure(text=f"{int(value)}pt")
    
    def guardar_configuracion_apariencia(self):
        config_apariencia = {
            "tema": self.radio_var_tema.get(),
            "esquema_color": self.combo_color.get(),
            "tamaño_fuente": self.slider_fuente.get()
        }
        self.app.guardar_config_apariencia(config_apariencia)
        self.app.mostrar_mensaje("✅ Configuración guardada. El esquema de color se aplicará al reiniciar")
    
    def cargar_valores(self, config):
        """Carga los valores guardados"""
        tema = config.get("tema", "light")
        self.radio_var_tema.set(tema)
        ctk.set_appearance_mode(tema)
        texto_tema = "Claro" if tema == "light" else "Oscuro"
        self.info_tema.configure(text=f"Tema actual: {texto_tema}")
        
        self.combo_color.set(config.get("esquema_color", "blue"))
        self.slider_fuente.set(config.get("tamaño_fuente", 14))
        self.actualizar_fuente(config.get("tamaño_fuente", 14))


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuración inicial
        # Cargar configuración existente primero
        self.config_file = "config_asistente.json"
        self.config = self.cargar_configuracion()
        
        # Aplicar configuración de apariencia si existe
        if "apariencia" in self.config:
            tema = self.config["apariencia"].get("tema", "light")
            esquema = self.config["apariencia"].get("esquema_color", "blue")
            ctk.set_appearance_mode(tema)
            ctk.set_default_color_theme(esquema)
        else:
            ctk.set_appearance_mode("light")
            ctk.set_default_color_theme("blue")
        
        self.geometry("900x700")
        self.title("Coreonline - Asistente Virtual")
        
        # Archivo de configuración ya cargado arriba
        
        # Frame principal con barra lateral
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Barra lateral
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(5, weight=1)
        
        # Logo/Título
        self.logo_label = ctk.CTkLabel(
            self.sidebar, 
            text="Coreonline", 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.subtitle_label = ctk.CTkLabel(
            self.sidebar, 
            text="Asistente Virtual", 
            font=ctk.CTkFont(size=12)
        )
        self.subtitle_label.grid(row=1, column=0, padx=20, pady=(0, 20))
        
        # Botones de navegación
        self.btn_general = ctk.CTkButton(
            self.sidebar,
            text="⚙️ General",
            command=lambda: self.mostrar_frame("general"),
            height=40
        )
        self.btn_general.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        
        self.btn_voz = ctk.CTkButton(
            self.sidebar,
            text="🎤 Voz",
            command=lambda: self.mostrar_frame("voz"),
            height=40
        )
        self.btn_voz.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        
        self.btn_apariencia = ctk.CTkButton(
            self.sidebar,
            text="🎨 Apariencia",
            command=lambda: self.mostrar_frame("apariencia"),
            height=40
        )
        self.btn_apariencia.grid(row=4, column=0, padx=20, pady=10, sticky="ew")
        
        # Frame de contenido
        self.content_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.content_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
        # Label para mensajes
        self.mensaje_label = ctk.CTkLabel(
            self.content_frame,
            text="",
            font=ctk.CTkFont(size=12),
            text_color="green"
        )
        self.mensaje_label.grid(row=0, column=0, pady=(0, 10), sticky="ew")
        
        # Crear frames
        self.frames = {}
        self.crear_frames()
        
        # Mostrar frame inicial
        self.mostrar_frame("general")
    
    def crear_frames(self):
        """Crea todos los frames de configuración"""
        self.frames["general"] = ConfiguracionFrame(self.content_frame, self)
        self.frames["voz"] = VozFrame(self.content_frame, self)
        self.frames["apariencia"] = AparienciaFrame(self.content_frame, self)
        
        # Cargar valores guardados en cada frame
        if "general" in self.config:
            self.frames["general"].cargar_valores(self.config["general"])
        if "voz" in self.config:
            self.frames["voz"].cargar_valores(self.config["voz"])
        if "apariencia" in self.config:
            self.frames["apariencia"].cargar_valores(self.config["apariencia"])
    
    def mostrar_frame(self, nombre):
        """Muestra el frame seleccionado y oculta los demás"""
        for frame in self.frames.values():
            frame.grid_forget()
        
        self.frames[nombre].grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.mensaje_label.configure(text="")
    
    def cargar_configuracion(self):
        """Carga la configuración desde el archivo JSON"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def guardar_config(self, config):
        """Guarda la configuración general"""
        if "general" not in self.config:
            self.config["general"] = {}
        self.config["general"].update(config)
        self.guardar_archivo_config()
    
    def guardar_config_voz(self, config):
        """Guarda la configuración de voz"""
        if "voz" not in self.config:
            self.config["voz"] = {}
        self.config["voz"].update(config)
        self.guardar_archivo_config()
    
    def guardar_config_apariencia(self, config):
        """Guarda la configuración de apariencia"""
        if "apariencia" not in self.config:
            self.config["apariencia"] = {}
        self.config["apariencia"].update(config)
        self.guardar_archivo_config()
    
    def guardar_archivo_config(self):
        """Guarda el archivo de configuración completo"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error al guardar configuración: {e}")
    
    def mostrar_mensaje(self, mensaje):
        """Muestra un mensaje temporal en la interfaz"""
        self.mensaje_label.configure(text=mensaje)
        self.after(3000, lambda: self.mensaje_label.configure(text=""))


if __name__ == "__main__":
    app = App()
    app.mainloop()