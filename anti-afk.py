import pyautogui
import random
import time
import sys

class MinecraftAntiAFK:
    def __init__(self):
        self.running = False
        self.total_duration = 60 * 60  # 1 hora por defecto
        self.start_time = None
        self.action_count = 0
        
    def move_forward(self, duration=0.5):
        """Mover hacia adelante por un tiempo determinado"""
        pyautogui.keyDown('w')
        time.sleep(duration)
        pyautogui.keyUp('w')
        
    def move_backward(self, duration=0.5):
        """Mover hacia atrás por un tiempo determinado"""
        pyautogui.keyDown('s')
        time.sleep(duration)
        pyautogui.keyUp('s')
        
    def move_left(self, duration=0.5):
        """Mover hacia la izquierda por un tiempo determinado"""
        pyautogui.keyDown('a')
        time.sleep(duration)
        pyautogui.keyUp('a')
        
    def move_right(self, duration=0.5):
        """Mover hacia la derecha por un tiempo determinado"""
        pyautogui.keyDown('d')
        time.sleep(duration)
        pyautogui.keyUp('d')
        
    def jump(self):
        """Saltar"""
        pyautogui.press('space')
        
    def attack(self):
        """Golpear/atacar"""
        pyautogui.click(button='left')
        
    def look_around(self):
        """Mover la cámara aleatoriamente"""
        # Movimiento aleatorio del mouse para simular mirar alrededor
        dx = random.randint(-50, 50)
        dy = random.randint(-30, 30)
        pyautogui.moveRel(dx, dy, duration=0.5)
        
    def perform_random_action(self):
        """Realiza una acción aleatoria de las disponibles"""
        actions = [
            # Movimientos básicos
            lambda: self.move_forward(random.uniform(0.3, 1.0)),
            lambda: self.move_backward(random.uniform(0.3, 0.8)),
            lambda: self.move_left(random.uniform(0.3, 0.8)),
            lambda: self.move_right(random.uniform(0.3, 0.8)),
            
            # Saltos
            self.jump,
            
            # Ataques ocasionales
            self.attack,
            
            # Mirar alrededor
            self.look_around,
            
            # Combinaciones más complejas
            lambda: self.complex_movement(),
        ]
        
        # Seleccionar acción aleatoria con pesos
        weights = [15, 10, 12, 12, 8, 5, 10, 8]  # Más probabilidad de movimientos básicos
        action = random.choices(actions, weights=weights)[0]
        action()
        
    def complex_movement(self):
        """Realiza una secuencia de movimientos más compleja"""
        sequences = [
            # Caminar y saltar
            lambda: (self.move_forward(0.8), self.jump()),
            # Moverse en L
            lambda: (self.move_forward(0.5), self.move_right(0.5)),
            # Retroceder y saltar
            lambda: (self.move_backward(0.3), self.jump()),
            # Círculo pequeño
            lambda: (self.move_forward(0.3), self.move_right(0.3), self.move_backward(0.3), self.move_left(0.3)),
        ]
        
        sequence = random.choice(sequences)
        sequence()
        
    def start_anti_afk(self):
        """Inicia el sistema anti-AFK"""
        self.running = True
        self.start_time = time.time()
        
        print("🎮 Minecraft Anti-AFK iniciado!")
        print(f"⏱️  Duración: {self.total_duration // 60} minutos")
        print("🎯 Acciones cada 1-2 minutos para evitar AFK")
        print("⚠️  Asegúrate de que Minecraft esté en primer plano")
        print("⚠️  Mueve el mouse a las esquinas para detener de emergencia")
        print("🔄 Iniciando en 5 segundos...\n")
        
        # Countdown
        for i in range(5, 0, -1):
            print(f"Iniciando en {i}...")
            time.sleep(1)
        
        print("¡Anti-AFK activo!\n")
        
        try:
            while self.running:
                # Verificar tiempo transcurrido
                elapsed_time = time.time() - self.start_time
                if elapsed_time >= self.total_duration:
                    print(f"\n✅ ¡Completado! Se ejecutó durante {self.total_duration // 60} minutos.")
                    print(f"📊 Total de acciones realizadas: {self.action_count}")
                    break
                
                # Realizar acción anti-AFK
                print(f"🎮 Realizando acción anti-AFK #{self.action_count + 1}...")
                self.perform_random_action()
                self.action_count += 1
                
                # Mostrar progreso
                remaining_time = self.total_duration - elapsed_time
                minutes_left = int(remaining_time // 60)
                seconds_left = int(remaining_time % 60)
                print(f"📊 Acciones: {self.action_count} | Tiempo restante: {minutes_left}m {seconds_left}s\n")
                
                # Espera aleatoria entre 1-2 minutos
                wait_time = random.uniform(60, 120)  # 1-2 minutos
                print(f"😴 Esperando {wait_time:.1f} segundos hasta la próxima acción...")
                
                # Espera en intervalos pequeños para poder interrumpir
                wait_intervals = int(wait_time / 5)  # Revisar cada 5 segundos
                for _ in range(wait_intervals):
                    if not self.running:
                        break
                    time.sleep(5)
                
                # Esperar el tiempo restante
                remaining_wait = wait_time % 5
                if remaining_wait > 0 and self.running:
                    time.sleep(remaining_wait)
                    
        except pyautogui.FailSafeException:
            print("\n🛑 Anti-AFK detenido por seguridad (mouse movido a esquina)")
            print(f"📊 Total de acciones realizadas: {self.action_count}")
            
        except KeyboardInterrupt:
            print(f"\n🛑 Anti-AFK detenido por el usuario (Ctrl+C)")
            print(f"📊 Total de acciones realizadas: {self.action_count}")
            
        finally:
            self.running = False

def main():
    print("=" * 60)
    print("🎮 MINECRAFT ANTI-AFK - EVITA SER ECHADO POR INACTIVIDAD")
    print("=" * 60)
    print()
    
    # Configurar pyautogui
    pyautogui.FAILSAFE = True  # Permite detener moviendo mouse a esquina
    pyautogui.PAUSE = 0.01     # Pausa mínima entre acciones
    
    anti_afk = MinecraftAntiAFK()
    
    try:
        print("🎯 Configuración:")
        print("   • Movimientos: W, A, S, D")
        print("   • Saltos: Barra espaciadora")
        print("   • Ataques: Clic izquierdo ocasional")
        print("   • Cámara: Movimiento aleatorio del mouse")
        print("   • Frecuencia: Cada 1-2 minutos")
        print()
        
        # Configurar duración
        try:
            duration_input = input("⏱️ ¿Cuántos minutos quieres que se ejecute? (predeterminado: 60): ").strip()
            if duration_input:
                duration_minutes = int(duration_input)
                anti_afk.total_duration = duration_minutes * 60
            else:
                print("⏱️ Usando duración predeterminada: 60 minutos")
        except ValueError:
            print("⚠️ Valor inválido, usando duración predeterminada: 60 minutos")
        
        print()
        print("⚠️ IMPORTANTE:")
        print("   • Asegúrate de que Minecraft esté abierto y en primer plano")
        print("   • El personaje debe estar en un lugar seguro")
        print("   • No uses este script en servidores donde esté prohibido")
        print()
        
        # Confirmar antes de iniciar
        response = input("¿Deseas continuar? (s/n): ").strip().lower()
        if response in ['s', 'si', 'sí', 'y', 'yes']:
            anti_afk.start_anti_afk()
        else:
            print("❌ Operación cancelada.")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        
    print("\n👋 ¡Hasta luego!")

if __name__ == "__main__":
    main()