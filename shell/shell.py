import sys
import os

def main():
    while True:
        p = os.getcwd()+' $$$$' if 'PS1' not in os.environ else os.environ['PS1']
        os.write(1, p.encode())
        input = os.read(0, 128)
        input = input.decode()
        input_splitted = input.split()
        if input_splitted[0] == 'cd':
            os.chdir(input_splitted[1])
        if "exit" in input:
            print("Exiting")
            sys.exit(1)





if __name__ == '__main__':
    main()
