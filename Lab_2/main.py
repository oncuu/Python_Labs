import logging
import sys

def run():
   read_log()

def read_log():
    count = 0
    entries = 0
    #entries are lines containing a data, non empty lines
    list = []
    for read_data in sys.stdin:
        try:
            if len(read_data.split()) == 0:
                count += 1
                continue
            tokens = read_data.split(' ')
            count += 1
            entries += 1
            test = (tokens[0], int(tokens[1]), int(tokens[2]), int(tokens[3]))
        #tokens[0] = path , tokens[1] = HTML , tokens[2] = size , tokens[3] = time
            list.append(test)
        except Exception as e:
            logging.error("file couldn't find")
    logging.debug(f"Number of lines {count} ")
    logging.debug(f"Number of entries {entries} ")
    successful_reads(list)
    failed_reads(list)
    html_entries(list)
    print_html_entries(list)
    return list

def successful_reads(list1):
    list = []
    for tokens in list1:
        if tokens[1] > 199  and tokens[1] < 300 :
            list.append(tokens[1])
    logging.info(f"Correct entries 2xx: {len(list)}")
    return list

def failed_reads(list2):
    list = []
    list1 = []
    for tokens in list2:
        if tokens[1] > 399 and tokens[1] < 500:
            list.append(tokens[1])
        elif tokens[1] > 499 and tokens[1] < 600:
            list1.append(tokens[1])
    NewList = [list + list1]
    logging.info(f"Wrong entries 4xx :{len(list)} , 5xx: {len(list1)}")
    return NewList

def html_entries(list3):
    list = []
    for tokens in list3:
        if ".html" in tokens[0]:
            list.append(tokens)
    return list

def print_html_entries(entries):
    print(html_entries(entries))

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Program started...')
    run()
    logging.info('Program ending...')
