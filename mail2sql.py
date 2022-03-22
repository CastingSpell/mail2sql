# Libraries needed
from os import SEEK_DATA
from imap_tools import MailBox, AND
import re, pymysql

# Database connection
db = pymysql.connect(host="dbserver", user="root", passwd="root", database="database")

# Infinite loop for listening to new mails
while True:
    with MailBox('mail.domain.com').login('user@domain.com', 'password') as mailbox:
        new_mail = mailbox.idle.wait(timeout=10)
        if new_mail: # If a new mail is received we parse it, looking for the id and the data
            for msg in mailbox.fetch(criteria=AND(seen=False, from_="sender@domain.com"), mark_seen=True, bulk=True):
                id = re.findall(r'local\s(\d+)', msg.text)[0]
                data = re.findall(r'CIST-\d{2}-\w{2}-\d{4}\sa\sT(\d)\s\(\w+\)\s=>\s(\d{3}.\d)\sL.', msg.text)

            # Cursor creation and data insertion for each parsed element from the mail
            c = db.cursor()
            for i in data:
                tank, liters = i[0], i[1]
                c.execute("""INSERT INTO table (dev_id, tank_num, litros, consumo) values (%s, %s, %s, %s)""", (id, tank, liters, liters))
                print(f'In the local {id} the tank {tank} has been filled with {liters} liters')

            # Database commit
            db.commit()