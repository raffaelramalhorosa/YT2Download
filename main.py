import os
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from pytube import YouTube

def baixar_video():
    url = entry_url.get()
    pasta_destino = entry_pasta.get()
    opcao = var_opcao.get()

    if not url or not pasta_destino:
        messagebox.showerror("Erro", "Preencha o link e a pasta de destino!")
        return

    # Verifica se a pasta existe, senão cria
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    try:
        yt = YouTube(url)
        titulo = yt.title.replace(" ", "_").replace("/", "")  # Limpa o título para nome de arquivo

        if opcao == '1':  # MP3 (áudio)
            stream = yt.streams.filter(only_audio=True).first()
            arquivo_saida = os.path.join(pasta_destino, f"{titulo}.mp3")
            stream.download(output_path=pasta_destino, filename=f"{titulo}.mp3")
            messagebox.showinfo("Sucesso", f"Áudio baixado como MP3 em: {arquivo_saida}")

        elif opcao == '2':  # MP4 720p
            stream = yt.streams.filter(res="720p", file_extension="mp4").first()
            if stream:
                arquivo_saida = os.path.join(pasta_destino, f"{titulo}_720p.mp4")
                stream.download(output_path=pasta_destino, filename=f"{titulo}_720p.mp4")
                messagebox.showinfo("Sucesso", f"Vídeo baixado em 720p em: {arquivo_saida}")
            else:
                messagebox.showerror("Erro", "Resolução 720p não disponível para este vídeo.")

        elif opcao == '3':  # MP4 1080p
            stream = yt.streams.filter(res="1080p", file_extension="mp4").first()
            if stream:
                arquivo_saida = os.path.join(pasta_destino, f"{titulo}_1080p.mp4")
                stream.download(output_path=pasta_destino, filename=f"{titulo}_1080p.mp4")
                messagebox.showinfo("Sucesso", f"Vídeo baixado em 1080p em: {arquivo_saida}")
            else:
                messagebox.showerror("Erro", "Resolução 1080p não disponível para este vídeo.")

        elif opcao == '4':  # MP4 4K (2160p)
            stream = yt.streams.filter(res="2160p", file_extension="mp4").first()
            if stream:
                arquivo_saida = os.path.join(pasta_destino, f"{titulo}_4K.mp4")
                stream.download(output_path=pasta_destino, filename=f"{titulo}_4K.mp4")
                messagebox.showinfo("Sucesso", f"Vídeo baixado em 4K em: {arquivo_saida}")
            else:
                messagebox.showerror("Erro", "Resolução 4K não disponível para este vídeo.")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

def selecionar_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        entry_pasta.delete(0, tk.END)
        entry_pasta.insert(0, pasta)

# Configuração da janela GUI
root = tk.Tk()
root.title("Ferramenta de Download do YouTube")
root.geometry("500x500")
root.configure(bg="#ffffff") # Cor de fundo

# Label e Entry para URL
tk.Label(root, text="Link do vídeo do YouTube:").pack(pady=5)
entry_url = tk.Entry(root, width=50)
entry_url.pack()

# Label e Entry para Pasta com botão de seleção
tk.Label(root, text="Pasta de destino:").pack(pady=5)
entry_pasta = tk.Entry(root, width=50)
entry_pasta.pack()
btn_selecionar = tk.Button(root, text="Selecionar Pasta", command=selecionar_pasta)
btn_selecionar.pack(pady=5)

# Opções de formato
tk.Label(root, text="Escolha o formato:").pack(pady=5)
var_opcao = tk.StringVar(value='1')
tk.Radiobutton(root, text="MP3 (áudio apenas)", variable=var_opcao, value='1').pack(anchor=tk.W)
tk.Radiobutton(root, text="MP4 720p", variable=var_opcao, value='2').pack(anchor=tk.W)
tk.Radiobutton(root, text="MP4 1080p", variable=var_opcao, value='3').pack(anchor=tk.W)
tk.Radiobutton(root, text="MP4 4K", variable=var_opcao, value='4').pack(anchor=tk.W)

# Botão de download
btn_baixar = ttk.Button(root, text="Baixar", command=baixar_video)
btn_baixar.pack(pady=20)

root.mainloop()