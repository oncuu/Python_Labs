import logging

def main():
    userInput = input("Please write the location")
    maxi = 0
    largest_resource = []
    failed_reqs = 0
    total_size = 0
    total_proc_time = 0
    count = 0
    try:
        with open(userInput) as file:
            read_data = file.readlines()
            for line in read_data:
                tokens = line.split(' ')
                size = int(tokens[2])
                if size > maxi:
                    maxi = size

                    largest_resource = tokens
                total_proc_time += int(tokens[3])
                count += 1

                if tokens[1][0] == '4':
                    failed_reqs += 1
                    logging.warning('!' + tokens[0])
                else:
                    total_size += size

                    logging.info(tokens[0])

    except Exception as e:
        logging.debug(e)
    logging.debug('Largest resource path: ' + largest_resource[0] + " and processing time " + largest_resource[3])
    print('Number of failed requests: ' + str(failed_reqs))
    logging.info('Number of bytes sent to user: ' + str(total_size))
    logging.info('Number of kilobytes sent to user: ' + str(total_size/1000))
    logging.info('Average processing time: ' + str(total_proc_time/count))

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Program starting...')
    main()
    logging.info('Program ending...')


# https://docs.python.org/3/library/logging.html
# https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook
# https://docs.python.org/3/howto/logging.html#logging-basic-tutorial