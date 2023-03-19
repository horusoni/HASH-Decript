#!usr/bin/env python
import hashlib
import os
import time
os.system('clear')

imagem =    "⠄⠄⠄⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⠄⠄⠄⡀⠄⢀⣿⣿⠄⠄⠄⢸⡇⠄⠄\n"\
            "⠄⠄⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄\n"\
            "⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄\n"\
           "⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄\n"\
           "⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰\n"\
           " ⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤\n"\
            "⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗\n"\
            "⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄\n"\
            "⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄\n"\
            "⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄\n"\
           " ⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄\n"\
           " ⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄\n"\
           " ⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁\n"\
           "⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴\n"\
           "⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿\n"\
           
print(imagem)

time.sleep(2)
os.system('clear')


#cifrar SHA-1
def sha1(dig):
    msg = input(dig)
    sha = hashlib.sha1(msg.encode())
    hexasha1 = sha.hexdigest().upper()
    print('\ncifra SHA1:\n'+hexasha1+'\n')
#cifrar SHA-256
def sha256(dig):
    msg = input(dig)
    sha = hashlib.sha256(msg.encode())
    hexasha256 = sha.hexdigest().upper()
    print('\ncifra SHA-256:\n'+hexasha256+'\n')
#cifrar SHA-512
def sha512(dig):
    msg = input(dig)
    sha = hashlib.sha512(msg.encode())
    hexasha512 = sha.hexdigest().upper()
    print('\ncifra SHA-512:\n'+hexasha512+'\n')

#decifrar sha-1 ---
def decifrarsha1(dig):

    listpass = ""
    with open("senhas.txt",'r') as senha:
        listpass  = senha.readlines()
        
    msg = input(dig)
    
    i = 0
    while i< len(listpass):
        sha = msg

        senha = listpass[i].replace('\n',"")
        listcript = hashlib.sha1(senha.encode()).hexdigest()
        
        os.system('clear')
        print(f'\nSENHA:{listpass[i]}')
        print(f'\nALVO:         [{sha.upper()}]\nCOMPARANDO:   [{listcript.upper()}]')
        print(f'')
          
        if listcript.upper() == sha.upper():
            print(f'               [CHAVE ENCONTADA!!]')
            print(f'               [SENHA: {senha}]')
            break

        else:
            time.sleep(0.01)
            print(f'                       [CHAVE NÂO ENCONTADA!]\n{senha}')
            i+=1

#decifra SHA-256---
def decifrarsha256(dig):

    listpass = ""
    with open("senhas.txt",'r') as senha:
        listpass  = senha.readlines()
        
    msg = input(dig)
    
    i = 0
    while i< len(listpass):
        sha = msg

        senha = listpass[i].replace('\n',"")
        listcript = hashlib.sha256(senha.encode()).hexdigest()
        
        os.system('clear')
        print(f'\nSENHA:{listpass[i]}')
        print(f'\nALVO:         [{sha.upper()}]\nCOMPARANDO:   [{listcript.upper()}]')
        print(f'')
        
        if listcript.upper() == sha.upper():
            print(f'               [CHAVE ENCONTADA!!]')
            print(f'               [SENHA: {senha}]')
            break

        else:
            time.sleep(0.01)
            print(f'                       [CHAVE NÂO ENCONTADA!]\n{listpass[i]}')
            i+=1

#decifar SHA-512---
def decifrarsha512(dig):

    listpass = ""
    with open("senhas.txt",'r') as senha:
        listpass  = senha.readlines()
        
    msg = input(dig)
    
    i = 0
    while i< len(listpass):
        sha = msg.upper()

        senha = listpass[i].replace('\n',"")
        listcript = hashlib.sha512(senha.encode()).hexdigest()
        
        os.system('clear')
        print(f'\nSENHA:{listpass[i]}')
        print(f'\nALVO:         [{sha}]\nCOMPARANDO:   [{listcript.upper()}]')
        print(f'')
            
        if listcript.upper() == sha:
            print(f'               [CHAVE ENCONTADA!!]')
            print(f'               [SENHA: {senha}]')
            break

        else:
            time.sleep(0.01)
            print(f'                       [CHAVE NÂO ENCONTADA!]\n{listpass[i]}')
            i+=1

#criar Wordlist
def listadesenha():
    os.system('clear')
    min = input('\nQuantidade mínima de dígitos que conterá sua senha.\n>> ')
    os.system('clear')
    max = input('Quantidade máxima de dígitos que conterá sua senha.\n>> ')
    os.system('clear')
    conteudo = input('Digite o conteúdo de sua senhas ex: Hello123.\n>> ')

    numin = int(min)
    numax = int(max)

    print('Sua wordlist está sendo criada em senhas.txt\nAguarde...')
    time.sleep(2)
    
    os.system(f'crunch {numin} {numax} {conteudo} -o senhas.txt')

#program
while True:
    iniciar = input('Selecione uma opção:\n\n[0] CIFRAR\n[1] DECIFRAR\n[2] CRIAR SENHAS\n[X] SAIR\n ').lower()

    #cifrar
    if iniciar == "0":
        os.system('clear')

        print('[CIFRAR]')
        option = input('\n[0]SHA-1\n[1]SHA-256\n[2]SHA-512\n[R]Voltar\n: ').lower()

        if option == '0':
            sha1('Digite o texto claro: ')

        if option == '1':
            sha256('Digite o texto claro: ')

        if option == '2':
            sha512('Digite o texto claro: ')
        #retorna para opção iniciar
        if option == 'r':
            os.system('clear')
            iniciar

    #encontrar combinação de hash
    if iniciar == '1':
        os.system('clear')
        print('[DECIFRAR]')
        option = input('\n[0]SHA-1\n[1]SHA-256\n[2]SHA-512\n[R]Voltar\n: ').lower()

        if option == '0':
            decifrarsha1('Decifrar SHA1:')

        if option == '1':
            decifrarsha256('Decifrar SHA-256: ')

        if option == '2':
            decifrarsha512('Decifrar SHA-512: ')

        if option == 'r':
            os.system('clear')
            iniciar
    
    if iniciar == '2':
        listadesenha()

    #sair da a plicação
    if iniciar == "x":
        print('\nObrigado por usar\nby: ʜᴏʀᴜsᴏɴɪ')
        break