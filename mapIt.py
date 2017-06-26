#!/usr/bin/env python3
#! python3
#Launches google maps with the given location
import webbrowser, sys

print("Welcome to mapit. To open an address on google maps follow the sample: mapit 80 Valencia St San Francisco CA. To quit type mapit Quit")

while True:
	readString = input()
	address = ''.join(readString[6:])

	if(address == 'Quit'):
		break

	webbrowser.open('https://google.com/maps/place/'+address)
	print("Ready for next address")
