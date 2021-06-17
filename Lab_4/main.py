def run():
    log = read_log()
    requests_count = ip_request_number(log)
    max_req_ip, max_req_count = ip_find(requests_count)
    longest_req = longest_request(log)
    missing_resources = non_existent(log)

    print('Requests Count: ')
    print(requests_count)
    print('Maximum Request and Count:')
    print(f"{max_req_ip}: {max_req_count}")
    # print(f'Minimum Request and Count: Count = {max_req_count}')
    # print(max_req_ip)
    print('Longest Request: ')
    print(longest_req)
    print('Missing Resources')
    print(missing_resources)

def read_log():
    log = {}
    with open('log', 'r') as logFile: #'r' = reading / 'w' = writing
        lines = logFile.readlines()
        for line in lines:
            tokens = line.split()
            ip = tokens[0]
            date = tokens[3]
            date_time = tokens[4]
            log[ip + ' ' + date + ' ' + date_time] = line
        #
    return log

def ip_request_number(log):
    lines = log.values()
    ip_request = {}
    for line in lines:
        ip = line.split(' ')[0]
        if ip in ip_request:
            #if ip did any request its adding on the counter otherwise its starting with 1
            ip_request[ip] += 1
        else:
            ip_request[ip] = 1
    return ip_request

def ip_find(request_count, most_active = True):
    if most_active:
        maxi = 0
        address = ''
        for key, count in request_count.items():
             if count > maxi:
                maxi = count
                address = key
        return address, maxi

    mini = 99999
    ip_list = []
    for key, count in request_count.items():
        if count <= mini:
            mini = count
            address = key
            ip_list.append(address)
    return ip_list, mini

def longest_request(log):
    result = ()
    lines = log.values()
    max = 0
    for line in lines:
        header = line.split('"')[1]
        if max < len(header):
            max = len(header)
            result = (line.split(' ')[0], header)
    return result

def non_existent(log):
    lines = log.values()
    error_list = []
    for line in lines:
        response = line.split(' ')[8]
        req_string = line.split('"')[1]
        if response == '404':
            error_list.append(req_string)
    return set(error_list)


if __name__ == '__main__':
    run()