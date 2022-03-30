from pytube import YouTube
import os 

print("        ____        _                     _                 _           ")
print("  _   _|___ \    __| | _____      ___ __ | | ___   __ _  __| | ___ _ __ ")
print(" | | | | __) |  / _` |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|")
print(" | |_| |/ __/  | (_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   ")
print("  \__, |_____|  \__,_|\___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   ")
print("  |___/ \n")

url = input("Insira a URL do vídeo que deseja baixar: ")
ytb = YouTube(url)
options = ytb.streams

print("Resoluções disponiveis: ")

# lista todas as resoluções disponíveis 

if(options.filter(res="240p", file_extension='mp4')):
    print("240p")
if(options.filter(res="360p", file_extension='mp4')):
    print("360p")
if(options.filter(res="480p", file_extension='mp4')):
    print("480p")
if(options.filter(res="720p", file_extension='mp4')):
    print("720p")
if(options.filter(res="1080p", file_extension='mp4')):
    print("1080p")

resolution = input("\nescolha a resolução desejada: ")
# Verifica se a opção escolhida está disponível
if(not(options.filter(res=resolution, file_extension='mp4'))):
    print("Essa resolução não existe, opção inválida!")
else:
    print("baixando...");
    # faz o download do vídeo
    my_video = options.filter(res=resolution, file_extension='mp4').first().download()
    print("\ndownload concluído!")
    # Pega o diretório atual do script
    cwd = os.getcwd()
    print(f"Seu vídeo foi armazenado no diretório: {cwd}")