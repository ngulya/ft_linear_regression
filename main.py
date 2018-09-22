#!/usr/bin/env python3

from time import time
import sys
import numpy as np
from dop_function import MSE, RMSE,trainModel_auto_l_r,from_input_to_int, load_theta, save_theta,estimatePrice, trainModel,return_list_from_data,graph,predict
import tkinter as T
# import Tkinter as T 2
import matplotlib.pyplot as plt



if __name__ == "__main__":
	
	l_km, l_price = return_list_from_data('data4.csv')

	# maxx_km = max(l_km)
	# minn_km = min(l_km)
	# maxx_price = max(l_price)
	# minn_price = min(l_price)
	# i = 0
	# while i < len(l_km):
	# 	l_km[i] = (l_km[i] - minn_km)/(maxx_km - minn_km)
	# 	i += 1
	# i = 0
	# while i < len(l_price):
	# 	l_price[i] = (l_price[i] - minn_price)/(maxx_price - minn_price)
	# 	i += 1
	th0, th1, status = load_theta()
	if status == False:
		th0 = 0
		th1 = 0
	# plt.scatter(l_km, l_price)
	# pr = predict(l_km, th0, th1)
	# plt.scatter(l_km, pr,c='g')
	# plt.show()
	# # exit()
	# graph(l_km, l_price, th0, th1)
	print ('MSE1 = ', MSE(predict(l_km, th0, th1), l_price))
	# l_r = from_input_to_int()
	l_r = 0.1
	
	th0, th1 = trainModel(l_km,l_price, l_r,th0, th1)
	# th0, th1 = trainModel_auto_l_r(l_km,l_price,th0, th1)
	print ('MSE2 = %.13f'%MSE(predict(l_km, th0, th1), l_price))
	
	plt.scatter(l_km, l_price)
	pr = predict(l_km, th0, th1)
	plt.scatter(l_km, pr,c='g')
	plt.show()
	# graph(l_km, l_price, th0, th1)

	# ans = raw_input('Save theta Y-Yes: ')
	# ans = input('Save theta Y-Yes: ')##python3
	# if ans == 'Y' or ans == 'y':
	# save_theta(th0, th1)