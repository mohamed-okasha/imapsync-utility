#
# this script uses to automate trasferring emails
# create new file with name email_list then append all emails, one email per line 
# email_list file and script1.py must be in the same directory



from subprocess import call
import os

if os.path.exists("email_list")==False:
      print "\nThere is no file with name email_list in current directory \n please create new file with name email_list then append all emails ,email per line"
      exit()



list_email=open("email_list","r").readlines()

password=str(input("Please enter password email:"))
source=str(input("Please enter source host ip :"))
distination=str(input("Please enter distination host ip :"))

command="/usr/bin/imapsync --nosyncacls --subscribe_all --syncinternaldates --noauthmd5 --host1 source --user1 email --password1 p@ssw0rd --host2 distination--user2 email --password2 p@ssw0rd --sep2 . --prefix2 '' "

command=command.replace("p@ssw0rd",password)
command=command.replace("source",source)
command=command.replace("distination",distination)

for cmd in list_email:
    call(command.replace("email",cmd.replace("\n","")).split(" "))
    


