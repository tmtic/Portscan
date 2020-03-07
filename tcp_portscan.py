import socket # Importação da biblioteca socket

host = input('Insert the host: ')
ports = []
decision = int(input('How many ports? > '))

while decision >= 1:
    ports.append(int(input('Insert the port: ')))
    decision -= 1

try:
    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.05)
        code = client.connect_ex((host, port))
        
        if code == 0:
            print(port, ' Open')
        else:
            print(port, ' Filtered')
        
    client.close()
except Exception as err:
    print(err)



