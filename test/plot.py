# -*- coding: utf-8 -*-


"""

	show all the result in the same plot

"""

import os
from utils import read_data
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def show(dir='data'):
	"""show all the result in the same figure

	get all the data from data dir
	"""
	if not os.path.isdir(dir):
		raise ValueError('dir is not exist')

	dirs = os.listdir(dir)
	align = 3
	q, r = divmod(len(dirs), align)
	q = q + 1 if r != 0 else q
	rows = q * 100
	columns = align * 10 
	start = 1
	# read all the data
	for index, file in enumerate(dirs):
		x, y, ys = read_data(os.path.join(dir, file))
		number = rows + columns + start + index
		# plot the data	
		plt.subplot(number)
		plt.title(file.split('.')[0], color='red')
		plt.xlabel('message/bytes')
		plt.ylabel('time/s')
		plt.plot(x, y, 'bo-', x, ys, 'r^-')

	# show the image
	red_patch = mpatches.Patch(color='blue', label='source data')
	blue_patch = mpatches.Patch(color='red', label='scipy fit func')
	plt.legend(handles=[red_patch, blue_patch], bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
	plt.show()



if __name__ == '__main__':
	show()
