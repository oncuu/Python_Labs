import json
import logging

def run():
    file = read_log()
    # print_all_request(file)
    # web_server_log_request(file)

def read_log():
    log = []
    test = []
    j_file = 'log.json'
    tokens = ['file', 'request', 'level', 'log_lines', 'my_parameters']
    try:
        with open(j_file) as logFile:
            try:
                try:
                    read_data = json.load(logFile)
                except NameError:
                    print("File name does not exist")
                new_logger = logging.getLogger()
                new_logger.setLevel(read_data['level'])
                try:
                    for token in tokens:
                        if token not in read_data:
                            raise ValueError
                except ValueError:
                    print("Value error")
                log_test = open(read_data['file'])
                for line in log_test.readlines():
                    requests = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'TRACE', 'OPTIONS', 'CONNECT', 'PATCH']
                    for word in requests:
                        if word in line and 'index.xml' in line:
                            # if 'index.xml' in line:
                                request_header = line.split('"')
                                test.append(request_header[1].split('/'))

                for line in test:
                    word = line[1].split(" ")
                    line[1] = word[0]
                    line[2] = word[1]
                    log.append(line[0] + line[1])
                for line in log:
                    print(line)
            except IOError:
                print("Its not a proper json file")
    except FileNotFoundError:
        print("File not found")

    return read_data

# def print_all_request(file):
#     number = int(file['log_lines'])
#     request = file['request']
#     print(number)
#     line_list = []
#     counter = -1
#     n = 1
#     log_test = open('log')
#     for line in log_test:
#         if request in line:
#             line_list.append(line)
#     for line in line_list:
#         counter += 1
#         if n * number == counter: #when the counter is equal to multiplication of number by 1 ,2 ,3 ...
#             n += 1
#             input("If you want to continue to see the lines please press any key")
#         print(line)
#     print("------------------------------------------------------------------------------")
#
#
# def web_server_log_request(file):
#     os = file['my_parameters']
#     request = file['request']
#     os_list = []
#     for line in open(file['file']):
#         if os and request in line:
#             os_list.append(line)
#     for line in os_list:
#         print(line)





if __name__ == '__main__':
    run()
