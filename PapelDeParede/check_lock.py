import psutil  # Biblioteca para monitorar processos do sistema
import time    # Biblioteca para adicionar pausas entre verificações
import subprocess  # Para rodar outro programa (o relógio)

def is_screen_locked():
    """Verifica se o Windows está bloqueado procurando pelo processo LogonUI.exe"""
    for process in psutil.process_iter(['name']):  # Percorre todos os processos em execução
        if process.info['name'] == 'LogonUI.exe':  # Se encontrar LogonUI.exe, o PC está bloqueado
            return True
    return False  # Se não encontrar, significa que o PC não está bloqueado

while True:
    if is_screen_locked():  # Se a tela estiver bloqueada...
        print("Tela bloqueada! Abrindo relógio...")
        subprocess.run(["python", "flip_clock.py"])  # Abre o relógio digital
    time.sleep(5)  # Espera 5 segundos antes de verificar novamente
