from socket import *

# parameters are ip address and a single port 
def conScan(tgtHost, tgtPort):
    try: 
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((tgtHost, tgtPort))
        print('[+]%d/tcp open'% tgtPort)
        connskt.close()
    except:
        print('[-]%d/tcp closed'% tgtPort)

# parameters are host name and multiple target ports 
def portScan(tgtHost, tgtPorts):
    try: 
        tgtIP = gethostbyname(tgtHost)
    except: 
        print('[-] Cannot resolve %s '% tgtHost)

        return 
    
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+] Scan result of: %s ' % tgtName[0])       
    except: 
        print('\n[+] Scan result of: %s ' % tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts: 
        print('Scanner Port: %d' % tgtPort)
        conScan(tgtHost, int(tgtPort))


if __name__ == '__main__':

# input (tgtName, tgtPorts)    
    portScan('github.com', [80,22])
