import re
import logging

myLogger = logging.getLogger("myLogger")


def run():
    read_log()
    read()
    parse()


def read_log():
    config_file = 'lab6.config'
    try:
        with open(config_file) as f:
            data = f.read()
            header = re.findall(r'\[.*]', data)

            content = re.findall(r'(.*)=(.*)', data)
            if len(header) == 3:
                liness = str(content[2]).split()[1][1:-2]
                separatorr = str(content[3]).split()[1][1:-2]
                filterr = str(content[4]).split()[1][1:-2]
                dic = {header[0]: content[0], header[1]: content[1],
                       header[2]: [int(liness), separatorr, filterr]}
                myLogger.setLevel(dic['[Config]'][1])
                print(myLogger.level)

                newDic = {'lines': int(liness),
                          'separator': separatorr, 'filter': filterr}

                print(newDic.items())
                name = dic['[LogFile]'][1]
                print(name)
    except FileExistsError:
        print("Config file is not present.")
        exit()
    bytes_counter(newDic['separator'], newDic['filter'])
    request('193.27.228.27', newDic['lines'])


def read():
    log_list = []
    try:
        with open('log_file') as f:
            for line in f:
                log_list.append(line)
        return log_list
    except FileExistsError:
        print("file not exist")
        exit()


def parse():
    parse_compare = re.compile(
        "(\\d{1,3}.\\d{1,3}.\\d{1,3}.\\d{1,3}) - - "
        "\\[(\\d{1,2}/[A-Z][a-z]{2}/\\d{4}:\\d{2}:\\d{2}:\\d{2} \\+\\d{4})] "
        "\"([A-Z]{3,7}) (.*[1-9]\" )(\\d{3}) (\\d{3})")
    tuples = []
    with open('log_file') as f:
        for line in f:
            match = re.search(parse_compare, line)
            if match:
                tuples.append(
                    (match.group(1), match.group(2),
                     match.group(3), int(match.group(5)),
                     int(match.group(6))))
        # for items in tuples:
        #     print(items)
        return tuples


def bytes_counter(seperator1, requestt):
    count = 0
    parse_compare = re.compile("(\\d{3}) (\\d{3})")
    with open('log_file') as f:
        for line in f:
            filterr = re.compile(requestt)
            header = re.search(filterr, line)
            if header is not None:
                match = re.search(parse_compare, line)
                if match is not None:
                    count = count + int(match.group(2))
    print({count}, {seperator1}, {requestt})


def request(ip_adress, lines):
    ip = '64.31.8.10'
    # '193.27.228.27'
    mask_length = 257312 % 16 + 8
    counter = -1
    n = 1
    with open('log_file') as f:
        for line in f:
            if ip_adress in line:
                counter += 1
                if n * lines == counter:
                    n += 1
                    input("Press any key to continue")

                print(line)
    print(mask_length)
    result = subnet(ip, ip_adress, mask_length)
    print(result)


def subnet(ip_adress, ip_adress2, subnett):
    i = '.'.join([bin(int(x) + 256)[3:] for x in ip_adress.split('.')])
    i2 = '.'.join([bin(int(x) + 256)[3:] for x in ip_adress2.split('.')])
    count = 0
    for item, nextitem in zip(i, i2):
        while count <= subnett:
            if item == nextitem:
                count += 1
            else:
                return False
    return True


if __name__ == '__main__':
    run()

# (venv) C:\Codes\ScriptLanguageLab\Lab_6>pycodestyle main.py
# main.py:25:80: E501 line too long (115 > 79 characters)
# main.py:28:80: E501 line too long (91 > 79 characters)
# main.py:53:80: E501 line too long (119 > 79 characters)
# main.py:61:80: E501 line too long (111 > 79 characters)
# main.py:93:80: E501 line too long (90 > 79 characters)

# I didn't get any output after i fixed the errors
#
