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

print("Resoluções disponiveis: \n")

# lista todas as resoluções disponíveis 
if(options.filter(res="240p", file_extension='mp4')):
    print("MP4/240p")
if(options.filter(res="360p", file_extension='mp4')):
    print("MP4/360p")
if(options.filter(res="480p", file_extension='mp4')):
    print("MP4/480p")
if(options.filter(res="720p", file_extension='mp4')):
    print("MP4/720p")
if(options.filter(res="1080p", file_extension='mp4')):
    print("MP4/1080p")
if(options.filter(only_audio=True)):
    print("MP3/Audio")

resolution = input("\nSelecione a opção desejada: ")

# Valida a opção escolhida pelo usuário
def validate(option):
    if(option == "MP4/240p"):
        return options.filter(res="240p", file_extension='mp4').first()
    elif(option == "MP4/360p"):
        return options.filter(res="360p", file_extension='mp4').first()
    elif(option == "MP4/480p"):
        return options.filter(res="480p", file_extension='mp4').first()
    elif(option == "MP4/720p"):
        return options.filter(res="720p", file_extension='mp4').first()
    elif(option == "MP4/1080p"):
        return options.filter(res="1080p", file_extension='mp4').first()
    elif(option == "MP3/Audio"):
        return options.filter(only_audio=True).first()
    else:
        return 1

my_video = validate(resolution)

if(my_video == 1):
    print("Opção inválida!")
else:
    print("Baixando...")
    # faz o download do vídeo ou música
    my_video.download()
    print("\ndownload concluído!")
    # Pega o diretório atual do script
    cwd = os.getcwd()
    print(f"Seu arquivo foi armazenado no diretório: {cwd}")
