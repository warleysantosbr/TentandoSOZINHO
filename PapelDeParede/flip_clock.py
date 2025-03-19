import tkinter as tk  # Biblioteca para criar interface gráfica
import time           # Biblioteca para capturar a hora atual

def update_time():
    """Atualiza o relógio com a hora atual"""
    current_time = time.strftime("%I:%M %p")  # Formata a hora (Ex: 06:30 PM)
    label.config(text=current_time)  # Atualiza o texto do relógio
    root.after(1000, update_time)  # Atualiza a cada 1 segundo

# Criando a janela principal
root = tk.Tk()  # Inicializa a janela Tkinter
root.title("Flip Clock")  # Nome da janela
root.geometry("600x300")  # Tamanho inicial (irá expandir para tela cheia)
root.configure(bg="black")  # Fundo preto para parecer um Flip Clock
root.attributes("-fullscreen", True)  # Define a janela como tela cheia
root.bind("<Escape>", lambda e: root.destroy())  # Pressionar ESC fecha o relógio

# Criar o rótulo do relógio
label = tk.Label(root, text="", font=("Arial", 120, "bold"), fg="white", bg="black")
label.pack(expand=True)  # Centraliza o relógio na tela

update_time()  # Inicia a atualização do relógio

root.mainloop()  # Mantém a janela aberta
