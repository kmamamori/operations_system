import os, sys

def main():
    while True:
        p = os.getcwd()+' $' if 'PS1' not in os.environ else os.environ['PS1']
        os.write(1, p.encode())
        input = os.read(0, 128)
        input = input.decode()
        if "exit" in input:
            print("Exiting")
            sys.exit(1)





if __name__ == '__main__':
    main()
