#!/usr/bin/env python

from time import time
import sys
import numpy as np
from dop_function import MSE, RMSE, load_theta, save_theta ,return_list
import random as rand
import Tkinter as T

def estimatePrice(mileage):
	global th0, th1
	res = th0 + (th1 * mileage)
	return res

def trainModel(l_km, l_price, learningRate):
	i = len(l_km) - 1
	sums0 = 0
	sums1 = 0
	while i >= 0:
		tmp = estimatePrice(l_km[i]) - l_price[i]
		sums0 += tmp
		sums1 += (tmp * l_km[i])
		i -= 1
	i = len(l_km) - 1
	th0 = learningRate * (sums0/i)
	th1 = learningRate * (sums1/i)

	return th0, th1

def predict(l_km):
	lst = []
	for i in l_km:
		lst.append(estimatePrice(i))
	return lst
# https://habr.com/post/163395/
def graph():
	root = T.Tk()
	canv = T.Canvas(root, width = 1000, height = 1000, bg = "lightblue")#, cursor = "pencil")
	# canv.create_line(500,1000,500,0,width=2,arrow='last') 
	canv.create_line(0,500,1000,500,width=2,arrow='last')
	# x0=0,y0=500,x1=1000,y1=500
	# x = 10
	# y = 10
	# i = len(l_km) - 1
	# maxx = max(l_km)
	# minn = min(l_km)
	# canv.create_oval(x, y, x + 20, y + 20, fill = 'black')

	canv.pack()
	root.mainloop() 

if __name__ == "__main__":
	l_km, l_price = return_list()
	
	graph()
	exit()
	print MSE(l_km, l_price)
	print RMSE(l_km, l_price)
	# save_theta(0.1124142111, -0.3)
	th0, th1, status = load_theta()
	if status == False:
		th0 = rand.uniform(-0.49, 0.49)
		th1 = rand.uniform(-0.49, 0.49)
	print 'MSE = ', MSE(predict(l_km), l_price)
	th0, th1 = trainModel(l_km,l_price, 0.9)
	print 'MSE = ', MSE(predict(l_km), l_price)
	# ans = raw_input('Save theta Y-Yes')
	# if ans == 'Y' or ans == 'y':
	# 	save_theta(th0, th1)
	

