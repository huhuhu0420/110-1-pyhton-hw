def ADD_W_FRONT(article: list, cmd: list):
    # cmd start from 1, n = word_index
    to_work_line, n, word = int(cmd[1]) - 1, int(cmd[2]), cmd[3]
    # sentence -> list, for ex: sentence = ['I', 'have', ...]
    sentence = article[to_work_line].split()
    print(sentence, article)

    # article[to_work_line] = ' '.join(sentence[ : n-1] + [word] + [n-1:])
'''    
def ADD_W_AFTER():
    
def ADD_S_FRONT():
    
def ADD_S_AFTER():
    
def INSERT_FRONT():

def INSERT_AFTER():
    
def DEL_W():
    
def DEL_L():
    
def REPLACE():
    
def COPY_L():
    
def COPY():
    
def PASTE_FRONT():
    
def PASTE_AFTER():
    
def COUNT():
'''


def call_back_function(function, article: list, command: list):
    function(article, command)


def main():
    queue = list()
    data = input().split()  # article_line = data[0], cmd_line = data[1]
    article = [str(input()) for article_line in range(
        int(data[0]))]  # article = ['line1', 'line2', ...]
    # print(article)
    command_list = [input().split() for command_line in range(
        int(data[1]))]  # command_list = [[line1], [line2], ...]
    # print(command_list)
    for command in command_list:  # command = which command + detailed manipulate, command -> list
        print(command)
        call_back_function(ADD_W_FRONT, article, command)


main()
