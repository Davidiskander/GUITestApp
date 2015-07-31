__author__ = 'davidiskander'

import os
import glob
import gspread
import json
from oauth2client.client import SignedJwtAssertionCredentials
from datetime import datetime
from random import randint
import sys
from sys import argv
from os.path import exists
import csv
import time

json_key = json.load(open('Parsing-1e6baa42f1a3.json'))
scope = ['https://spreadsheets.google.com/feeds']

def oauth_login():
		print "Logging into Google"
		credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
		gc = gspread.authorize(credentials)
		sh = gc.open("ParsingLogsReport")

		todays_date = datetime.today().strftime("%m/%d/%Y")
		global worksheet
		worksheet = sh.add_worksheet(title=todays_date, rows="1000", cols="20")

		title_row = {
			'A1': '#',
			'B1': 'Notification Type',
			'C1': 'Notification ID',
			'D1': 'Info',
			'E1': 'Datetime Sent',
			'F1': 'Received',
			'G1': 'Errors'
		}

		for cell, title in title_row.items():
			worksheet.update_acell(cell, title)

def create_new_csv():
		global current_csv_file
		current_csv_file = 'logs_{}.csv'.format(datetime.today())

def add_to_csv(notifications_test):

		with open(current_csv_file.format(datetime.today()), 'a') as csvfile:
			blargh = csv.writer(csvfile)
			blargh.writerow(notification_test)

def add_to_google_sheet():
		print "Logging Data onto Google Sheet"

		with open(current_csv_file, 'rb') as csvfile:
			blargh = csv.reader(csvfile)
			for row in blargh:
				number = worksheet.col_values(1)
				notification_type = worksheet.col_values(2)
				notification_id = worksheet.col_values(3)
				info = worksheet.col_values(4)
				datetime_sent = worksheet.col_values(5)
				received_notifications = worksheet.col_values(6)
				errors = worksheet.col_values(7)

				column_array = [number, notification_type, notification_id, info, datetime_sent, received_notifications, errors]
				for index, column_name in enumerate(column_array):
					row_num_of_next_empty_cell = len(column_name) + 1
					col_num = index + 1
					worksheet.update_cell(row_num_of_next_empty_cell, col_num, row[index])

def create_new_txt_file():
    print('Creating new text file')

    name = input('Enter the new file name: ')+'.txt'

    try:
        file = open(name,'r+')   # Trying to create a new file or open one
        file.close()

    except:
        print('Something went wrong! Can\'t tell what?')
        sys.exit(0) # quit Python

def run_script():
	notif_id = 0
	device_id= ['*_H3C88AED8BABDC0F34DC_*.txt', '*_H33B116C5459404C247A_*.txt']

	print "/Users/davidiskander/Desktop/Parse/5"
	path = raw_input('what\'s the logs directory ?\n')

	for id in device_id:
		print "Device: %s" % id
		print " Ready to parse files for Device %s, hit RETURN" %id
		raw_input()
		for txtfile in glob.glob(os.path.join(path, id) ):
			with open(txtfile, 'rU') as f:
				lines = f.readlines()

				for line in lines:
					if ("NOTIF:alloc/id:" in line):
						print "\n|Notification ID: %s\t|Arrived at: %s\t|" %(line [-10:-1] , line[:20]),
					if ('NOTIF:attrec:Test' in line):
						print "Type: Meeting\t| Preparing! \t | Info: %s\t|" %line[-9:-1],
					if ("+1 (408) 606-2975" in line):
						print "Type: SMS \t| Preparing! \t|",
					elif ('NOTIF:post:/id' in line):
						print "Sent \t|",
					elif ('err_code:3' in line):
						print "Fail; error_3",
					elif ('err_code:4' in line):
						print "Fail; error #4",
					elif ('err_code:5' in line or  'err_code:7' in line):
						print "Fail; error #5&7",


		print "\n"

run_script()

"""
Future Plan:
-use Parse Rest API, to grab the recent logs
-create a new file to copy each device logs in
-sort logs by date and time; to avoid disordered results
-delete all files after test is over
"""