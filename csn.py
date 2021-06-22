import requests
import re
from datetime import date
from prettytable import PrettyTable
from requests.sessions import session
from time import sleep
from os.path import isfile
from function import *


details = ''
if isfile('details.txt'):
    print('[*] details.txt file found.')
    with open('details.txt', 'r') as details_f:
        details = details_f.readlines()

else:
    print('[-] details.txt file not found.')
    exit()


print('[*] Starting Program.....')

try:
    print('[*] Found following details in details.txt!')
    age_limit = int(re.search('(?:age_limit:)(\d\d)', details[0]).group(1))
    print(f'[1] MINIMUM AGE LIMIT : {age_limit}')
    pincode = re.search('(?:pincode:)(\d\d\d\d\d\d)', details[1]).group(1) 
    print(f'[2] PINCODE : {pincode}')
    date = re.search('(?:date:)(\d\d\-\d\d\-\d\d\d\d)', details[2]).group(1) 
    print(f'[3] DATE : {date}')
    delay = int(re.search('(?:delay:)(\d+)', details[3]).group(1)) 
    print(f'[4] DELAY (in s): {delay}')
    sleep(3)

except Exception as e:
    print('[-] An Exception Occurred!!',e)
    print('[*] Exiting Program')
    exit()


API = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={date}'


wanna_check = True
while wanna_check:
    try:
        clrscr()

        eligible_centers_count = 0
        
        slots_data = requests.get(API).json()
        sessions = slots_data['sessions']
        total_centers = len(sessions)

        ### for table ###
        table = PrettyTable()
        table.field_names = ['Center ID', 'Name', 'Address', 'Time', 'Min Age Limit'] 

        for session in sessions:
            if age_limit == session['min_age_limit']:
                eligible_centers_count += 1
                table.add_row([session['center_id'], session['name'], session['address'], f"{session['from']}-{session['to']}", session['min_age_limit']])

        # print data
        print('[*] Total Centers Available: ', total_centers)
        print('[*] Eligible Centers Count : ', eligible_centers_count)

        if eligible_centers_count != 0:
            print(table)
            notify(eligible_centers_count)
        
        else:
            print('[-] No slots available, according to specified details.')
            print(table)

        print('[*] Press Control+C simultaneously to exit.')
        sleep(delay)

    except KeyboardInterrupt:
        print('[-] Keyboard Interrupt Detected! ')
        wanna_check = False

    except Exception as e:
        print('[-] An Exception Occurred!')
        print(e.with_traceback())
        print('[*] Exiting Program...')
        exit()
        

print('\n[*] Thank You For using COWIN SLOT NOTIFIER...')
print('\n[*] This program is written by DHRUMIL MISTRY')
