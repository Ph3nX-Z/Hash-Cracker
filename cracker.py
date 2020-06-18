import hashlib
import binascii
import os
import platform
import os
import time
a="""
 ▄  █ ██      ▄▄▄▄▄    ▄  █     ▄█▄    █▄▄▄▄ ██   ▄█▄    █  █▀ ▄███▄   █▄▄▄▄ 
█   █ █ █    █     ▀▄ █   █     █▀ ▀▄  █  ▄▀ █ █  █▀ ▀▄  █▄█   █▀   ▀  █  ▄▀ 
██▀▀█ █▄▄█ ▄  ▀▀▀▀▄   ██▀▀█     █   ▀  █▀▀▌  █▄▄█ █   ▀  █▀▄   ██▄▄    █▀▀▌  
█   █ █  █  ▀▄▄▄▄▀    █   █     █▄  ▄▀ █  █  █  █ █▄  ▄▀ █  █  █▄   ▄▀ █  █  
   █     █               █      ▀███▀    █      █ ▀███▀    █   ▀███▀     █   
  ▀     █               ▀               ▀      █          ▀             ▀    
       ▀                                      ▀                              
Only for MD5 / SHA1 / NTLM
By Ph3nX-Z : https://github.com/Ph3nX-Z/
"""
print(a)
def load():
    f=open("10millions.txt","r")
    wordlist=f.read()
    f.close()
    return wordlist

def crackermd5(hash_in,wordlist):
    for word in wordlist.split('\n'):
        result = hashlib.md5(word.encode())
        #print("Hash : {}".format(result.hexdigest()))
        if result.hexdigest()==hash_in:
            return word
    return ""

def crackersha1(hash_in,wordlist):
    for word in wordlist.split('\n'):
        result = hashlib.sha1(word.encode())
        #print("Hash : {}".format(result.hexdigest()))
        if result.hexdigest()==hash_in:
            return word
    return ""

def crackerntlm(hash_in,wordlist):
    for word in wordlist.split('\n'):
        result = hashlib.new('md4', word.encode('utf-16le')).digest()
        if binascii.hexlify(result).decode("utf8")==hash_in:
            return word
    return ""

type_of_hash=input("Type of hash :")
hash_to_crack=input("Your {} Hash :".format(type_of_hash))
wordlist=load()


password=crackersha1(hash_to_crack,wordlist)

password2=crackermd5(hash_to_crack,wordlist)

password3=crackerntlm(hash_to_crack,wordlist)


if password != "":
    print("[+] Password sha1 :{}".format(password))
else:
    print("[-] Password sha1 : Not Found")

time.sleep(2)


if password2 !="":
    print("[+] Password md5 :{}".format(password2))
else:
    print("[-] Password md5 : Not Found")

time.sleep(2)

if password3 !="":
    print("[+] Password ntlm :{}".format(password3))
else:
    print("[-] Password ntlm : Not Found")

time.sleep(2)
p=open("cracked.txt",'a')
to_write="Hash : "+str(hash_to_crack)+" sha1: "+str(password)+" md5: "+str(password2)+" ntlm: "+str(password3)+"\n"
p.write(to_write)
p.close()
print("[+] Ended")
print("[/] Logs in Cracked.txt")