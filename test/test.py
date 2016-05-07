# -*- coding: utf-8 -*-

"""

	test suit for SEF

"""

import time
import random
import string
import hashlib
import subprocess
from SEF import encrypt
from SEF import decrypt
from pprint import pprint
from color import Colors
from utils import humanize_bytes


def gnuplot(x, y, xt, yt, xl, yl):
	"""draw console plot 

	use the gnuplot

	"""
	scale = 1.3

	gnuplot = subprocess.Popen(['/usr/bin/gnuplot'], stdin=subprocess.PIPE)
	shell = gnuplot.stdin.write
	# set plot
	shell("set terminal dumb\n")
	shell("set title 'time growing'\n")
	# draw
	shell("set xlabel '{0}'\n".format(xl))	
	shell("set ylabel '{0}'\n".format(yl))
	shell("set xrange[0:{0}]\n".format(xt * scale))
	shell("set yrange[0:{0}]\n".format(yt * scale))
	shell("plot '-' with linespoints\n")
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

	seed = hashlib.sha512(message).hexdigest()
	key_types = 8, 16, 32, 64, 128, 256

	keys = []
	for type in key_types:
		q, r = divmod(type, 8)
		value = seed[:q*2]
		keys.append((type, value))

	print Colors.colorize('keys: ', 'cyan', 'black', 'bold')
	pprint(keys)
	print '-' * 80

	print Colors.colorize('Tester Result: ', 'cyan', 'black', 'bold')
	print ('{:>15}' * 3).format('key', 'status', 'runtime') 
	print ''
	deltas = []
	for type, key in keys:
		start = time.clock()
		cliper = encrypt(message, key, mask).getvalue()
		message_ = decrypt(cliper, key, mask).getvalue()
		stop = time.clock()
		delta = stop - start
		deltas.append(delta)
		status = 'success' if message == message_ else 'fail'
		print ('{:>15}' * 3).format(type, status, delta)

	print '-' * 80
	print Colors.colorize('Time Consuming Growing: ', 'cyan', 'black', 'bold')
	gnuplot(key_types, deltas, key_types[-1], deltas[-1], 'key/bits', 'time/s')
	print '-' * 80


def length_generator(val):
	"""generate length for message
	
	start from  pow(2, 5) till to pow(2, 5+val)

	"""
	base = 2
	point = 5 
	for _ in xrange(val):
		yield pow(2, point)
		point += 1


def generate_message(length):
	"""generate random message with given length

	"""
	items = string.digits + string.letters
	return ''.join([random.choice(items) for i in xrange(length)])


def test_message():
	"""test for the message length

	"""
	key = '53d42ffefe5c71be'
	print Colors.colorize('encrypt key: ', 'cyan', 'black', 'bold'), key
	print '-' * 80

	mask = 5
	print Colors.colorize('mask: ', 'cyan', 'black', 'bold'), mask
	print '-' * 80

	turns = 13
	print Colors.colorize('test turns: ', 'cyan', 'black', 'bold'), turns
	print '-' * 80

	print Colors.colorize('Tester Result: ', 'cyan', 'black', 'bold')
	print ('{:>15}' * 3).format('message len', 'status', 'runtime') 
	print ''
	lens = []
	deltas = []
	for length in length_generator(turns):
		# get the message
		lens.append(length)
		message = generate_message(length)
		# measure time
		start = time.clock()
		cliper = encrypt(message, key, mask).getvalue()
		message_ = decrypt(cliper, key, mask).getvalue()
		stop = time.clock()
		delta = stop - start
		deltas.append(delta)
		status = 'success' if message == message_ else 'fail'
		print ('{:>15}' * 3).format(humanize_bytes(length), status, delta)

	print '-' * 80
	print Colors.colorize('Time Consuming Growing: ', 'cyan', 'black', 'bold')
	gnuplot(lens, deltas, lens[-1], deltas[-1], 'message/bytes', 'time/s')
	print '-' * 80


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
