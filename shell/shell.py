import os, sys

def main():
    while True:
        input = os.read(0, 128)
        print(input)
        input = input.decode()
        print(input)
        print("abc")
        if "exit" in input:
            print("Exiting")
            sys.exit(1)





if __name__ == '__main__':
    main()
