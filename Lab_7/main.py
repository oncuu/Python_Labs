import re
from datetime import datetime

regex_pars = re.compile(
    '(\d{1,3}.\\d{1,3}.\d{1,3}.\d{1,3}) - - \[(.*)] '
    '"([A-Z]{3,7}) (\/.*.[a-z]+) (\W*(HTTP)\W*\d.\d)" (\d{1,3}) (\d{1,3}) ')


def run():
    first_date = datetime_test('23/Oct/2020:18:28:41 +0200')
    second_date = datetime_test('24/Oct/2020:02:00:38 +0200')
    My_line = '185.191.171.41 - - [18/Oct/2020:01:30:43 +0200] "GET /robots.txt HTTP/1.1" 404 196 "-" ' \
              '"Mozilla/5.0 (compatible; SemrushBot/6~bl; +http://www.semrush.com/bot.html)"'
    My_Http_Request = HttpRequest(My_line)
    My_Log_Entry = LogEntry(My_line)
    My_log_object = return_log_entry_object(My_line)
    My_list_object = list_log_entry_object()
    check_two_argument(first_date, second_date)


def read_log():
    log_file = 'Log_file'
    logs = []
    with open(log_file) as f:
        read_file = f.readlines()
        for lines in read_file:
            logs.append(lines)
    return logs



def datetime_test(date):
    datetime_string = "%d/%b/%Y:%H:%M:%S %z"
    return datetime.strptime(date, datetime_string)


class HttpRequest:
    def __init__(self, line):
        regex = re.match(regex_pars, line)

        self.method = regex.group(3)
        self.resource = regex.group(4)

    def __str__(self):
        return f'Request type: {self.method} Resource: {self.resource}'

    def return_method(self):
        return self.method

    def return_resource(self):
        return self.resource


class LogEntry:
    def __init__(self, lines):
        regex = re.match(regex_pars, lines)
        if regex:
            self.ip = regex.group(1)
            self.time = datetime_test(regex.group(2))
            self.method = regex.group(3)
            self.resource = regex.group(4)
            self.status = regex.group(5)
            self.response_size = regex.group(6)
        else:
            raise MalformedHttpRequest

    def return_date(self):
        return self.time

    def __repr__(self):
        return f'Ip address: {self.ip} Date and time: {self.time} Request type: {self.method} Resource: {self.resource} Status: {self.status} Size of response: {self.response_size}'


def return_log_entry_object(line):
    return LogEntry(line)


def list_log_entry_object():
    list_log = []
    for lines in read_log():
        try:
            list_log.append(LogEntry(lines))
        except MalformedHttpRequest:
            continue
    return list_log


class MalformedHttpRequest(Exception):
    pass


def check_two_argument(first_date: datetime, second_date: datetime):
    if second_date < first_date:
        print(f'{first_date} is before than {second_date}, please check it again')
    else:
        for requests in list_log_entry_object():
            if second_date > requests.return_date() > first_date:
                print(requests)


if __name__ == '__main__':
    run()
