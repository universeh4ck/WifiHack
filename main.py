import subprocess
import time

def open_google():
    subprocess.Popen(['termux-open', 'https://www.xvideos.com/video.hdfeiuha780/gostosa_da_buceta_carnuda_e_molhada_dando_o_cu_e_gemendo_alto'])

def main():
    try:
        while True:
            open_google()
            time.sleep(1)  # espera 20 segundos antes de abrir novamente
    except KeyboardInterrupt:
        print("\nEncerrando o script.")

if __name__ == "__main__":
    main()
