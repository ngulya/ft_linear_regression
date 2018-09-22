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

def estimatePrice(mileage,th0, th1):
	return th0 + (th1 * mileage)


def predict(x, th0, th1):
	lst = []
	for i in x:
		p =  th0 + (th1 * i)
		lst.append(p)
	return lst



def predict_MSE(x,y, th0, th1):
	ans = 0
	i = 0
	lens = len(x)
	while i < lens:
		p =  th0 + (th1 * x[i])
		ans += (p-y[i])**2
		i += 1

	return ans / i



def from_input_to_int():
	learning_rate = 0.1
	bad = True
	while bad:
		# tmp = raw_input('\ninput learning rate > 0: ')

		tmp = input('\ninput learning rate > 0: ')##python3
		# tmp = raw_input('\ninput learning rate > 0: ')
		try:
			float(tmp)
		except Exception as e:
			learning_rate = 0.1
			print ('learning_rate = 0.1')
			return learning_rate
		if float(tmp) >= 0 and float(tmp) < 10:
			return float(tmp)
		else:
			print ('Error: g > 0 and g < 10')
	return learning_rate


def give_gradient(x,y, th0, th1):
	lens = len(x)
	i = 0
	sums0 = 0
	sums1 = 0
	while i < lens:
		tmp = (th0 + th1*x[i] - y[i])
		sums0 += tmp
		sums1 += (tmp * x[i])
		i += 1
	n_th0 = (sums0/i)
	n_th1 = (sums1/i)
	return n_th0, n_th1

def return_N(n_th0, n_th1, th0,th1, x,y):

	err = predict_MSE(x, y, th0, th1)
	N = 1
	now_err = predict_MSE(x, y, th0 - N*( n_th0), th1 - N*( n_th1))
	if now_err < err:
		return N
	else:
		N_smll = N / 2
		now_err_smll = predict_MSE(x, y, th0 - N_smll*( n_th0), th1 - N_smll*( n_th1))
		if now_err_smll < now_err:
			while now_err_smll >= err:
				N_tmp = N_smll / 2
				tmp = predict_MSE(x, y, th0 - N_tmp*( n_th0), th1 - N_tmp*( n_th1))
				if tmp < now_err_smll:
					now_err_smll = tmp
					N_smll = N_tmp
				else:
					return N_smll
			return N_smll
		else:
			while now_err_smll >= err:
				N_tmp = N_smll * 2
				tmp = predict_MSE(x, y, th0 - N_tmp*( n_th0), th1 - N_tmp*( n_th1))
				if tmp < now_err_smll:
					now_err_smll = tmp
					N_smll = N_tmp
				else:
					return N_smll
			return N_smll
import random as rd

def trainModel_auto_l_r(x, y,th0, th1):

	err = predict_MSE(x, y, th0, th1)
	lerr = err + 1
	while err > 0.0000001:
		n_th0, n_th1 = give_gradient(x,y, th0,th1)
		N = return_N(n_th0, n_th1, th0,th1, x,y)
		th0 = th0 - N*( n_th0)
		th1 = th1 - N*( n_th1)
		lerr = err
		err = predict_MSE(x, y, th0, th1)
		print('err=', err, 'N=',N)
		if err < lerr or err/lerr < 0.000001:
			lerr = err
		else:
			break
	return th0, th1


def give_gradient2(x,y,th0, th1):
	lens = len(x)
	i = 0
	sums0 = 0
	sums1 = 0
	while i < lens:
		tmp = (th0 + th1*x[i] - y[i])
		# print('tmp=',tmp,'tmp*xi=' ,tmp*x[i])
		sums0 += tmp
		sums1 += (tmp * x[i])
		i += 1

	# print('sums0',sums0,'sums1', sums1)
	n_th0 = (sums0/i)
	n_th1 = (sums1/i)
	
	return n_th0, n_th1

import matplotlib.pyplot as plt




