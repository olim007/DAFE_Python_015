//import socket
import thread
import time

max_symbol = 254
PORT = 9090
working = True
connect = False

def addRoom(sock, server, host, com):
    port = int(com[1])
    sock.sendto(com[1].encode("utf-8"), server)
    time.sleep(0.4)

    information, address = sock.recvfrom(254)
    if information.decode("utf-8") != "New room":
        print("Enter different room")
    print(information.decode("utf-8"))

    information, address = sock.recvfrom(254)
    print(data.decode("utf-8"))
    if data.decode("utf-8") == "User added":
            self.connect = True
            return port, name    
    

def chat(sock, server, host):
    print("If you want subscribe, enter your name and rooms number in format - add name rooms_number")
    print("If you want add message, enter your name and rooms number in format - addmsg name rooms_number message")
    print("If you want publish mails, enter your name and rooms number in format - publish name rooms_number")
    print("If you want creat room, enter room number in format = addroom number")
    print("If you want quit, enter /quit")
    while working:        
        print("Enter command\n")
        command= input()
        com = command.split(' ')
        if com[0] == '\quit':
            warking = False
#        if com[0] == 'add':
            #addClient(sock, server, host, com)
#        if com[0] == 'publish':
            #showHistoy(sock, server, host, com)
#        if com[0] == 'addmsg':
            #addMessage(sock, server, host, com)
        if com[0] == 'addroom':
            addRoom(sock, server, host, com)

def main():
    port = 0
    host = socket.gethostbyname(socket.gethostname())
    server = (host, 9090)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    sock.setblocking(0)
    
    chat(sock, server, host)
    
    sock.close()
    
if __name__ == '__main__':
    main()
