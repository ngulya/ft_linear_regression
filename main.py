#!/usr/bin/env python
from time import time
import sys
import numpy as np
from dop_function import MSE, RMSE,trainModel_auto_l_r,from_input_to_int, load_theta, save_theta,estimatePrice, trainModel,return_list_from_data,graph,predict
import Tkinter as T
# import matplotlib.pyplot as plt#########uncom

class ft_linear_regression:

	th0 = 0
	th1 = 0
	max_x = 0
	min_x = 0
	max_y = 0
	min_y = 0
	learning_rate = 0
	# x = []
	# y = []
	# x_test = []
	# y_test = []
	def __init__(self):
		# if self.load_model() == False:
		print 'Warning: no theta and normalize param. \nUse return_max_min(x, y).'
		# self.learning_rate = 0.1
		self.from_input_to_int()
	def return_max_min(self, x, y):
		self.max_x = max(x)
		self.min_x = min(x)
		self.max_y = max(y)
		self.min_y = min(y)

	def ERR(self, st):
		print st
		sys.exit(1)

	def load_x_y(self, x, y):
		self.x = x
		self.y = y

	def MSE(self, have, must):

		lens = len(have) - 1
		e = 0
		while lens >= 0:
			rz = have[lens] - must[lens]
			e += (rz * rz)
			lens -= 1
		e = e / len(have)
		return e

	def RMSE(self, have, must):
		return (self.MSE(have, must)**0.5)

	def normalize_x(self, l_x):
		x = []
		
		for i in l_x:
			x.append(i)

		i = 0
		while i < len(x):
			x[i] = float(x[i] - self.min_x)/(self.max_x - self.min_x)
			i += 1
		return x

	def normalize_y(self, l_y):

		y = []
		for i in l_y:
			y.append(i)

		i = 0
		while i < len(y):
			y[i] = float(y[i] - self.min_y)/(self.max_y - self.min_y)
			i += 1
		return y

	def unnormalize_x(self, x):
		max_min = self.max_x - self.min_x
		
		if isinstance(x, list) == False:
			return self.min_x + (x * (max_min))
		
		x_new = []
		for i in x:
			x_new.append(self.min_x + (i * (max_min)))
		return x_new

	def unnormalize_y(self, y):
		max_min = self.max_y - self.min_y
		
		if isinstance(y, list) == False:
			return self.min_y + (y * (max_min))

		y_new = []
		for i in y:
			y_new.append(self.min_y + (i * (max_min)))
		return y_new

	def estimatePrice(self, mileage):
		return self.th0 + (self.th1 * mileage)


	def predict(self, x):
		if self.max_x == 0 and self.min_x == 0:
			print 'Error: model no train'
			return 0, 0
		if isinstance(x, list) == False:
			x_new = float(x - self.min_x)/(self.max_x - self.min_x)
			y_new = self.th0 + (self.th1 * x_new)
			return self.unnormalize_y(y_new), 1
		i = 0
		lst = []
		while i < len(x):
			tmp = float(x[i] - self.min_x)/(self.max_x - self.min_x)
			lst.append(self.th0 + (self.th1 * tmp))
			i += 1
		return self.unnormalize_y(lst), len(lst)

	def predict_MSE(self, x, y):
		ans = 0
		i = 0
		if len(x) == 1:
			p =  self.th0 + (self.th1 * x[i])
			ans += (p-y[i])**2
			return ans, 1
		lens = len(x)
		while i < lens:
			p =  self.th0 + (self.th1 * x[i])
			ans += (p-y[i])**2
			i += 1
		return ans / i, len(x)

	def from_input_to_int(self):
		self.learning_rate = 0.1
		bad = True
		while bad:
			tmp = raw_input('\ninput learning rate > 0 or learning rate == -1: ')
			try:
				float(tmp)
			except Exception as e:
				self.learning_rate = 0.1
				print 'learning rate = 0.1'
				return
			if float(tmp) == -1:
				self.learning_rate = -1
				return
			if float(tmp) >= 0 and float(tmp) < 10:
				self.learning_rate = float(tmp)
				return
			else:
				print 'Error: learning_rate > 0 and learning_rate < 10'

	def give_gradient(self, x,y):
		lens = len(x)
		if lens == 1:
			# tmp = (self.th0 + self.th1*x[i] - y[i])
			tmp = (self.estimatePrice(x) - y)
			sums0 += tmp
			sums1 += (tmp * x[i])
			return sums0, sums1, 1
		i = 0
		sums0 = 0
		sums1 = 0
		while i < lens:
			tmp = (self.estimatePrice(x[i]) - y[i])
			# tmp = (self.th0 + self.th1*x[i] - y[i])
			sums0 += tmp
			sums1 += (tmp * x[i])
			i += 1
		n_th0 = (sums0/i)
		n_th1 = (sums1/i)
		return n_th0, n_th1, len(x)



	def trainModel(self, l_x, l_y):
		if self.max_x == 0 and self.max_y == 0 and self.min_y == 0 and self.min_x == 0:
			self.return_max_min(l_x, l_y)
		x = self.normalize_x(l_x)
		y = self.normalize_y(l_y)
		print 'For stop study input Y-Yes'
		err, _ = self.predict_MSE(x, y)

		i = 1
		print 'err =',err
		while err > 0.00001:
			n_th0, n_th1,_ = self.give_gradient(x,y)
			self.th0 = self.th0 - (self.learning_rate*n_th0)
			self.th1 = self.th1 - (self.learning_rate*n_th1)
			err, _ = self.predict_MSE(x, y)
			if  err > 10e+30:
				self.ERR('Too mush learning rate')
			print 'err =', err
			a = raw_input('')
			if a == 'y' or a == 'Y':
				break
		
	def load_model(self, name_csv):
		th0 = 0
		th1 = 0
		max_x = 0
		min_x = 0
		max_y = 0
		min_y = 0
		try:
			in_file = open(name_csv, "r")
		except:
			print '\nError: load file ' + name_csv + '\n'
			return False
		zr = 0
		for line in in_file.readlines():
			try:
				float(line)
			except Exception as e:
				print '\nUnvalid ' + name_csv + 'file: ' + str(zr + 1) + '\n'
				return False
			else:
				if zr == 0:
					th0 = float(line)	
				elif zr == 1:
					th1 = float(line)
				elif zr == 2:
					max_x = float(line)
				elif zr == 3:
					min_x = float(line)
				elif zr == 4:
					max_y = float(line)
				elif zr == 5:
					min_y = float(line)
				else:
					print '\nError: read ' + name_csv + '\n'
					return False
				zr += 1
		self.th0 = th0
		self.th1 = th1
		self.max_x = max_x
		self.min_x = min_x
		self.max_y = max_y
		self.min_y = min_y
		self.min_y
		return True

	def save_model(self, name_csv):
		try:
			in_file = open(name_csv, "w")
		except:
			print 'Error: cant read file: '+ name_csv
			return

		in_file.write(str(self.th0) + '\n')
		in_file.write(str(self.th1) + '\n')
		in_file.write(str(self.max_x) + '\n')
		in_file.write(str(self.min_x) + '\n')
		in_file.write(str(self.max_y) + '\n')
		in_file.write(str(self.min_y))
		in_file.close()


	def return_list_from_data(self, name_csv):

		l_x, l_y = [],[]
		try:
			in_file = open(name_csv, "r")
		except:
			print 'Error: cant read file: ' + name_csv
			return 0,0, False
		num_str = 0
		frst = 0
		for line in in_file.readlines():
			try:
				line = line.split(',')
				float(line[0])
				float(line[1])
			except Exception as e:
				if frst != 0:
					print 'Error: num str = ' + str(frst + 1)
					return 0,0, False
				num_str += 1
			else:
				l_x.append(float(line[0]))
				l_y.append(float(line[1]))
			frst += 1
		in_file.close()
		if len(l_x) == 0 or len(l_y) == 0 or len(l_y) != len(l_x):
			print 'Error: zero size'
			return 0,0, False
		return l_x, l_y, True


if __name__ == "__main__":

	lin = ft_linear_regression()
	l_x, l_y, status = lin.return_list_from_data('data.csv')
	if status:
		lin.load_model('theta.txt')
		# lin.load_x_y(l_x, l_y)
		# lin.normalize_data()
		lin.trainModel(l_x, l_y)
		x,_ = lin.predict(l_x)
		print l_x
		print x
		graph(l_x, l_y, lin.th0, lin.th1, lin.max_x, lin.min_x, lin.max_y, lin.min_y, 'line')
		lin.save_model('theta.txt')