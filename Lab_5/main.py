import json

def main():
    file = input("What is name of the webserver log ?")
    test = False
    requests = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'TRACE', 'OPTIONS', 'CONNECT', 'PATCH']
    http = ""
    while not test:
        print(f'Please chose any request type from the list {requests}')
        http = input("Enter any request:")
        if http in requests:
            test = True
        else:
            print("Please write valid request")
    test = False
    level = ""
    levels = ["DEBUG", "INFO", "ERROR", "WARNING", "ERROR", "CRITICAL"]
    while not test:
        print(f"Please chose which logging level you want {levels}")
        level = input("Enter logging level:")
        if level in levels:
            test = True
        else:
            print("Please chose valid logging level")
    test = False
    log_lines = ""
    log_line = ['0', '1']
    while not test:
        log_lines = input("Please write how many lines you want:")
        if log_lines in log_line:
            print("Please write higher number")
            test = False
        else:
            test = True
    test = False

    my_parameters = ['Windows', 'Macintosh', 'Ubuntu']
    while not test:
        print(f"Please write any of this {my_parameters} os system")
        my_parameter = input("os system :")
        if my_parameter in my_parameters:
            test = True
        else:
            print("Please chose correct os system")

    config = {
        'file': file,
        'request': http,
        'level': level,
        'log_lines': log_lines,
        'my_parameters': my_parameter
    }
    print(config)
    j_file = 'log.json'
    with open(j_file, 'w') as f:
        json.dump(config, f)

if __name__ == '__main__':
    main()