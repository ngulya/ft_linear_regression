#!/usr/bin/env python
from time import time
import sys
import numpy as np
from dop_function import MSE, RMSE,trainModel_auto_l_r,from_input_to_int, load_theta, save_theta,estimatePrice, trainModel,return_list_from_data,graph,predict
import Tkinter as T
import matplotlib.pyplot as plt



if __name__ == "__main__":
	
	l_x, l_y = return_list_from_data('data.csv')

	maxx_x = max(l_x)
	minn_x = min(l_x)
	maxx_y = max(l_y)
	minn_y = min(l_y)
	i = 0

	while i < len(l_x):
		l_x[i] = float(l_x[i] - minn_x)/(maxx_x - minn_x)
		i += 1
	i = 0
	while i < len(l_y):
		l_y[i] = float(l_y[i] - minn_y)/(maxx_y - minn_y)
		i += 1

	th0, th1, status = load_theta()
	if status == False:
		th0 = 0
		th1 = 0

	# plt.scatter(l_x, l_y)
	# pr = predict(l_x, th0, th1)
	# plt.scatter(l_x, pr,c='g')
	# plt.show()
	# graph(l_x, l_y, th0, th1)
	print ('MSE1 = ', MSE(predict(l_x, th0, th1), l_y))
	# l_r = from_input_to_int()
	l_r = 0.1
	
	# th0, th1 = trainModel(l_x,l_y, l_r,th0, th1)
	th0, th1 = trainModel_auto_l_r(l_x,l_y,th0, th1)
	print ('MSE2 = %.13f'%MSE(predict(l_x, th0, th1), l_y))

	graph(l_x, l_y, th0, th1, maxx_x, minn_x, maxx_y, minn_y)

	# ans = raw_input('Save theta Y-Yes: ')
	# ans = input('Save theta Y-Yes: ')##python3
	# if ans == 'Y' or ans == 'y':
	# save_theta(th0, th1)