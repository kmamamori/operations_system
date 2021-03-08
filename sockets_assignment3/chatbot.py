import sys
import socket
import json
import traceback

class Bot:
    def __init__(self, reader):
        self.answer = ""
        self.reader = reader

    def start_conversation(self):
        self.answer = self.ask_question('gender')
        self.answer = self.ask_question('major')
        self.answer = self.ask_question('animal')
        self.send_animal_response()
    
    def ask_question(self, question):
        question = self.get_question_from_server(question)
        print(question)
        return self.reader.get_next_line()

    def get_question_from_server(self, question):
        request = dict()
        request['question'] = question
        request['prev_answer'] = self.answer
        request = json.dumps(request)
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("localhost", 7069))
        s.sendall(request.encode())

        return s.recv(256).decode()

    def send_animal_response(self):
        answer_list = self.answer.split(" ")
        print(answer_list[0], "awesome, but I hate", answer_list[-1])


class ConsoleReader:
    def __init__(self):
        pass
    
    def get_next_line(self):
        return input()

class FileReader:
    def __init__(self, filename):
        with open(filename) as f:
            content = f.readlines()
        self.file_lines = [x.strip() for x in content] 

    def get_next_line(self):
        return self.file_lines.pop(0)

def main():
    try:
        start_bot()
    except FileNotFoundError:
        print("File was not found")
    except IndexError:
        print("File has not enought lines to conversate")
    except BaseException:
        print("No valid arguments")
        traceback.print_exc()

def start_bot():
    reader = get_reader()
    bot = Bot(reader)
    bot.start_conversation()

def get_reader():
    if len(sys.argv) == 1:
        return ConsoleReader()
    
    if len(sys.argv) == 2:
        return FileReader(sys.argv[1])
    
    raise BaseException
    

main()