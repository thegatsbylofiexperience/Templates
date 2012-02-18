#! /usr/bin/python
#This is a template file, the basis for all scripts written in python.
#Commenting is mandatory, as it will make it easier for others to understand your wacky choices another day


######IMPORTS######
import redis


######DIRECTORIES######


######CONSTANTS######
HOST_IP = "localhost";

######FUNCTIONS OR CLASSES######

	
##$##MAIN##$##
if __name__ == '__main__':
	redis = redis.Redis(HOST_IP);#Connect to redis server!
	

#####OLD or BAD CODE##### Check it down here with an explanation of why it is baaad (all quoted out too!)
