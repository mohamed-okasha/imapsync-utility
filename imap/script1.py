#
# this script uses to automate trasferring emails
# create new file with name email_list then append all emails, one email per line 
# email_list file and script1.py must be in the same directory



from subprocess import Popen, PIPE
import os
import re

if os.path.exists("email_list")==False:
      print "\nThere is no file with name email_list in current directory \n please create new file with name email_list then append all emails ,email per line\n"
      exit()



# sync  linux <--> windows
command1="/usr/bin/imapsync --nosyncacls --subscribe_all --syncinternaldates --noauthmd5 --host1 source --user1 email --password1 p@ssw0rd --host2 distination--user2 email --password2 p@ssw0rd --sep2 . --prefix2 '' "

# sync  linux <--> linux
command="/usr/bin/imapsync --nosyncacls --subscribe --syncinternaldates --ssl1 --host1 source --user1 email --password1 p@ssw0rd  --noauthmd5 --host2 distination --ssl2 --user2 email --password2 p@ssw0rd  --noauthmd5"


print "\n1:Sync linux <--> windows\n2:Sync linux <--> linux\\zimpra \n"     

typec=input("Press 1 or 2 then press Enter:")
if typec=='2':
    command=command1

    



list_email=open("email_list","r").readlines()


password=str(raw_input("Please enter email password :"))
source=str(raw_input("Please enter source host ip :"))
distination=str(raw_input("Please enter distination host ip :"))


command=command.replace("p@ssw0rd",password)
command=command.replace("source",source)
command=command.replace("distination",distination)

list_failures={}
list_success=[]
print "Started sync\n"
for email in list_email:
    # you can redirect i/o stream to any pipe using 'Popen' but can not do that with 'call'
    p = Popen(command.replace("email",email.replace("\n","")).split(" "), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, err = p.communicate()

    #if re.match(r'Detected 0 errors',stdout) != None:
    if stdout.find('Detected 0 errors')==-1:
        list_failures[email]=err
    else:
        list_success.append(email)
        print email +" : " +source+"<->"+distination+" "+" sync ended\n"


print "\n-Summary-\n"
print "("+str(len(list_success))+ ") emails successed sync\n"

if len(list_failures) !=0:
   print "An error occurred while sync "+str(len(list_failures))+" emails "+"\n".join(list_failures.keys())


