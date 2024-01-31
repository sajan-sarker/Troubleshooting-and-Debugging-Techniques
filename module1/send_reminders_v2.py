#!/usr/bin/env python3

import csv, email, smtplib, sys
import datetime

def usage():
    print("Send_reminders: Send meeting reminders")
    print()
    print("Invocation: ")
    print("    send_reminders 'date | Meeting Title | Emails' ")
    return 1


def dow(date):
    dateobj = datetime.datetime.strptime(date, r"%Y-%m-%d")
    return dateobj.strftime("%A")

def message_template(date, title):
    message = email.message.EmailMessage()
    weekday = dow(date)
    message['Subject'] = f'Meeting reminder: "{title}"'
    message.set_content(f'''
Hi all!
This is a quick mail to remind you all that we have a meeting about: 
"{title}".
On {weekday}, {date}.

See you there.
''')
    
    return message

def get_name(contacts):
    names = {}
    with open(contacts) as file:
        reader = csv.reader(file)
        for row in reader:
            names[row[0]] = row[1]
    return names

def send_message(date, title, emails, contacts):
    smtp = smtplib.SMTP('localhost')
    names = get_name(contacts)
    for email in emails.split(','):
        name = names[email]
        name = get_name(contacts, email)
        message = message_template(date, title, name)
        message['From'] = 'noreply@example.com'
        message['To'] = email
        smtp.send_message(message)
    smtp.quit()
    pass

def main():
    if len(sys.argv) < 2:
        return usage()
    
    try:
        try:
            date, title, emails = sys.argv[1].split('|')
            print(f"Message Format is: Date - {date}, Title - {title}, Emails are - {emails}")
        except:
            print("Unpacking Failed!")
            sys.exit(0)
        message = message_template(date, title)
        print(message)
        send_message(message, emails)
        print("Successfully sent reminders to: ", emails)
    except Exception as e:
        #print("Failure to send email", file=sys.stderr) 
        print("Failure to send email with: {}".format(e), file=sys.stderr) 
if __name__ == "__main__":
    main()