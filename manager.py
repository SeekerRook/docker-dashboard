
import subprocess
from os import system
def geimages():
    img  = subprocess.check_output(["docker","images"])

    images = (img.decode("utf-8"))

    return images
def gecontainers():
    cont  = subprocess.check_output(["docker","ps","-a"])

    conteiners = (cont.decode("utf-8"))


    return conteiners
def getactivecontainers():
    cont  = subprocess.check_output(["docker","ps"])

    conteiners = (cont.decode("utf-8"))

 
    return conteiners

def startc(name):
    cont  = subprocess.check_output(["docker","start",name])

    conteiners = (cont.decode("utf-8"))

    return conteiners
def stopc(name):
    cont  = subprocess.check_output(["docker","stop",name])

    conteiners = (cont.decode("utf-8"))

    return conteiners
def delc(name):
    try:
        cont  = subprocess.check_output(["docker","rm",name])
    except:
        cont  = subprocess.check_output(["docker","stop",name])
        cont  = subprocess.check_output(["docker","rm",name])
    
    conteiners = (cont.decode("utf-8"))

    return conteiners
def attach(name):
    cont  = subprocess.check_output(["docker","attach",name])

    conteiners = (cont.decode("utf-8"))

    return conteiners

def clean():
    cont  = subprocess.check_output(["docker","image","prune","-f"])
    conteiners = (cont.decode("utf-8"))
    return conteiners
def makefile(rp,u,up):
    s = f"""

echo -e "{rp}\\n{rp}\\n{rp}" | passwd root &&
echo -e "\\n\\n\\n\\n\\n\y" | adduser {u} &&
echo -e "{up}\\n{up}\\n{up}" | passwd {u} 

    """
    open("init.sh",'w').write(s)
def createcont(name,image,inport=0,outport=0):
    if(inport==0 and outport ==0):
        cont  = subprocess.check_output(["docker","run","-d","--name" , name, image])
        
    else:cont  = subprocess.check_output(["docker","run","-d","-p",f"{inport}:{outport}","--name" , name, image])

    if (image == 'python-ssh'):
        rp = input("Root Password : ")
        u = input("Default User Name : ")
        up = input("Default User Password : ")
        makefile(rp,u,up)
        system( f"docker exec -i -u root {name} /bin/bash < init.sh" )
    
    conteiners = (cont.decode("utf-8"))
    return conteiners


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
                    # try:
                        n = input("Container name : ")
                        i = input("Container Image (if not sure python-ssh) : ")
                        op = input("Container in-port (if not sure 22): ")
                        ip = input("Container out-port (something original): ")
                        
                        print(createcont(name=n,image=i,inport=int(ip),outport=int(op)))
                        print(gecontainers())

                    # except  :
                    #     print("INVALID NAME OR PORT!!!!")
                    #     print("Check Here:")
                    #     print(gecontainers())
                elif choice == '6':
                    n = input("Container name : ")

                    print(delc(n))

                    # print ("Not Implemented yet")

                elif choice == '0':
                
                    break
                else:
                     print("What???")
        # elif choice == '3':
        #     print ("Not Implemented yet")
        # elif choice == '5':
        #     print ("Not Implemented yet")
        elif choice == '0':
            print ("""

             Bye!!!!

             """)
            exit(0)

        else :
            print("What???")

if __name__ == "__main__":
    main()