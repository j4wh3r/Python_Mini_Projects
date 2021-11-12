import socket
#tested on metasploitable2
# connect_ex() = 0 ; if operation succeeded(port open)

target = input("enter the target IP address: ")
ports = [80,443,53,25,21,22,23,445,3306,5900,2049,111]


for port in ports:
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        status = s.connect_ex((target,port))
        if status == 0:
            print(f"[*]Port {port} is open")
        else:
            print(f"[*]Port {port} is closed")