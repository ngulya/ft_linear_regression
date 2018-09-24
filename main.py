#!/usr/bin/env python
from time import time
import sys
import numpy as np
# from dop_function import MSE, RMSE,trainModel_auto_l_r,from_input_to_int, load_theta, save_theta,estimatePrice, trainModel,return_list_from_data,graph,predict
from oop import ft_linear_regression
import Tkinter as T
import matplotlib.pyplot as plt#########uncom



if __name__ == "__main__":

	lin = ft_linear_regression()
	l_x, l_y, status = lin.return_list_from_data('data.csv')
	if status:
		lin.load_model('theta.txt')
		lin.trainModel(l_x, l_y)

		pr_y, status  = lin.predict(l_x)
		lin.graph(l_x, l_y, pr_y, 'line')
		
		# lin.save_model('theta.txt')