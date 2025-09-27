import pyautogui
import random
import time
import threading
import sys

class AutoClicker:
    def __init__(self):
        self.running = False
        self.total_duration = 8 * 60 * 60  # 8 horas en segundos
        self.start_time = None
        
    def start_clicking(self):
        """Inicia el proceso de clic automático"""
        self.running = True
        self.start_time = time.time()
        
        print("🖱️  AutoClicker iniciado!")
        print(f"⏱️  Duración: 30 minutos")
        print(f"📍 Posición actual del mouse: {pyautogui.position()}")
        print("⚠️  Mueve el mouse a las esquinas de la pantalla para detener de emergencia")
        print("⌨️  Se presionará la barra espaciadora cada 10 clics")
        print("🔄 Iniciando en 3 segundos...\n")
        
        # Countdown
        for i in range(3, 0, -1):
            print(f"Iniciando en {i}...")
            time.sleep(1)
        
        print("¡Comenzando!")
        
        click_count = 0
        
        try:
            while self.running:
                # Verificar si han pasado 30 minutos
                elapsed_time = time.time() - self.start_time
                if elapsed_time >= self.total_duration:
                    print(f"\n✅ ¡Completado! Se ejecutó durante 30 minutos.")
                    print(f"📊 Total de clics realizados: {click_count}")
                    break
                
                # Realizar clic izquierdo
                pyautogui.click()
                click_count += 1
                
                # Presionar barra espaciadora cada 10 clics
                if click_count % 10 == 0:
                    pyautogui.keyDown('space')
                    time.sleep(0.5)  # Mantener presionado por 500ms
                    pyautogui.keyUp('space')
                                      
                    # Mantener clic derecho durante 2 segundos
                    pyautogui.mouseDown(button='right')
                    time.sleep(2.0)  # Mantener presionado por 2 segundos
                    pyautogui.mouseUp(button='right')
                    
                    remaining_time = self.total_duration - elapsed_time
                    minutes_left = int(remaining_time // 60)
                    seconds_left = int(remaining_time % 60)
                    print(f"Clics: {click_count} | Espacio 500ms + Clic derecho 2s | Tiempo restante: {minutes_left}m {seconds_left}s")
                
                # Generar intervalo aleatorio entre 1 y 2 segundos
                interval = random.uniform(1.0, 2.0)
                time.sleep(interval)
                
        except pyautogui.FailSafeException:
            print("\n🛑 AutoClicker detenido por seguridad (mouse movido a esquina)")
            print(f"📊 Total de clics realizados: {click_count}")
            
        except KeyboardInterrupt:
            print(f"\n🛑 AutoClicker detenido por el usuario (Ctrl+C)")
            print(f"📊 Total de clics realizados: {click_count}")
            
        finally:
            self.running = False

def main():
    print("=" * 50)
    print("🖱️  AUTOCLICKER - CLIC AUTOMÁTICO")
    print("=" * 50)
    print()
    
    # Configurar pyautogui
    pyautogui.FAILSAFE = True  # Permite detener moviendo mouse a esquina
    pyautogui.PAUSE = 0.01     # Pausa mínima entre acciones
    
    autoclicker = AutoClicker()
    
    try:
        # Obtener posición actual del mouse
        current_pos = pyautogui.position()
        print(f"📍 El mouse está actualmente en: {current_pos}")
        print("⚡ Los clics se realizarán en la posición actual del mouse")
        print("⌨️  La barra espaciadora se presionará cada 10 clics")
        print()
        
        # Confirmar antes de iniciar
        response = input("¿Deseas continuar? (s/n): ").strip().lower()
        if response in ['s', 'si', 'sí', 'y', 'yes']:
            autoclicker.start_clicking()
        else:
            print("❌ Operación cancelada.")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        
    print("\n👋 ¡Hasta luego!")

if __name__ == "__main__":
    main()
