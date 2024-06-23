import webbrowser
import time

def open_google():
    url = "https://xvideos.com/"
    webbrowser.open(url)

def main():
    try:
        while True:
            open_google()
            time.sleep(1)  # espera 20 segundos antes de abrir novamente
    except KeyboardInterrupt:
        print("\nEncerrando o script.")

if __name__ == "__main__":
    main()

