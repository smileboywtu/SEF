# -*- coding: utf-8 -*-

"""

	test suit for SEF

"""

import os
import time
import hashlib
import subprocess
from SEF import Key 
from color import Colors
from curve import Curve
from pprint import pprint
from utils import (
	length_generator, generate_message,
	humanize_bytes, save_data
)
from cellers import (
	SEF_celler, DES_celler, DES3_celler, AES_celler
)

# patch for Colors
def plain(msg, *args):
	return msg
#Colors.colorize = staticmethod(plain)

func, fmt = Curve.linear
curve = Curve(func, fmt)


def gnuplot(title, x, y, xt, yt, xl, yl, fmt='dumb', output=None):
	"""draw console plot 

	use the gnuplot

	"""
	scale = 1.3

	gnuplot = subprocess.Popen(['/usr/bin/gnuplot'], stdin=subprocess.PIPE)
	shell = gnuplot.stdin.write
	# set plot
	shell("set terminal {0}\n".format(fmt))
	if output:
		shell("set grid\n")
		shell("set output '{0}'\n".format(output))

	shell("set key top left\n")
	shell("set title '{0}'\n".format(title))
	# draw
	shell("set xlabel '{0}'\n".format(xl))	
	shell("set ylabel '{0}'\n".format(yl))
	shell("set xrange[0:{0}]\n".format(xt * scale))
	shell("set yrange[0:{0}]\n".format(yt * scale))
	shell("plot '-' with linespoints pointtype 5\n")
	for x_, y_ in zip(x, y):
		shell('{0} {1}\n'.format(x_, y_))
	# exit
	shell("exit\n")
	shell('quit\n')
	out, err = gnuplot.communicate()
	if err:
		print out


def test_keys():
	"""test same message for different length key

	"""
	message = (
		"Python was conceived in the late 1980s,[30] and its implementation "
		"began in December 1989[31] by Guido van Rossum at Centrum Wiskunde & "
		"Informatica (CWI) in the Netherlands as a successor to the ABC language "
		"(itself inspired by SETL)[32] capable of exception handling and interfacing "
		"with the operating system Amoeba.[7] Van Rossum is Python's principal author, "
		"and his continuing central role in deciding the direction of Python is reflected "
		"in the title given to him by the Python community, benevolent dictator for life (BDFL)."
		"About the origin of Python, Van Rossum wrote in 1996:[33]"
	)

	print Colors.colorize('message source: ', 'cyan', 'black', 'bold')
	pprint(message)
	print '-' * 80

	mask = 0x03
	print Colors.colorize('key mask: ', 'cyan', 'black', 'bold'), mask
	print '-' * 80

	key_types = [i * 8 for i in range(1, 33)]
	keys = [(type, Key.random_key(type)) for type in key_types]

	print Colors.colorize('keys: ', 'cyan', 'black', 'bold')
	pprint(keys)
	print '-' * 80

	print Colors.colorize('Tester Result: ', 'cyan', 'black', 'bold')
	print ('{:>15}' * 3).format('key', 'status', 'runtime(s)') 
	print ''
	deltas = []
	for type, key in keys:
		start = time.clock()
		ret = SEF_celler(message, key, mask)
		stop = time.clock()
		delta = stop - start
		deltas.append(delta)
		status = 'success' if ret else 'fail'
		print ('{:>15}' * 3).format(type, status, delta)

	print '-' * 80
	print Colors.colorize('Time Consuming Growing: ', 'cyan', 'black', 'bold')
	gnuplot(
		'key bits growing', 
		key_types, deltas, 
		key_types[-1], deltas[-1], 
		'key/bits', 'time/s'
	)
	print '-' * 80	
	curve.fit(key_types, deltas)
	print Colors.colorize('Scipy Curve Fit: ', 'cyan', 'black', 'bold'), curve
	print '-' * 80
	_, ys = curve.sample()
	save_data(key_types, deltas, ys, 'KEY.dat')


