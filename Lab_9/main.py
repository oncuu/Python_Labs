import smtplib
import argparse
import datetime
import sys
import account
import requests
from bs4 import BeautifulSoup


def run():
    argument = argparse.ArgumentParser()
    argument.add_argument('--mail', help="Sending an email to the teacher")
    argument.add_argument('--cat-facts', help="How many facts ?")
    argument.add_argument('--teachers', help="Write a letter")
    args = argument.parse_args()
    if args.mail == "My message to the teacher":
        mail()
    if args.cat_facts is not None:
        cats(args.cat_facts)
    if args.teachers is not None:
        researchers(1, args.teachers)


def mail():
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        mail_id = account.mail_id
        password = account.password
        print(f'You are sending from {mail_id}')
        smtp.starttls()
        smtp.ehlo()
        smtp.login(mail_id, password)
        print('Please write the reciever id : ')
        reciever = input()
        print('Please write your subject: ')
        subject = input()
        print('Please write your message: ')
        body = input()
        From = 'Berke Kaan Oncu'
        To = 'Wojciech Thomas'
        msg = f"Subject: {subject}\n{body}\n\nFrom: {From}\nTo :{To}\n{datetime.datetime.today().strftime('%H:%M  %d/%m/%Y')}"
        smtp.sendmail(mail_id, reciever, msg)
        print(f'Mail send it!\n{msg}')


def cats(number):
    cat_fact = requests.get('https://cat-fact.herokuapp.com/facts')
    new_list = []
    counter = 0
    for facts in cat_fact.json():
        new_list.append(facts['text'])
    if int(number) > len(new_list) or int(number) < 0:
        print(f"Sorry but cats doesn't have {number} fact/facts")
        sys.exit()
    else:
        while counter < int(number):
            print(new_list[counter])
            counter += 1


def researchers(page_number, letter):
    names = []
    mail_list = []
    while page_number <= 10:
        page = requests.get('https://wiz.pwr.edu.pl/pracownicy/page' + str(page_number) + '.html?letter=' + letter)
        if page.status_code == 200:
            page.raise_for_status()
            content = BeautifulSoup(page.text, 'html.parser')

            home_links = content.find(class_='home')
            home_links.decompose()

            top_links = content.find(class_='row columns clearfix')
            top_links.decompose()

            researcher_name_list = content.find(class_='row columns').find(class_='column-content')
            researcher_name_list_items = researcher_name_list.find_all(class_="title")
            mail_list_items = researcher_name_list.find_all('p')

            for researcher_name in researcher_name_list_items:
                names.append(researcher_name.contents[0])

            for mail_add in mail_list_items:
                mail_list.append(mail_add.contents[0])

            for name, email in zip(names, mail_list):
                print(f'{name}, {email}')
        page_number += 1


if __name__ == '__main__':
    run()
