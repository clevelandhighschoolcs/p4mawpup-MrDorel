import time
import urllib
import re
import requests
from twilio.rest import Client

account_sid = 'AC767817a5c1ed3e223e922a4927f402f4'
auth_token = '4c36bb4c4ea20b9ee027df992ed49de5'
twilio_phone_number = '+19718034163'
my_phone_number = '+15035454979'

def main ():
	
	sec = 500
	timeT = 0

	while timeT < sec:
	
		print "Checking the current price of apple stock. This may take a few a few minutes..."
		time.sleep(5)
		htmlfile = urllib.urlopen("http://www.nasdaq.com/symbol/aapl/real-time")
		htmltext = htmlfile.read()
		regex = '<div id="qwidget_lastsale" class="qwidget-dollar">(.+?)</div>'	
		pattern = re.compile(regex)
		oldPrice = re.findall(pattern,htmltext)
		time.sleep(60)
		htmlfile = urllib.urlopen("http://www.nasdaq.com/symbol/aapl/real-time")
		htmltext = htmlfile.read()
		regex = '<div id="qwidget_lastsale" class="qwidget-dollar">(.+?)</div>'	
		pattern = re.compile(regex)
		newPrice = re.findall(pattern,htmltext)
		time.sleep(5)
		print " The current price of apple stock is: "
		print newPrice
		
		if newPrice != oldPrice:
			body = "---------------------Price changed!---------------------"
			print "The new Apple stock price is:"
			client = Client(account_sid, auth_token)
			client.messages.create(
			body=body,
			to=my_phone_number,
			from_=twilio_phone_number
			)
			
			oldPrice = newPrice
		
		else:
			print "The new Apple stock price is:"
			timeT +=1
			
		print newPrice
		
		if timeT < sec:
			print "Restarting...This may take a few seconds..."
		
		if timeT == sec:
			print "Ending process..."
		
		
	

main()




