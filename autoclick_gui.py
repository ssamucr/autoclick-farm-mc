import tkinter as tk
from tkinter import ttk, messagebox
import pyautogui
import random
import time
import threading
import sys

class AutoClickerGUI:
    def __init__(self):
        self.running = False
        self.total_duration = 30 * 60  # 30 minutos por defecto
        self.start_time = None
        self.click_count = 0
        self.thread = None
        
        # Crear la ventana principal
        self.root = tk.Tk()
        self.root.title("🖱️ AutoClicker Ssamucr")
        self.root.geometry("520x780")
        self.root.resizable(False, False)
        
        # Configurar pyautogui
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.01
        
        self.create_widgets()
        
    def create_widgets(self):
        """Crea todos los widgets de la interfaz"""
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Título
        title_label = ttk.Label(main_frame, text="🖱️ AutoClicker Ssamucr", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Configuración de duración
        duration_frame = ttk.LabelFrame(main_frame, text="⏱️ Configuración de Tiempo", padding="10")
        duration_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Label(duration_frame, text="Duración (minutos):").grid(row=0, column=0, sticky=tk.W)
        self.duration_var = tk.StringVar(value="30")
        duration_entry = ttk.Entry(duration_frame, textvariable=self.duration_var, width=10)
        duration_entry.grid(row=0, column=1, padx=(10, 0))
        
        # Posición del mouse
        position_frame = ttk.LabelFrame(main_frame, text="📍 Posición del Mouse", padding="10")
        position_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.position_label = ttk.Label(position_frame, text="Posición actual: Obteniendo...")
        self.position_label.grid(row=0, column=0, sticky=tk.W)
        
        ttk.Button(position_frame, text="🔄 Actualizar Posición", 
                  command=self.update_position).grid(row=1, column=0, pady=(10, 0))
        
        # Configuración de acciones
        actions_frame = ttk.LabelFrame(main_frame, text="⚙️ Configuración de Acciones", padding="10")
        actions_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Label(actions_frame, text="✓ Clic izquierdo cada 1-2 segundos").grid(row=0, column=0, sticky=tk.W)
        ttk.Label(actions_frame, text="✓ Barra espaciadora cada 10 clics (500ms)").grid(row=1, column=0, sticky=tk.W)
        ttk.Label(actions_frame, text="✓ Clic derecho cada 10 clics (2s)").grid(row=2, column=0, sticky=tk.W)
        
        # Estado actual
        status_frame = ttk.LabelFrame(main_frame, text="📊 Estado Actual", padding="10")
        status_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.status_label = ttk.Label(status_frame, text="Estado: Detenido")
        self.status_label.grid(row=0, column=0, sticky=tk.W)
        
        self.clicks_label = ttk.Label(status_frame, text="Clics realizados: 0")
        self.clicks_label.grid(row=1, column=0, sticky=tk.W)
        
        self.time_label = ttk.Label(status_frame, text="Tiempo restante: --:--")
        self.time_label.grid(row=2, column=0, sticky=tk.W)
        
        # Barra de progreso
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(status_frame, variable=self.progress_var, maximum=100)
        self.progress_bar.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=(10, 0))
        
        # Botones de control
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=5, column=0, columnspan=2, pady=(20, 0))
        
        self.start_button = ttk.Button(buttons_frame, text="▶️ Iniciar AutoClicker", 
                                      command=self.start_clicking)
        self.start_button.grid(row=0, column=0, padx=(0, 10))
        
        self.stop_button = ttk.Button(buttons_frame, text="⏹️ Detener", 
                                     command=self.stop_clicking, state='disabled')
        self.stop_button.grid(row=0, column=1)
        
        # Información de seguridad
        safety_frame = ttk.LabelFrame(main_frame, text="⚠️ Información de Seguridad", padding="10")
        safety_frame.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(20, 0))
        
        safety_text = ("• Mueve el mouse a cualquier esquina para detener\n"
                      "• Asegúrate de estar en la app correcta antes de iniciar\n"
                      "• Usa el botón 'Detener' o cierra la ventana (X) para parar")
        
        ttk.Label(safety_frame, text=safety_text, justify=tk.LEFT, wraplength=480).grid(row=0, column=0)
        
        # Actualizar posición inicial
        self.update_position()
        
        # Configurar el cierre de ventana
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Manejar Alt+F4 y otras combinaciones de cierre
        self.root.bind('<Alt-F4>', lambda e: self.on_closing())
        self.root.focus_force()  # Asegurar que la ventana tenga foco para capturar eventos
        
    def update_position(self):
        """Actualiza la posición actual del mouse"""
        try:
            pos = pyautogui.position()
            self.position_label.config(text=f"Posición actual: {pos.x}, {pos.y}")
        except Exception as e:
            self.position_label.config(text="Error obteniendo posición")
            
    def start_clicking(self):
        """Inicia el proceso de clic automático"""
        if self.running:
            return
            
        try:
            duration_minutes = int(self.duration_var.get())
            if duration_minutes <= 0:
                raise ValueError("La duración debe ser mayor a 0")
            self.total_duration = duration_minutes * 60
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa una duración válida en minutos")
            return
        
        # Confirmar inicio
        result = messagebox.askyesno("Confirmar", 
                                   f"¿Iniciar AutoClicker por {duration_minutes} minutos?\n\n"
                                   f"Posición: {pyautogui.position()}\n"
                                   "Asegúrate de estar en la aplicación correcta.")
        
        if not result:
            return
        
        self.running = True
        self.start_time = time.time()
        self.click_count = 0
        
        # Actualizar interfaz
        self.start_button.config(state='disabled')
        self.stop_button.config(state='normal')
        self.status_label.config(text="Estado: ⏳ Iniciando en 3 segundos...")
        
        # Iniciar en un hilo separado
        self.thread = threading.Thread(target=self.clicking_loop, daemon=True)
        self.thread.start()
        
    def clicking_loop(self):
        """Loop principal del clic automático"""
        try:
            # Countdown
            for i in range(3, 0, -1):
                if not self.running:
                    return
                self.root.after(0, lambda i=i: self.status_label.config(text=f"Estado: ⏳ Iniciando en {i}..."))
                time.sleep(1)
            
            self.root.after(0, lambda: self.status_label.config(text="Estado: 🔄 Ejecutándose"))
            
            while self.running:
                # Verificar tiempo transcurrido
                elapsed_time = time.time() - self.start_time
                if elapsed_time >= self.total_duration:
                    self.root.after(0, self.clicking_completed)
                    break
                
                # Realizar clic izquierdo
                pyautogui.click()
                self.click_count += 1
                
                # Acciones especiales cada 10 clics
                if self.click_count % 10 == 0:
                    # Barra espaciadora por 500ms
                    pyautogui.keyDown('space')
                    time.sleep(0.5)
                    pyautogui.keyUp('space')
                    
                    # Clic derecho por 2 segundos
                    pyautogui.mouseDown(button='right')
                    time.sleep(2.0)
                    pyautogui.mouseUp(button='right')
                
                # Actualizar interfaz
                self.root.after(0, self.update_status)
                
                # Intervalo aleatorio
                if self.running:
                    interval = random.uniform(1.0, 2.0)
                    time.sleep(interval)
                    
        except pyautogui.FailSafeException:
            self.root.after(0, lambda: self.stop_clicking_with_message("🛑 Detenido por seguridad (mouse en esquina)"))
        except Exception as e:
            self.root.after(0, lambda: self.stop_clicking_with_message(f"❌ Error: {str(e)}"))
            
    def update_status(self):
        """Actualiza el estado en la interfaz"""
        if not self.running:
            return
            
        elapsed_time = time.time() - self.start_time
        remaining_time = max(0, self.total_duration - elapsed_time)
        
        minutes_left = int(remaining_time // 60)
        seconds_left = int(remaining_time % 60)
        
        # Actualizar labels
        self.clicks_label.config(text=f"Clics realizados: {self.click_count}")
        self.time_label.config(text=f"Tiempo restante: {minutes_left:02d}:{seconds_left:02d}")
        
        # Actualizar barra de progreso
        progress = (elapsed_time / self.total_duration) * 100
        self.progress_var.set(min(100, progress))
        
    def clicking_completed(self):
        """Se ejecuta cuando se completa el proceso"""
        self.stop_clicking()
        messagebox.showinfo("Completado", 
                          f"✅ AutoClicker completado!\n"
                          f"📊 Total de clics: {self.click_count}\n"
                          f"⏱️ Duración: {self.total_duration // 60} minutos")
        
    def stop_clicking(self):
        """Detiene el proceso de clic automático"""
        self.running = False
        
        # Esperar a que el hilo termine si está activo
        if hasattr(self, 'thread') and self.thread and self.thread.is_alive():
            try:
                self.thread.join(timeout=2.0)  # Esperar hasta 2 segundos
            except:
                pass
        
        # Actualizar interfaz
        self.start_button.config(state='normal')
        self.stop_button.config(state='disabled')
        self.status_label.config(text="Estado: ⏹️ Detenido")
        self.progress_var.set(0)
        
    def stop_clicking_with_message(self, message):
        """Detiene el proceso y muestra un mensaje"""
        self.stop_clicking()
        messagebox.showwarning("AutoClicker Detenido", message)
        
    def on_closing(self):
        """Maneja el cierre de la ventana"""
        if self.running:
            result = messagebox.askyesno("Confirmar", "¿Detener el AutoClicker y cerrar la aplicación?")
            if result:
                self.running = False
                if self.thread and self.thread.is_alive():
                    self.thread.join(timeout=1.0)  # Esperar hasta 1 segundo
                self.root.quit()
                self.root.destroy()
        else:
            self.root.quit()
            self.root.destroy()
    
    def run(self):
        """Ejecuta la aplicación"""
        self.root.mainloop()

def main():
    """Función principal"""
    try:
        app = AutoClickerGUI()
        app.run()
    except Exception as e:
        messagebox.showerror("Error Fatal", f"Error al iniciar la aplicación: {str(e)}")

if __name__ == "__main__":
    main()