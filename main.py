#!/usr/bin/env python3

from time import time
import sys
import numpy as np
from dop_function import MSE, RMSE, load_theta, save_theta,estimatePrice, trainModel,return_list_from_data,graph,predict
import tkinter as T
# import Tkinter as T 2
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression


if __name__ == "__main__":
	# l_km, l_price = return_list_km_price()
	l_km, l_price = return_list_from_data('data.csv')
	# plt.plot(l_km, l_price, 'ro')
	# plt.show()
	# # exit()

	th0, th1, status = load_theta()
	if status == False:
		th0 = 0
		th1 = 0
	
	# graph(l_km, l_price, th0, th1)
	print ('MSE = ', MSE(predict(l_km, th0, th1), l_price))
	th0, th1 = trainModel(l_km,l_price, 0.000000003,th0, th1)
	print ('MSE = ', MSE(predict(l_km, th0, th1), l_price))
	
	graph(l_km, l_price, th0, th1)
	# ans = raw_input('Save theta Y-Yes')
	# if ans == 'Y' or ans == 'y':
	# save_theta(th0, th1)
	

