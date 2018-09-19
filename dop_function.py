#!/usr/bin/env python3
########PYTHON2

from time import time
import sys
import numpy as np
import tkinter as T
# import Tkinter as T 2
def ERR(st):
	print(st)
	sys.exit(1)

def predict(l_km, th0, th1):
	lst = []
	for i in l_km:
		lst.append(estimatePrice(i, th0, th1))
	return lst
def estimatePrice(mileage,th0, th1):
	return th0 + (th1 * mileage)

def trainModel(l_km, l_price, learningRate,th0, th1):
	lens = len(l_km)
	sums0 = 0
	sums1 = 0
	i = 0
	while i < lens:
		tmp = estimatePrice(l_km[i], th0, th1) - l_price[i]
		sums0 += tmp
		sums1 += (tmp * l_km[i])
		i += 1

	th0 = learningRate * (sums0/i)
	th1 = learningRate * (sums1/i)

	return th0, th1


def graph(l_km, l_price, th0, th1):
	root = T.Tk()
	canv = T.Canvas(root, width = 1000, height = 1000, bg = "lightblue")
	canv.create_line(3,1000,3,0,width=2,arrow='last') 
	canv.create_line(0,997,1000,997,width=2,arrow='last')
	maxx_km = max(l_km)
	minn_km = min(l_km)
	maxx_price = max(l_price)
	minn_price = min(l_price)
	
	rz = maxx_km - minn_km
	rz /= 20
	i = 10
	start = minn_km
	while start < maxx_km-rz-1:
		canv.create_text(30,i,text = int(start))
		canv.create_line(0,i,6,i,width=2, fill = 'black')
		start += rz
		i += 50

	rz = maxx_price - minn_price
	rz /= 10
	i = 100
	start = minn_price + rz
	while start < maxx_price:
		canv.create_text(i,980,text = int(start))
		canv.create_line(i,994,i,1000,width=2, fill = 'black')
		start += rz
		i += 100

	lens = len(l_price)
	i = 0
	while i < lens:
		y = (float(l_km[i] - minn_km) / (maxx_km - minn_km))*1000
		x = (float(l_price[i] - minn_price) / (maxx_price - minn_price))*1000
		canv.create_oval(x, y, x + 10, y + 10, fill = 'black')
		i += 1
	
	pr = predict(l_km, th0, th1)
	maxx_price = max(pr)
	minn_price = min(pr)
	lens = len(l_price)
	i = 0
	lsty = []
	lstx = []
	while i < lens:
		y = (float(l_km[i] - minn_km) / (maxx_km - minn_km))*1000
		x = (float(pr[i] - minn_price) / (maxx_price - minn_price))*1000
		lsty.append(y)
		lstx.append(x)
		i += 1
	minx = lstx.index(min(lstx))
	maxx = lstx.index(max(lstx))

	canv.create_line(lstx[minx],lsty[minx],lstx[maxx],lsty[maxx],width=5, fill = 'orange')
	canv.pack()
	root.mainloop() 

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
			print('No theta')
			return 0,0,False
		else:
			if zr == 0:
				th0 = float(line)	
			elif zr == 1:
				th1 = float(line)
			else:
				print('No theta')
				return 0,0,False
			zr += 1
	return th0, th1, True


def save_theta(th0, th1):
	try:
		in_file = open('theta', "w")
	except:
		ERR('Error: cant read file: theta')

	in_file.write(str(th0) + '\n')
	in_file.write(str(th1))
	in_file.close()


def return_list_from_data(name_csv):

	l_x, l_y = [],[]
	try:
		in_file = open(name_csv, "r")
	except:
		ERR('Error: cant read file:' + name_csv)
	num_str = 0
	frst = 0
	for line in in_file.readlines():
		try:
			line = line.split(',')
			int(line[0])
			int(line[1])
		except Exception as e:
			if frst != 0:
				ERR('Error: num str = ' + str(frst + 1))
			num_str += 1
		else:
			l_x.append(int(line[0]))
			l_y.append(int(line[1]))
		frst += 1
	in_file.close()
	if len(l_x) == 0 or len(l_y) == 0 or len(l_y) != len(l_x):
		ERR('Error: zero size')
	return l_x, l_y