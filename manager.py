
import subprocess
from os import system
import json
from hashlib import sha256
import getpass


def geimages():
    img  = subprocess.check_output(["docker","images"])

    images = (img.decode("utf-8"))

    return images
def gecontainers():
    res  = subprocess.check_output(["docker","ps","-a"])

    result = (res.decode("utf-8"))


    return result
def getactivecontainers():
    res  = subprocess.check_output(["docker","ps"])

    result = (res.decode("utf-8"))

 
    return result

def startc(name):
    res  = subprocess.check_output(["docker","start",name])

    result = (res.decode("utf-8"))

    return result
def stopc(name):
    res  = subprocess.check_output(["docker","stop",name])

    result = (res.decode("utf-8"))

    return result
def delc(name):
    try:
        res  = subprocess.check_output(["docker","rm",name])
    except:
        res  = subprocess.check_output(["docker","stop",name])
        res  = subprocess.check_output(["docker","rm",name])
    
    result = (res.decode("utf-8"))

    return result

def run(container,command,arg):
    res  = subprocess.check_output(["docker","exec","-i",container,command,arg])

    result = (res.decode("utf-8"))
    
    return result



def clean():
    res  = subprocess.check_output(["docker","image","prune","-f"])
    result = (res.decode("utf-8"))
    return result
def makefile(rp,u,up):
    s = f"""

echo -e "{rp}\\n{rp}\\n{rp}" | passwd root &&
echo -e "\\n\\n\\n\\n\\n\y" | adduser {u} &&
echo -e "{up}\\n{up}\\n{up}" | passwd {u} 

    """
    open("init.sh",'w').write(s)
def createcont(name,image,inport=0,outport=0):
    if(inport==0 and outport ==0):
        res  = subprocess.check_output(["docker","run","-d","--name" , name, image])
        
    else:res  = subprocess.check_output(["docker","run","-d","-p",f"{inport}:{outport}","--name" , name, image])

    if (image == 'python-ssh' or 1==1):
        rp = input("Root Password : ")
        u = input("Default User Name : ")
        up = input("Default User Password : ")
        makefile(rp,u,up)
        subprocess.run( f"docker exec -i -u root {name} /bin/bash < init.sh " ,shell=True,stdout=subprocess.DEVNULL,stderr= subprocess.DEVNULL)

    
    result = (res.decode("utf-8"))
    return result




def main():

    while (True):
        system("clear")
        print ("""
   ___________ _   _________ 
  / __/ __/ _ \ | / / __/ _ \\
 _\ \/ _// , _/ |/ / _// , _/
/___/___/_/|_||___/___/_/|_|

    by SeekerRook

    """
    )
        choice = input ("""
Options :
    1) Images
    2) Containers
    0) Quit

>> """
               )
        if choice == '1':
            while(True):
                choice = input ("""
Image Options :
    1) get images
    2) clean prune
    0) Back

>> """)
                if choice == '1':
                    print(geimages())
                elif choice == '2':
                    print(clean())

                elif choice == '0':
                
                    break
                else:
                     print("What???")
        elif choice == '2':
           while(True):
                choice = input ("""
Container Options :

    1) get all containers
    2) get active containers

    3) start container
    4) stop container
    
    5) New container
    6) Delete container

    7) Run Command inside Container

    0) Back

>> """)
                if choice == '1':
                    print(gecontainers())
                elif choice == '2':
                    print(getactivecontainers())

                elif choice == '3':
                    n = input("Container name : ")
                    print(startc(n))

                elif choice == '4':
                    n = input("Container name : ")

                    print(stopc(n))
                elif choice == '5':
                        n = input("Container name : ")
                        i = input("Container Image (if not sure python-ssh) : ")
                        op = input("Container in-port (if not sure 22): ")
                        ip = input("Container out-port (something original): ")
                        
                        print(createcont(name=n,image=i,inport=int(ip),outport=int(op)))
                        print(gecontainers())
                elif choice == '6':
                    n = input("Container name : ")

                    print(delc(n))

                elif choice == '7':
                    choice = input ("""
Choose Command :

    1) show directory content
    2) read file
    3) create file

>> """)

                    if choice == '1':

                        n = input("Container name : ")
                        d = input("Directory : ")

                        print(run(n,"ls",d))
                    elif choice == '2':

                        n = input("Container name : ")
                        d = input("File Path : ")

                        print(run(n,"cat",d))
                    elif choice == '3':

                        n = input("Container name : ")
                        d = input("File Path : ")

                        print(run(n,"touch",d))

                elif choice == '0':
                
                    break
                else:
                     print("What???")

        elif choice == '0':
            print ("""

             Bye!!!!

             """)
            exit(0)

        else :
            print("What???")

if __name__ == "__main__":

        main()
