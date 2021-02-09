import sys

class FileReader:
    def __init__(self, filename):
        with open(filename) as f:
            content = f.readlines()
        self.file_lines = [x.strip() for x in content]

    def get_next_line(self):
        return self.file_lines.pop(0)


print('a')
if len(sys.argv) == 1:
    print('greater than 1')
if len(sys.argv) == 2:
    f = FileReader(sys.argv[1])
    c = 27
    while c>0:
        cv = f.get_next_line()
        if cv != "":
            if cv[0] != "#":
                cv = cv.split()
                print(cv[0])
        c-=1
print(sys.argv[1])
