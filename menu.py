import os
import getpass

os.system("tput setaf 1")
print("\t\t\t Hey welcome to my TUI, Which makes the use of Linux easy")
os.system("tput setaf 7")
print("\t\t\t --------------------------------------------------------")
os.system("tput setaf 3")

#passwd = input("Enter your password:")
passwd = getpass.getpass("Enter your password :")

pw = "test123"

if passwd != pw:
    print("auth incorrect")
    exit()

print("where you would like to perform your job { local / remote } :" , end='')
location = input()
print(location)

if location == "remote":
    remoteIP = input("Enter your IP : ")
    ip=remoteIP

while True:
    #os.system("clear")
    print("""
    Press 1: Linux
    Press 2: AWS
    Press 3: Apache Webserver
    Press 4: Hadoop
    Press 5: Ansible
    Press 6: Docker
    press 7: To go back into first menu
    Press 8: Exit
    """)

    ch = int(input(" Enter your choice : "))
    
    if location == "local":
      if ch == 1:
        print("""********* LINUX *************
              """)

        while True:
               # os.system("clear")
                print("\t\t\t\t\t Linux")
                print("\t\t\t\t\t-------")
                print("""
                Press 1 : To Check Date
                Press 2 : To Check Calender
                Press 3 : To Check Ip
                Press 4 : To Check Network connectivity
                Press 5 : To Use Python
                press 6 : To Create Directory
                press 7 : To Check the Software is installed or not
                Press 8 : To Check Domain name
                Press 9 : To Launch Firefox
                Press 10: To Create User
                Press 11: To Create File
                Press 12: To go into main menu
                Press 13: Exit from program
                """)

                print("Enter Your Choice : ",end="")

                ch=input()
                
                if int(ch) == 1:
                    os.system("date")
                elif int(ch) == 2:
                    os.system("cal")
                elif int(ch) == 3:
                    os.system("ifconfig")
                elif int(ch) == 4:
                    os.system("ping goo.gl -c 5")
                elif int(ch) == 5:
                    os.system("python3")
                elif int(ch) == 6:
                    print("Enter the dir name")
                    dir_name = input()
                    os.system("mkdir {}".format(dir_name))
                    print("Directory Created Successfully")
                elif int(ch) == 7:
                    print("Enter the package name")
                    package_name = input()
                    os.system("rpm -q {}".format(package_name))
                elif int(ch) == 8:
                    print("Enter the site name")
                    site_name = input()
                    os.system("nslookup {}".format(site_name))
                elif int(ch) == 9:
                    print("Enter the site name")
                    Enter_site_name = input()
                    os.system("firefox {}".format(Enter_site_name))                              
                elif int(ch) == 10:
                    print("can u please user name: ", end='')
                    create_user = input()
                    passwd = input()
                    os.system("useradd {}".format(create_user))
                    os.system("passwd {}".format(passwd))                    
                elif int(ch) == 11:
                    print("can u please enter file name: ", end='')
                    file_name = input()
                    os.system("touch {}".format(file_name))
                    print("File Created Successfully")
                elif int(ch) == 12:
                  break
                elif int(ch) == 13:
                  exit()
                else:
                  print("Your choice is wrong....")
                
        
        # ENTER ALL LINUX CMD HERE




      elif ch == 2:
        print("""********* AWS *************
              """)
        while True:
               # os.system("clear")
                print("\t\t\t\t\t AWS")
                print("\t\t\t\t\t-----")
                print("""
                Press  0 : To install aws-cli
                Press  1 : To Login into AWS CLI
                Press  2 : To Launch a instance
                Press  3 : To Start a Instance
                Press  4 : To Stop a Instance 
                Press  5 : To Describe All Instances 
                Press  6 : To Create a Volume
                Press  7 : To Attach volume with instance
                Press  8 : For Partitioning the attached volume
                Press  9 : To configure Web Server
                Press 10 : To Format Partition
                Press 11 : To Mount the Web Server to Volume
                Press 12 : To go into main menu
                Press 13 : Exit from program
                """)

                print("Enter Your Choice : ",end="")

                ch=input()

                if int(ch) == 0:
                    os.system("pip3 install awscli --upgrade")
                    
                elif int(ch) == 1:

                    os.system("aws configure")

                elif int(ch) == 2:
                    print("""
                            Press 1:AWS Linux
                            Press 2:Redhat Linux
                            """)
                    print("Enter your Choice :  ",end="")
                    img=input()
                    if int(img) ==1:
                        print("Enter Your Key name: ",end ="")
                        key = input()
                        os.system("aws ec2 run-instances --image-id  ami-081bb417559035fe8 --subnet-id subnet-0ecad70c1783cb8f6 --instance-type t2.micro --key-name {} --security-group-ids sg-0eb67d6f24e2401ca --count 1".format(key))
                    elif int(img) == 2:
                        print("Enter Your Key name: ",end ="")
                        key = input()
                        os.system("aws ec2 run-instances --image-id  ami-0a9d27a9f4f5c0efc  --subnet-id subnet-0ecad70c1783cb8f6  --instance-type t2.micro --key-name {} --security-group-ids sg-0eb67d6f24e2401ca --count 1".format(key))


                elif int(ch) == 3:

                    print("Enter Instance Id : ",end = "")
                    uid = input()
                    os.system(" aws ec2 start-instances --instance-id {}".format(uid))


                elif int(ch) == 4:
                    
                    print("Enter Instance Id : ",end = "")
                    uid = input()
                    os.system(" aws ec2 stop-instances --instance-id {}".format(uid))


                elif int(ch) == 5:

                    os.system("aws ec2 describe-instances")

                    
                elif int(ch) == 6:

                    
                    print("Enter Size : ",end = "")
                    size = input()
                    print("Enter availability zone : ",end = "")
                    zone = input()
                    print("Enter volume type : ",end= "")
                    vtype = input()
                    os.system(" aws ec2 create-volume  --availability-zone {} --size {} --volume-type {}".format(zone,size,vtype))


                elif int(ch) == 7:


                    os.system("tput setaf 3")
                    print("\t\t\tVolume Zone & Instance Zone Must be same !!!")
                    print("\t\t\t--------------------------------------------")
                    os.system("tput setaf 7")
                    print("Enter volume-id : ",end = "")
                    vid = input()
                    print("Enter instance-id : ",end = "")
                    iid = input()
                    print("Enter device : /dev/",end= "")
                    device = input()
                    os.system(" aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/{} ".format(vid,iid,device))


                elif int(ch) == 8:

                    print("Enter IP : ",end = "")
                    ip = input()
                    print("Enter key : ",end = "")
                    key = input()
                    print("Enter device : /dev/",end= "")
                    device = input()
                    os.system(" ssh -l ec2-user {} -i {}.pem sudo fdisk /dev/{} ".format(ip,key,device))



                elif int(ch) == 9:

                    os.system("tput setaf 3")
                    print("\t\t\tHTTPD must be installed...")
                    print("\t\t\t--------------------------")
                    os.system("tput setaf 7")
                    print("Enter IP : ",end = "")
                    ip = input()
                    print("Enter key : ",end = "")
                    key = input()
                    os.system(" ssh -l ec2-user {} -i {}.pem sudo systemctl start httpd ".format(ip,key))


                elif int(ch) == 10:

                    print("Enter IP : ",end = "")
                    ip = input()
                    print("Enter key : ",end = "")
                    key = input()
                    print("Enter Device : /dev/",end="")
                    device = input()
                    os.system(" ssh -l ec2-user {} -i {}.pem sudo mkfs.ext4 /dev/{} ".format(ip,key,device))


                elif int(ch) == 11:

                    print("Enter IP : ",end = "")
                    ip = input()
                    print("Enter key : ",end = "")
                    key = input()
                    print("Enter Device : /dev/",end="")
                    device = input()
                    os.system(" ssh -l ec2-user {} -i {}.pem sudo mount /dev/{} /var/www/html/ ".format(ip,key,device))


                elif int(ch) == 12:
                    break
                
                elif int(ch) == 13:
                    exit()

                else:
                    print("You Entered Wrong Choice ...")
        


        # ENTER ALL AWS CMD HERE



      elif ch == 3:
        print("""********* WEBSERVER *************
              """)
        while True:
                #os.system("clear")
                print("\t\t\t\t\t WebServer")
                print("\t\t\t\t\t-----------")
                print("""
                         Press 1: To install WebServer
                         Press 2: To copy code to required folder
                         Press 3: To start service of httpd
                         Press 4: To go to main menu
                         Press 5: Exit from program

                      """)
                
                ch = input(" Enter your choice : ")

                if int(ch) == 1:
                      os.system("yum install httpd -y")
                elif int(ch) == 2:
                    os.system("echo HelloWorld >> /var/www/html/test.html")
                elif int(ch) == 3:
                    os.system("systemctl start httpd")
                elif int(ch) == 4:
                  break
                elif int(ch) == 5:
                  exit()
                else :
                  print("You entered wrong choice....")


        # ENTER ALL web server HERE



      elif ch == 4:
        print("""********* HADOOP *************
              """)

        while True:
                #os.system("clear")
                print("\t\t\t\t\t HADOOP ")
                print("\t\t\t\t\t--------")
                print("""
                         Press 1: To start Hadoop namenode
                         Press 2: To view Hadoop filelist
                         Press 3: To stop Hadoop namenode
                         Press 4: To Start Hadoop datanode
                         Press 5: To View Hadoop fileslist
                         Press 6: To Stop Hadoop datanode
                         Press 7: To go to main menu
                         Press 8: Exit from program

                      """)
                
                ch = input(" Enter your choice : ")
                
                if int(ch) == 1:
                      os.system("hadoop-daemon.sh start namenode")
                elif int(ch) == 2:
                    os.system("hadoop fs -ls /")	
                elif int(ch) == 3:
                    os.system("hadoop-daemon.sh stop namenode")
                elif int(ch) == 4:
                      os.system("hadoop-daemon.sh start datanode")
                elif int(ch) == 5:
                    os.system("hadoop fs -ls /")	
                elif int(ch) == 6:
                    os.system("hadoop-daemon.sh stop datanode")
                elif int(ch) == 7:
                  break
                elif int(ch) == 8:
                  exit()
                else:
                  print(" You entered wrong choice....")

        # ENTER ALL HADOOP CMD HERE
      


      elif ch == 5:
        print("""********* ANSIBLE *************
              """)
        
        while True:
                #os.system("clear")
                print("\t\t\t\t\t Ansible")
                print("\t\t\t\t\t---------")
                print("""
                         Press 1: To install ansible 
                         Press 2: to configure ansible
                         Press 3: Create inventory directory 
                         Press 4: To go to main menu
                         Press 5: Exit from program

                      """)
                
                ch = input(" Enter your choice : ")

                if int(ch) == 1:
                      os.system("pip3 install ansible")
                elif int(ch) == 2:
                    os.system("mkdir /etc/ansible")
                elif int(ch) == 3:
                    os.system("vi /etc/ansible/ansible.cfg")
                    os.system("vi /etc/ansible/inventory.txt")
                elif int(ch) == 4:
                  break
                elif int(ch) == 5:
                  exit()
                else :
                  print("You entered wrong choice....")


        # ENTER ALL ANSIBLE CMD HERE






      elif ch == 6:
        print("""********* DOCKER *************
              """)
        while True:
                #os.system("clear")
                print("\t\t\t\t\t DOCKER ")
                print("\t\t\t\t\t--------")
                print("""
                         Press 1: To Install Docker Service
                         Press 2: To start Docker Service
                         Press 3: To pull Webserver image
                         Press 4: To launch Webserver image
                         Press 5: To go to main menu
                         Press 6: Exit from program

                """)

                print("Enter Your Choice : ",end="")

                ch=input()
                
                if int(ch) == 1:
                      os.system("yum install docker-ce --nobest -y")
                elif int(ch) == 2:
                    os.system("systemctl start docker")
                elif int(ch) == 3:
                    os.system("docker pull anuddeeph/apache-webserver-php:latest")
                elif int(ch) == 4:
                    os.system("docker run -it --name webserver anuddeeph/apache-webserver-php:latest")
                elif int(ch) == 5:
                  break
                elif int(ch) == 6:
                  exit()
                else :
                  print("You entered wrong choice....")

        # ENTER ALL DOCKER CMD HERE




      elif ch == 7:
        break

      elif ch == 8:
        exit()
      
      else:
        print(" you entered wrong choice....")

  
    elif location == "remote":
      ip=remoteIP
      if ch == 1:
          print("""********* LINUX *************
                """)

          while True:
                  #os.system("ssh {} clear")
                  print("\t\t\t\t\t Linux")
                  print("\t\t\t\t\t-------")
                  print("""
                  Press 1: To Check Date
                  Press 2: To Check Calender
                  Press 3: To check Ip
                  Press 4: To check Network connectivity
                  Press 5: To use Python
                  Press 6: To Create Directory
                  Press 7: To check the Software is installed or not                           Press 8: To Check Domain name
                  Press 9: To Launch Firefox
                  Press 10: To Create User
                  Press 11: To Create File
                  Press 12: To go into main menu
                  Press 13: Exit from program
                  """)

                  print("Enter Your Choice : ",end="")

                  ch=input()
                  
                  if int(ch) == 1:
                      os.system("ssh {} date".format(remoteIP))
                  elif int(ch) == 2:
                      os.system("ssh {} cal".format(remoteIP))
                  elif int(ch) == 3:
                      os.system("ssh {} ifconfig".format(remoteIP))
                  elif int(ch) == 4:
                      os.system("ssh {} ping goo.gl -c 5".format(remoteIP))
                  elif int(ch) == 5:
                      os.system("ssh {} python3".format(remoteIP))
                  elif int(ch) == 6:
                      print("Enter the directory name")
                      dir_name = input()
                      os.system("ssh {} mkdir {}".format(remoteIP,dir_name))
                      print("Directory Created Successfully")
                  elif int(ch) == 7:
                      print("Enter the package name")
                      package_name = input()
                      os.system("ssh {} rpm -q {}".format(remoteIP,package_name))
                      
                  elif int(ch) == 8:
                      print("Enter the site name")
                      site_name = input()
                      os.system("ssh {} nslookup {}".format(remoteIP,site_name))
                  elif int(ch) == 9:
                      print("Enter the site name")
                      Enter_site_name = input()
                      os.system("ssh {} firefox {}".format(remoteIP,Enter_site_name))
                  elif int(ch) == 10:
                      print("can u please user name: ", end='')
                      create_user = input()
                      passwd = input()
                      os.system("ssh {} useradd {}".format(remoteIP,create_user))
                      os.system("ssh {} passwd {}".format(remoteIP,passwd))
                  elif int(ch) == 11:
                      print("can u please enter file name: ", end='')
                      file_name = input()
                      os.system("ssh {} touch {}".format(remoteIP,file_name))
                      print("File Created Successfully")
                  elif int(ch) == 12:
                    break
                  elif int(ch) == 13:
                    exit()
                  else:
                    print("Your choice is wrong....")
      
      elif int(ch) == 2:
              while True:
                  print("\t\t\t\t\t AWS")
                  print("\t\t\t\t\t-----")
                  print("""
                  Press  0 : To install aws-cli
                  Press  1 : To Login into AWS CLI
                  Press  2 : To Launch a instance
                  Press  3 : To Start a Instance
                  Press  4 : To Stop a Instance 
                  Press  5 : To Describe All Instances 
                  Press  6 : To Create a Volume
                  Press  7 : To Attach volume with instance
                  Press  8 : For Partitioning the attached volume
                  Press  9 : To configure Web Server
                  Press 10 : To Format Partition
                  Press 11 : To Mount the Web Server to Volume
                  Press 12 : Exit
                  """)

                  print("Enter Your Choice : ",end="")

                  ch=input()

                  if int(ch) == 0:
                      os.system("ssh {} pip3 install awscli --upgrade".format(remoteIP))
                      
                  elif int(ch) == 1:

                      os.system("ssh {} aws configure".format(remoteIP))

                  elif int(ch) == 2:
                      print("""
                              Press 1:AWS Linux
                              Press 2:Redhat Linux
                              """)
                      print("Enter your Choice :  ",end="")
                      img=input()
                      if int(img) ==1:
                          print("Enter Your Key name: ",end ="")
                          key = input()
                          os.system("ssh {} aws ec2 run-instances --image-id ami-081bb417559035fe8 --subnet-id subnet-0ecad70c1783cb8f6 --instance-type t2.micro --key-name {} --security-group-ids sg-0eb67d6f24e2401ca --count 1".format(remoteIP,key))
                      elif int(img) == 2:
                          print("Enter Your Key name: ",end ="")
                          key = input()
                          os.system("ssh {} aws ec2 run-instances --image-id ami-0a9d27a9f4f5c0efc  --subnet-id subnet-0ecad70c1783cb8f6  --instance-type t2.micro --key-name {} --security-group-ids sg-0eb67d6f24e2401ca --count 1".format(remoteIPkey))


                  elif int(ch) == 3:

                      print("Enter Instance Id : ",end = "")
                      uid = input()
                      os.system("ssh {}  aws ec2 start-instances --instance-id {}".format(remoteIP,uid))


                  elif int(ch) == 4:
                      
                      print("Enter Instance Id : ",end = "")
                      uid = input()
                      os.system("ssh {}  aws ec2 stop-instances --instance-id {}".format(remoteIP,uid))


                  elif int(ch) == 5:

                      os.system("ssh {} aws ec2 describe-instances".format(remoteIP))

                      
                  elif int(ch) == 6:

                      
                      print("Enter Size : ",end = "")
                      size = input()
                      print("Enter availability zone : ",end = "")
                      zone = input()
                      print("Enter volume type : ",end= "")
                      vtype = input()
                      os.system("ssh {}  aws ec2 create-volume  --availability-zone {} --size {} --volume-type {}".format(remoteIP,zone,size,vtype))


                  elif int(ch) == 7:


                      os.system("ssh {} tput setaf 3".format(remoteIP))
                      print("\t\t\tVolume Zone & Instance Zone Must be same !!!")
                      print("\t\t\t--------------------------------------------")
                      os.system("ssh {} tput setaf 7".format(remoteIP))
                      print("Enter volume-id : ",end = "")
                      vid = input()
                      print("Enter instance-id : ",end = "")
                      iid = input()
                      print("Enter device : /dev/",end= "")
                      device = input()
                      os.system("ssh {}  aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/{} ".format(remoteIP,vid,iid,device))


                  elif int(ch) == 8:

                      print("Enter IP : ",end = "")
                      ip = input()
                      print("Enter key : ",end = "")
                      key = input()
                      print("Enter device : /dev/",end= "")
                      device = input()
                      os.system("ssh {}  ssh -l ec2-user {} -i {}.pem sudo fdisk /dev/{} ".format(remoteIP,ip,key,device))



                  elif int(ch) == 9:

                      os.system("ssh {} tput setaf 3".format(remoteIP))
                      print("\t\t\tHTTPD must be installed...")
                      print("\t\t\t--------------------------")
                      os.system("ssh {} tput setaf 7".format(remoteIP))
                      print("Enter IP : ",end = "")
                      ip = input()
                      print("Enter key : ",end = "")
                      key = input()
                      os.system("ssh {}  ssh -l ec2-user {} -i {}.pem sudo systemctl start httpd ".format(remoteIP,ip,key))


                  elif int(ch) == 10:

                      print("Enter IP : ",end = "")
                      ip = input()
                      print("Enter key : ",end = "")
                      key = input()
                      print("Enter Device : /dev/",end="")
                      device = input()
                      os.system(" ssh {} ssh -l ec2-user {} -i {}.pem sudo mkfs.ext4 /dev/{} ".format(remoteIPip,key,device))


                  elif int(ch) == 11:

                      print("Enter IP : ",end = "")
                      ip = input()
                      print("Enter key : ",end = "")
                      key = input()
                      print("Enter Device : /dev/",end="")
                      device = input()
                      os.system("ssh {}  ssh -l ec2-user {} -i {}.pem sudo mount /dev/{} /var/www/html/ ".format(remoteIP,ip,key,device))


                  elif int(ch) == 12:
                      exit()
                  elif int(ch)==13:
                      break
                      
                  else:
                      print("You Entered Wrong Choice ...")

      elif ch == 3:
          print("""********* WEB SERVER *************
                """)
          while True:
                  #os.system("ssh {} clear".format(remoteIP))
                  print("\t\t\t\t\t Webserver")
                  print("\t\t\t\t\t-----------")
                  print("""
                          Press 1: To install WebServer
                          Press 2: To copy code to required folder
                          Press 3: To start service of httpd
                          Press 4: To go to main menu
                          Press 5: Exit from program

                        """)
                  
                  ch = input(" Enter your choice : ")

                  if int(ch) == 1:
                      os.system("ssh {} yum install httpd -y".format(remoteIP))
                  elif int(ch) == 2:
                      os.system("ssh {} echo HelloWorld >> /var/www/html/test.html".format(remoteIP))
                  elif int(ch) == 3:
                      os.system("ssh {} systemctl start httpd".format(remoteIP))
                  elif int(ch) == 4:
                    break
                  elif int(ch) == 5:
                    exit()
                  else :
                    print("You entered wrong choice....")

      elif ch == 4:
          print("""********* HADOOP *************
                """)

          while True:
                  os.system("ssh {} clear".format(remoteIP))
                  print("\t\t\t\t\t HADOOP ")
                  print("\t\t\t\t\t--------")
                  print("""
                          Press 1: To start Hadoop namenode
                          Press 2: To view Hadoop filelist
                          Press 3: To stop Hadoop namenode
                          Press 4: To Start Hadoop datanode
                          Press 5: To View Hadoop fileslist
                          Press 6: To Stop Hadoop datanode
                          Press 7: To go to main menu
                          Press 8: Exit from program

                        """)
                  
                  ch = input(" Enter your choice : ")
                  
                  if int(ch) == 1:
                      os.system("ssh {} hadoop-daemon.sh start namenode".format(remoteIP))
                  elif int(ch) == 2:
                      os.system("ssh {} hadoop fs -ls /".format(remoteIP))	
                  elif int(ch) == 3:
                      os.system("ssh {} hadoop-daemon.sh stop namenode".format(remoteIP))
                  elif int(ch) == 4:
                      os.system("ssh {} hadoop-daemon.sh start datanode".format(remoteIP))
                  elif int(ch) == 5:
                      os.system("ssh {} hadoop fs -ls /".format(remoteIP))	
                  elif int(ch) == 6:
                      os.system("ssh {} hadoop-daemon.sh stop datanode".format(remoteIP))
                  elif int(ch) == 7:
                    break
                  elif int(ch) == 8:
                    exit()
                  else:
                    print(" You entered wrong choice....")

      elif ch == 5:
          print("""********* ANSIBLE *************
                """)
          
          while True:
                  #os.system("ssh {} clear".format(remoteIP))
                  print("\t\t\t\t\t Ansible")
                  print("\t\t\t\t\t---------")
                  print("""
                          Press 1: To install ansible 
                          Press 2: Create inventory directory 
                          Press 3: to configure ansible
                          Press 4: To go to main menu
                          Press 5: Exit from program

                        """)
                  
                  ch = input(" Enter your choice : ")

                  if int(ch) == 1:
                      os.system("ssh {} pip3 install ansible".format(remoteIP))
                  elif int(ch) == 2:
                      os.system("ssh {}  mkdir /etc/ansible".format(remoteIP))
                  elif int(ch) == 3:
                      os.system("ssh {} vi /etc/ansible/ansible.cfg".format(remoteIP))
                      os.system("ssh {} vi /etc/ansible/inventory.txt".format(remoteIP))
                  elif int(ch) == 4:
                    break
                  elif int(ch)== 5:
                    exit()
                  else: 
                    print("You entered wrong choice....")

      elif ch == 6:
          print("""********* DOCKER *************
                """)
          while True:
                  os.system("ssh {} clear".format(remoteIP))
                  print("\t\t\t\t\t DOCKER ")
                  print("\t\t\t\t\t--------")
                  print("""
                          Press 1: To Install Docker Service
                          Press 2: To start Docker Service
                          Press 3: To pull Webserver image
                          Press 4: To launch Webserver image
                          Press 5: To go to main menu
                          Press 6: Exit from program


                  """)

                  print("Enter Your Choice : ",end="")

                  ch=input()
                  
                  if int(ch) == 1:
                      os.system("ssh {} yum install docker-ce --nobest -y".format(remoteIP))
                  elif int(ch) == 2:
                      os.system("ssh {} systemctl start docker".format(remoteIP))
                  elif int(ch) == 3:
                      os.system("ssh {} docker pull anuddeeph/apache-webserver-php:latest".format(remoteIP))
                  elif int(ch) == 4:
                      os.system("ssh {} docker run -dit --name web anuddeeph/apache-webserver-php:latest".format(remoteIP))
                  elif int(ch) == 5:
                    break
                  elif int(ch) == 6:
                    exit()
                  else:
                    print("You entered wrong choice....")

      elif int(ch) == 7:
        break

      elif int(ch) == 8:
        exit()
      
      else:
        print("Your choise is wrong...")

    else:
          print("location doesn't support")
    input("enter to continue..")
      
