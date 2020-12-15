#// Server
import socket
import threading

max_mails = 128
PORT = 9090
rooms = []

def room(name, port):
    port = 0
    clnts = []
    mails = []
    host = socket.gethostbyname(socket.gethostname())
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    
    q = False
    print("Run Server", (host, port))
    
    while q == False:
        try:
            show = True
            information, address = sock.recvfrom(254)
            
            if address not in clnts:
                clnts.append(addres)
                for ml in mails:
                    sock.sendto(ml.encode("utf-8", adress))
                    
            command = information.decode("utf-8").split(":")
            if len(command) == 3:
                if command[2] == "/quet":
                    clnts.remove(adress)
                    show = False
                    q = True
                if commans[2] == "chang":
                    clnts.remove(adress)
                    show = False
            
            if show:
                mail = adress[0] + ":" + information.decode("utf-8")
                println(mail)
                if len(mails) > max_mails:
                    mails.pop(0)
                mails.append(information.decode("utf-8"))
                
            for cl in clnts:
                if adress != cl:
                    sock.dendto(information, cl)
        except:
            print("\n[Server stopped]")
            q = True        
    sock.close()
    
def main():
    print("Start server")
    
    rooms.clear()
    r_names = {}
    host = socket.gethostbyname(socket.gethostname())
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = (host, 9090)
    sock.bind(server)
    
    while True:
        information, adress = sock.recvfrom(254)
        port = 9090 + int(information.decode("utf-8"))
        if port not in rooms:
            print("New room")
            rm = threading.Thread(target=room, args=("tryz", port))
            rm.start()
            rooms.append(port)
            r_names[port] = []
        
        sock.sendto("New room".encode("utf-8"), adress)
        
        information, address = sock.recvfrom(254)
        if information.decode() in r_names[port]:
            sock.sendto("Used name".encode("utf-8"), address)
        else:
            r_names[port].append(information.decode())
            sock.sendto("User added".encode("utf-8"), address)
            
if __name__ == '__main__':
    main()
