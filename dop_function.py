#!/usr/bin/env python

from time import time
import sys
import numpy as np

def MSE(have, must):
	lens = len(have) - 1
	e = 0
	while lens >= 0:
		rz = have[lens] - must[lens]
		e += (rz * rz)
		lens -= 1
	e = e / len(have)
	return e

def RMSE(have, must):
	return (MSE(have, must)**0.5)

def load_theta():
	th0, th1 = 0, 0
	try:
		in_file = open('theta', "r")
	except:
		return 0,0,False

	zr = 0
	for line in in_file.readlines():
		try:
			float(line)
		except Exception as e:
			print 'No theta'
			return 0,0,False
		else:
			if zr == 0:
				th0 = float(line)	
			elif zr == 1:
				th1 = float(line)
			else:
				print 'No theta'
				return 0,0,False
			zr += 1
	return th0, th1, True


def save_theta(th0, th1):
	try:
		in_file = open('theta', "w")
	except:
		ERR('Error: cant read file: theta')
		sys.exit(1)

	in_file.write(str(th0) + '\n')
	in_file.write(str(th1))


def return_list():

	l_km, l_price = [],[]
	try:
		in_file = open('data.csv', "r")
	except:
		ERR('Error: cant read file: data.csv')
		sys.exit(1)

	for line in in_file.readlines():
		# print line
		try:
			line2 = line.split(',')
			int(line2[0])
			int(line2[1])
		except Exception as e:
			if line.find('km,price') != 0:
				print 'line != km,price'
				sys.exit(1)
		else:
			l_km.append(int(line2[0]))
			l_price.append(int(line2[1]))

	in_file.close()
	if len(l_km) == 0 or len(l_price) == 0:
		print '0 size'
		sys.exit(1)

	return l_km, l_price