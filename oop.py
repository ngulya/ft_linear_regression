#!/usr/bin/env python

from time import time
import sys
import numpy as np
import Tkinter as T
import matplotlib.pyplot as plt

class ft_linear_regression:

	_th0 = 0
	_th1 = 0
	_max_x = 0
	_min_x = 0
	_max_y = 0
	_min_y = 0
	_learning_rate = 0

	def __init__(self):
		pass
	def return_max_min(self, x, y):
		self._max_x = max(x)
		self._min_x = min(x)
		self._max_y = max(y)
		self._min_y = min(y)

	def ERR(self, st):
		print st
		sys.exit(1)

	def load_x_y(self, x, y):
		self.x = x
		self.y = y

	def MSE(self, have, must):
		print type(have)
		if isinstance(have, list) == False:
			return (have-must)**2
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
			x[i] = float(x[i] - self._min_x)/(self._max_x - self._min_x)
			i += 1
		return x

	def normalize_y(self, l_y):

		y = []
		for i in l_y:
			y.append(i)

		i = 0
		while i < len(y):
			y[i] = float(y[i] - self._min_y)/(self._max_y - self._min_y)
			i += 1
		return y

	def unnormalize_x(self, x):
		max_min = self._max_x - self._min_x
		
		if isinstance(x, list) == False:
			return self._min_x + (x * (max_min))
		
		x_new = []
		for i in x:
			x_new.append(self._min_x + (i * (max_min)))
		return x_new

	def unnormalize_y(self, y):
		max_min = self._max_y - self._min_y
		
		if isinstance(y, list) == False:
			return self._min_y + (y * (max_min))

		y_new = []
		for i in y:
			y_new.append(self._min_y + (i * (max_min)))
		return y_new

	def estimatePrice(self, mileage):
		return self._th0 + (self._th1 * mileage)


	def predict(self, x):
		if self._max_x == 0 and self._min_x == 0:
			print 'Error: model no train'
			return 0, 0
		if isinstance(x, list) == False:
			x_new = float(x - self._min_x)/(self._max_x - self._min_x)
			y_new = self._th0 + (self._th1 * x_new)
			return self.unnormalize_y(y_new), 1
		i = 0
		lst = []
		while i < len(x):
			tmp = float(x[i] - self._min_x)/(self._max_x - self._min_x)
			lst.append(self._th0 + (self._th1 * tmp))
			i += 1
		return self.unnormalize_y(lst), len(lst)

	def predict_MSE(self, x, y):
		ans = 0
		i = 0
		if isinstance(x, list) == False:
			p =  self._th0 + (self._th1 * x[i])
			ans += (p-y[i])**2
			return ans, 1
		lens = len(x)
		while i < lens:
			p =  (self._th0 + (self._th1 * x[i])) - y[i]
			ans += (p*p)
			i += 1
		return ans / i, len(x)

	def from_input_to_int(self):
		self._learning_rate = 0.1
		bad = True
		while bad:
			tmp = raw_input('\ninput learning rate > 0 or learning rate == -1: ')
			try:
				float(tmp)
			except Exception as e:
				self._learning_rate = 0.1
				print 'learning rate = 0.1'
				return
			if float(tmp) == -1:
				self._learning_rate = -1
				return
			if float(tmp) >= 0 and float(tmp) < 10:
				self._learning_rate = float(tmp)
				return
			else:
				print 'Error: learning rate > 0 and  learning srate < 10'

	def give_gradient(self, x,y):
		lens = len(x)
		if lens == 1:
			# tmp = (self._th0 + self._th1*x[i] - y[i])
			tmp = (self.estimatePrice(x) - y)
			sums0 += tmp
			sums1 += (tmp * x[i])
			return sums0, sums1, 1
		i = 0
		sums0 = 0
		sums1 = 0
		while i < lens:
			tmp = (self.estimatePrice(x[i]) - y[i])
			# tmp = (self._th0 + self._th1*x[i] - y[i])
			sums0 += tmp
			sums1 += (tmp * x[i])
			i += 1
		n__th0 = (sums0/i)
		n__th1 = (sums1/i)
		return n__th0, n__th1, len(x)



	def trainModel(self, l_x, l_y):
		self.from_input_to_int()
		if self._max_x == 0 and self._max_y == 0 and self._min_y == 0 and self._min_x == 0:
			self.return_max_min(l_x, l_y)
		x = self.normalize_x(l_x)
		y = self.normalize_y(l_y)
		ans = raw_input('step by step press Y-Yes: ')
		step = False
		if ans == 'y' or ans == 'Y': step = True
		if step:
			print 'For stop study input Y-Yes'
		err, _ = self.predict_MSE(x, y)

		i = 1
		print 'err =',err
		lerr = err + 1
		while err > 0.00001:
			n__th0, n__th1,_ = self.give_gradient(x,y)
			self._th0 = self._th0 - (self._learning_rate*n__th0)
			self._th1 = self._th1 - (self._learning_rate*n__th1)
			err, _ = self.predict_MSE(x, y)
			if lerr < err:
				break
			else:
				lerr = err
			if  err > 10e+30:
				self.ERR('Too mush learning rate')
			if step:
				print 'err =', err
				a = raw_input('')
				if a == 'y' or a == 'Y':
					break
		print 'err =', err
		
	def load_model(self, name_csv):
		_th0 = 0
		_th1 = 0
		_max_x = 0
		_min_x = 0
		_max_y = 0
		_min_y = 0
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
					_th0 = float(line)	
				elif zr == 1:
					_th1 = float(line)
				elif zr == 2:
					_max_x = float(line)
				elif zr == 3:
					_min_x = float(line)
				elif zr == 4:
					_max_y = float(line)
				elif zr == 5:
					_min_y = float(line)
				else:
					print '\nError: read ' + name_csv + '\n'
					return False
				zr += 1
		self._th0 = _th0
		self._th1 = _th1
		self._max_x = _max_x
		self._min_x = _min_x
		self._max_y = _max_y
		self._min_y = _min_y
		self._min_y
		return True

	def save_model(self, name_csv):
		try:
			in_file = open(name_csv, "w")
		except:
			print 'Error: cant read file: '+ name_csv
			return

		in_file.write(str(self._th0) + '\n')
		in_file.write(str(self._th1) + '\n')
		in_file.write(str(self._max_x) + '\n')
		in_file.write(str(self._min_x) + '\n')
		in_file.write(str(self._max_y) + '\n')
		in_file.write(str(self._min_y))
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
	def graph(self, l_x, l_y, pr_y, line):
		if line == 'standart':
			plt.scatter(l_x, l_y, s = 40)
			plt.scatter(l_x, pr_y,c='g',  s = 40)
			plt.show()
			return
			
		root = T.Tk()
		canv = T.Canvas(root, width = 1000, height = 1000, bg = "white")
		canv.create_line(8,998,8,2,width=2,arrow='last') 
		canv.create_line(8,998,998,998,width=2,arrow='last')

		max_x = max(l_x)
		min_x = min(l_x)

		max_y = max(l_y)
		min_y = min(l_y)
		
		if max(pr_y) > max_y: max_y = max(pr_y)
		if min(pr_y) < min_y: min_y = min(pr_y)

		i = 1
		rz = (max_y - min_y) / 10
		start = min_y + rz
		while i < 10:#Y
			if rz < 1:
				txt = '%.5f'%((start))
			else:
				txt = '%d'%((start))

			canv.create_text(30,1000-(i * 100),text = int(txt))
			canv.create_line(6,1000-(i * 100),10,1000-(i * 100),width=2, fill = 'black')
			start += rz
			i += 1
		i = 1
		rz = (max_x - min_x) / 10
		start = min_x + rz
		while i < 10:#X
			if rz < 1:
				txt = '%.5f'%((start))
			else:
				txt = '%d'%((start))
			canv.create_text(i * 100,980,text = int(txt))
			canv.create_line(i * 100,994,i * 100,1000,width=2, fill = 'black')
			start += rz
			i += 1
		
		lens = len(l_y)
		i = 0

		while i < lens:
			y1 = ((1-(float(l_y[i]-min_y)/(max_y-min_y))) * 1000)+5
			x = ((float(l_x[i]-min_x)/(max_x - min_x)) * 1000)+5
			canv.create_oval(x, y1, x + 7, y1 + 7, fill = 'black')
			if line != 'line':
				y2 = ((1-(float(pr_y[i]-min_y)/(max_y-min_y))) * 1000)+5
				canv.create_line(x+3,y1,x+3,y2,width=1, fill = 'black')
				canv.create_oval(x, y2, x + 7, y2 + 7, fill = 'orange')
			i += 1
		
		x0 = 0
		y0 = self._th0 + self._th1 * x0
		x1 = 1
		y1 = self._th0 + self._th1 * x1
		if line == 'line':
			canv.create_line(0,((1-y0) * 1000),x1*1000,((1-y1) * 1000),width=2, fill = 'orange')
		canv.pack()
		root.mainloop() 
		