def trainModel(x, y, learning_rate,th0, th1):


	# if th0 == 0 and th1 == 0:
	# 	minx = x.index(min(x))
	# 	maxx = x.index(max(x))
	# 	print('->',minx)
	# 	x1 = x[minx]
	# 	x2 = x[maxx]
	# 	y1 = y[minx]
	# 	y2 = y[maxx]
	# 	th0 = ((-x1*(y2-y1))/(x2-x1)) + y1
	# 	th1 = (y2-y1)/(x2-x1)

	print('th0 = ',th0, 'th1=',th1)
	err = predict_MSE(x, y, th0, th1)
	print('err=', err)
	print('\n\n')
	plt.scatter(x, y)
	pr = predict(x, th0, th1)
	plt.scatter(x, pr,c='g')
	plt.show()
	lerr = err + 1

	# th0 = 10000
	# N = 0.00000000001
	N = 0.1
	i = 1
	while err > 0.00001:
		# if i > 3:
		# 	N = 1
		n_th0, n_th1 = give_gradient2(x,y, th0,th1)
		print('n_th0 = ',n_th0, 'n_th1=',n_th1)
		

		th0 = th0 - N*( n_th0)
		th1 = th1 - N*( n_th1)
		print('th0 = ',th0, 'th1=',th1)
		lerr = err
		# if err < 0.0901:
		# 	# print('BSFKJASGHKFGBJAS')
		# 	N =0.01
		err = predict_MSE(x, y, th0, th1)
		# if  err > 1e+30:
		# 	ERR('to mush N')
		print('err=', err,'N=',N,i )
		if i > 10000:
			break
		# if err/lerr < 0.000001:
		# 	print ('err/last_err < 0.000001')
		# if err < lerr:
		# 	lerr = err
		# else:
		# 	break
		i += 1
		# a = input(':')
		print('\n')
		plt.scatter(x, y)
		pr = predict(x, th0, th1)
		plt.scatter(x, pr,c='g')
		plt.show()
	return th0, th1

# def trainModel(x, y, learning_rate,th0, th1):

# 	try:
# 		err = predict_MSE(x, y, th0, th1)
# 		lerr = err + 1
# 		N = learning_rate
# 		while err > 0.00001:
# 			n_th0, n_th1 = give_gradient(x,y, th0,th1)
# 			th0 = th0 - N*( n_th0)
# 			th1 = th1 - N*( n_th1)
# 			lerr = err
# 			err = predict_MSE(x, y, th0, th1)
# 			print('err=', err)
# 			if err/lerr < 0.000001:
# 				print ('err/last_err < 0.000001')
# 			if err < lerr:
# 				lerr = err
# 			else:
# 				break
# 	except:
# 		print('\nException')
# 	return th0, th1






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
	if rz == 0:
		ERR('Error: max - min = 0')
	rz /= 20
	i = 10

	start = minn_km
	while start < maxx_km-rz-1:
		# print('start',start)
		canv.create_text(30,1000-i,text = int(start))
		canv.create_line(0,1000-i,6,i,width=2, fill = 'black')
		start += rz
		i += 50
	# exit()
	rz = maxx_price - minn_price
	if rz == 0:
		ERR('Error: max - min = 0')
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
		y = 1000-((float(l_km[i] - minn_km) / (maxx_km - minn_km))*1000)
		x = (float(l_price[i] - minn_price) / (maxx_price - minn_price))*1000
		canv.create_oval(x, y, x + 10, y + 10, fill = 'black')
		i += 1
	
	pr = predict(l_km, th0, th1)
	maxx_price = max(pr)
	minn_price = min(pr)
	if maxx_price - minn_price == 0:
		ERR('Error: predicted max - min = 0')
	lens = len(l_price)
	i = 0
	lsty = []
	lstx = []
	while i < lens:
		y = 1000-((float(l_km[i] - minn_km) / (maxx_km - minn_km))*1000)
		x = (float(pr[i] - minn_price) / (maxx_price - minn_price))*1000
		print('x =', x, 'pr = ',pr[i], 'must=',l_price[i])
		lsty.append(y)
		lstx.append(x)
		canv.create_oval(x, y, x + 10, y + 10, fill = 'orange')
		i += 1
	# minx = lstx.index(min(lstx))
	# maxx = lstx.index(max(lstx))

	# canv.create_line(lstx[minx],lsty[minx],lstx[maxx],lsty[maxx],width=5, fill = 'orange')
	canv.pack()
	root.mainloop() 

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
			float(line[0])
			float(line[1])
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