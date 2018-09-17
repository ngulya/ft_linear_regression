#!/usr/bin/env python

from time import time
import sys
import numpy as np
from dop_function import MSE, RMSE, load_theta, save_theta ,return_list


if __name__ == "__main__":
	l_km, l_price = return_list()
	print MSE(l_km, l_price)
	print RMSE(l_km, l_price)
	# save_theta(0.1124142111, -0.3)
	th0, th1, status = load_theta()
	if status == False:
	
	print th0, th1