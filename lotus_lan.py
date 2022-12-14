import whois
import os
import clienttcp
from socket import *
import socket


from platform import system as ok

def main():
    on = True
    os.system('clear')
    while on == True:
        menu =input("== Scanner de rede ==\nOpções:\n1- Escanear range de IP\n2- Verificar dados de host específico(apenas ping por enquanto)\n3- Teste de vulnerabilidade Nmap em host específico (ainda não funcional)\n4- Whois\n5- Client TCP\n6- Meu IP\n7- Alterar IP\n8- Varrer portas abertas do IP\n0- SAIR\n")
        match menu: #switch de opções
            case '1':
                scanner()
            case '2':
                verificar_host_especifico()
            case '3':
                teste_de_vulnerabilidade_nmap()
            case '4':
                acionar_whois()
            case '5':
                clienttcp.client() #função externa importada
            case '6':
                print(meuip())
            case '7':
                alteraip()
            case '8':
                varrer_portas_abertas()
            case '0':
                on = False
                return 0
             

def scanner(): # Opção 1
    print("scanner")    
    
    os.system('clear')
    lista_ips=[]
    ip_inicial= input("Insira o IP inicial: ")
    ip = ip_inicial.split('.') # Transforma a string em uma lista dividida pelo ponto
    index = int(input("Qual o range de IP? "))
    print ('Testando...')
    for i in range(1,index): # loop em quantos ips eu vou varrer, iniciando pelo 1
        ip[3] = str(i) # mudar a ultima parte do ip para o numero como string
        ip_formatado = '.'.join(ip) # criar o texto que representa o ip
        
        rs = os.system('ping -c 1 {}'.format(ip_formatado)) # executar o comando com o ip certo
        if rs == 0:
            print ('O {} ta on'.format(ip_formatado))
            
            lista_ips.append(ip_formatado) #insere o ip formatado online no fim da lista
    print("São ",len(lista_ips)," ips online no range de ",index)
    print(lista_ips)



def verificar_host_especifico(): #opção 2
    
    ip_insert= input("Insira o IP ou HOST ")
    ip=ip_insert.split(".")
    ip_formatado = '.'.join(ip) # criar o texto que representa o ip
        
    rs = os.system('ping -c 1 {}'.format(ip_formatado))
    print(rs)
    if rs == 0:
            print ('IP {} está on'.format(ip_formatado))
    else:
        print ('IP {} está off'.format(ip_formatado))
    #realizar um ping para o IP ou Host informado

def teste_de_vulnerabilidade_nmap(): #opção 3
    
    ip = input("Qual IP? ")
    nmap=  os.system(f'nmap -sV --script vuln {ip}')
    print(nmap)


def acionar_whois(): # Opção 4
    
    host = input("Insira o HOST ")
    w = whois.whois(host)    
    #simplesmente executo um whois no host informado
    print(w)
    
def meuip(): # Opção 6
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    # inicializa a função do modulo socket e conecta com o ip interno 8.8.8.8:80
    ip=s.getsockname()[0]
    return ip
    #realiza uma conexão com o ip e porta e retorna o próprio IP da máquina

def alteraip(): # Opção 7    => Script não funciona https://www.google.com/search?q=modificar+meu+ip+ubuntu+terminal&oq=modificar+meu+ip+u&aqs=chrome.2.69i57j33i160l2.6062j0j4&client=ubuntu&sourceid=chrome&ie=UTF-8
    print("IP atual é ", meuip()) #chama a mesma função da opção 6
    opcao = input('sua conexão é cabo ou sem fio: ')
    if ok() == 'Linux':
        print('começando...')
        

        escolha= input("Qual IP novo?")
       
        if opcao in 'Ss':
            os.system(f'ifconfig wlan0 {escolha}')
            os.system('sudo service networking restart')
        if opcao in 'Cc':
            os.system(f'ifconfig eth0 {escolha}')
            os.system('sudo service networking restart')
        print(f'novo IP: ', meuip())
    if ok == 'Windows':
        print('começando...')
        
        os.system('ipconfig /release')
        os.system('ipconfig /renew')

def varrer_portas_abertas(): # Opção 8
    #input de ip e portas que deseja vascular
    portas_abertas=[]
    ip = str(input("Input ip server: "))
    start = int(input("Input porta inicial: "))
    end=int(input("Input porta final:"))
    for port in range(start,end):
        print("Teste porta "+str(port)+"....")
        s=socket.socket(AF_INET, SOCK_STREAM)
        s.settimeout(5)
        if(s.connect_ex((ip,port))==0):
            #print("port", port, "está aberta")
            portas_abertas.append(str(port))
        s.close()
    os.system('clear')
    print("Portas abertas: ")
    print(portas_abertas)
    print("Principais portas:\nFTP- 21 |SSH- 22 |Telnet- 23|SMTP- 25|DNS- 53|HTTP- 80|POP3- 110|SFTP- 115|IMAP4- 143|SQL- 156|HTTPS- 443|SMTP- 465|SMTP- 587")



main()
    

