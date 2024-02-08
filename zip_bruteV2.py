from zipfile import ZipFile
from colorama import Fore


zf = input("Enter password proteccted zip file name to crack : ")
file = input("Enter filename to use it as password list : ")
zf = ZipFile(zf)

with open(file,'r') as f:
	for i in f:
		try:
			i = i.strip()
			zf.extractall(pwd=bytes(i,'utf-8'))
		except:
			print(Fore.RED + "[-] Trying password : ",i)
		else:
			print(Fore.GREEN + "[+] password found :",i)
			print("Extracting data ........")
			break
	else:
		print("Password not found !!try other wordlist :/")
