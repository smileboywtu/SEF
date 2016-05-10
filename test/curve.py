# -*- coding: utf-8 -*-

"""

	use scipy to fit the curve

"""

import numpy as np
from scipy.optimize import curve_fit

class Curve:
	"""fit the curve"""

	linear = lambda  x, a, b: a * x + b, 'f(x) = {0} * x + {1}'

	def __init__(self, func, fmt):
		"""init the curve"""
		self.func = func
		self.fmt = fmt
		self.funcs = {'linear': Curve.linear}

	def fit(self, xdata, ydata):
		"""fit the curve"""
		popt, pcov = curve_fit(self.func, xdata, ydata)
		perr = np.sqrt(np.diag(pcov))	
		# get the sample
		ys = [self.func(x, *popt) for x in xdata]
		self.sample_ = xdata, ys 
		self.args = popt
		self.err = perr

	def add_func(self, name, func, fmt):
		"""add new fit func to Curve"""
		self.funcs.update({
			name: (func, fmt)
		})

	def sample(self):
		"""give the sample data for curve"""
		return self.sample_

	def __str__(self):
		"""return func string"""
		return self.fmt.format(*tuple(self.args)) + '\nstandard deviation errors: ' + str(self.err)