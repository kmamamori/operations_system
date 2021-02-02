import os
import sys

def main():
	cmds = [['cat', '/proc/cpuinfo'], ['echo', 'Hellow World'], ['python3', 'spinner.py', '1000000'], ['uname', '-a']]
	for cmd in cmds:
		rc = os.fork()
		if rc<0:
			print("Fork failed")
			sys.exit(1)
		elif rc == 0:
			print("\nI am child. My pid ==", os.getpid(), ".\nExecuting", cmd)
			os.execve('/usr/bin/'+cmd[0], cmd, os.environ)
		else:
			rc_wait=os.wait()
			print("I am parent. My pid ==", rc, ". Parent's pid ==", os.getpid())
	last_rc = os.fork()
	if last_rc > 0:
		print("I am parent. My pid ==", last_rc, ". Parent's pid ==", os.getpid())
		exit()
	else:
		print("\nI am child. My pid ==", os.getpid(), ".\nExecuting python3 spinner.py 2000000")
		os.execv('/usr/bin/python3', ['python3', 'spinner.py', '2000000'])

if __name__ == '__main__':
	main()
