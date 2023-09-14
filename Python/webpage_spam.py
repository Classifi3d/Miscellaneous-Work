
import urllib.request,time
import threading
# open a connection to a URL using urllib


def connection( threadName,port):
    while True:
        webUrl  = urllib.request.urlopen('http://192.168.0.94/'+str(port)+'/on')
        time.sleep(0.1)
        webUrl  = urllib.request.urlopen('http://192.168.0.94/'+str(port)+'/off')
        # webUrl  = urllib.request.urlopen('dan-mustea.com')
        time.sleep(0.1)
       
       
if __name__ == "__main__": 
    try:
        x = threading.Thread(target=connection, args=(1,4))
        x.start()
        x = threading.Thread(target=connection, args=(2,5))
        x.start()
    except:
        print("Error: unable to start thread")
    
    while 1:
        pass