def test_message():
	"""test for the message length

	"""
	key = Key.random_key(64)
	print Colors.colorize('encrypt key: ', 'cyan', 'black', 'bold'), key
	print '-' * 80

	mask = 5
	print Colors.colorize('mask: ', 'cyan', 'black', 'bold'), mask
	print '-' * 80

	turns = 13
	print Colors.colorize('test turns: ', 'cyan', 'black', 'bold'), turns
	print '-' * 80

	print Colors.colorize('Tester Result: ', 'cyan', 'black', 'bold')
	print ('{:>15}' * 3).format('message len', 'status', 'runtime(s)') 
	print ''
	lens = []
	deltas = []
	for length in length_generator(turns):
		# get the message
		lens.append(length)
		message = generate_message(length)
		# measure time
		start = time.clock()
		ret = SEF_celler(message, key, mask)
		stop = time.clock()
		delta = stop - start
		deltas.append(delta)
		status = 'success' if ret else 'fail'
		print ('{:>15}' * 3).format(humanize_bytes(length), status, delta)

	print '-' * 80
	print Colors.colorize('Time Consuming Growing: ', 'cyan', 'black', 'bold')
	gnuplot(
		'message growing', 
		lens, deltas, 
		lens[-1], deltas[-1], 
		'message/bytes', 'time/s', 
	)
	print '-' * 80
	curve.fit(lens, deltas)
	print Colors.colorize('Scipy Curve Fit: ', 'cyan', 'black', 'bold'), curve
	print '-' * 80
	_, ys = curve.sample()
	save_data(lens, deltas, ys, 'SEF.dat')


def test_general():
	"""run message length test for AES, DES, DES3"""
	files = 'DES.dat', 'DES3.dat', 'AES.dat'
	cellers = DES_celler, DES3_celler, AES_celler

	print (
		"Key Size: 128\n"
		"Cellers: {0}"
	).format(('DES', 'DES3', 'AES'))

	key = Key.random_key(128)[:16]
	print Colors.colorize('key: ', 'cyan', 'black', 'bold'), key

	turns = 13
	print Colors.colorize('test turns: ', 'cyan', 'black', 'bold'), turns
	print '-' * 80

	for index, celler in enumerate(cellers):
		lens = []
		deltas = []
		key_ = key[:8] if index == 0 else key
		cell = files[index].split('.')[0]
		print Colors.colorize('run test for ' + cell, 'cyan', 'black', 'bold')
		print '-' * 80

		print Colors.colorize('Tester Result: ', 'cyan', 'black', 'bold')
		print ('{:>15}' * 3).format('message len', 'status', 'runtime(s)') 
		print ''
		for length in length_generator(turns):
			lens.append(length)
			message = generate_message(length)
			start = time.clock()
			ret = celler(message, key_)
			stop = time.clock()
			delta = stop - start
			deltas.append(delta)
			status = 'success' if ret else 'fail'
			print ('{:>15}' * 3).format(humanize_bytes(length), status, delta)

		print '-' * 80
		print Colors.colorize('Time Consuming Growing: ', 'cyan', 'black', 'bold')
		gnuplot(
			'message growing', 
			lens, deltas, 
			lens[-1], deltas[-1], 
			'message/bytes', 'time/s', 
		)
		print '-' * 80
		curve.fit(lens, deltas)
		print Colors.colorize('Scipy Curve Fit: ', 'cyan', 'black', 'bold'), curve
		print '-' * 80
		_, ys = curve.sample()
		save_data(lens, deltas, ys, files[index])


def test_suit():
	"""run test suit for SEF

	@func

		1. key bits test
		2. file large test
	"""

	print Colors.colorize('run key bits tester', 'blue', 'white', 'bold')
	print '-' * 80
	test_keys()

	print Colors.colorize('run message length tester', 'blue', 'white', 'bold')
	print '-' * 80
	test_message()

	print Colors.colorize('run general cipher tester', 'blue', 'white', 'bold')
	print '-' * 80
	test_general()

	print Colors.colorize('run key test for DES3', 'blue', 'white', 'bold')
	print '-' * 80


def test_binary(dir='binary', odir='encrypt'):
	"""test for image file"""
	if not os.path.isdir(dir):
		raise ValueError('not valid dir')

	print Colors.colorize('Tester for image file, directory: ', 'blue', 'white', 'bold'), dir
	print '-' * 80
	key = Key.random_key(64)
	print Colors.colorize('Keys: ', 'cyan', 'black', 'bold'), key
	mask = 3
	print Colors.colorize('Mask: ', 'cyan', 'black', 'bold'), mask 

	for file in os.listdir(dir):
		print Colors.colorize('current test image: ', 'cyan', 'black', 'bold'), file
		print '-' * 80
		data = open(os.path.join(dir, file), 'rb').read()
		fname = os.path.splitext(file)[0] +'.dat'
		out = os.path.join(odir, fname)
		start = time.clock()
		ret = SEF_celler(data, key, mask, out=out)
		stop = time.clock()
		delta = stop - start
		print Colors.colorize('time: ', 'cyan', 'black', 'bold'), delta
		print '-' * 80
		status = 'success' if ret else 'fail'
		print Colors.colorize('status: ', 'cyan', 'black', 'bold'), status 
		print '-' * 80
