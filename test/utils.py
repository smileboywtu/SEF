# -*- coding: utf-8 -*-

"""

utils for test the sef module


"""

import os
import time
import hashlib


DIR = 'data'


def save_data(x, y, file):
	"""save the x, y data into the file

	"""
	with open(os.path.join(DIR, file), 'wt') as fp:
		fmt = '{0}	{1}\n'
		for a, b in zip(x, y):
			fp.write(fmt.format(a, b))	


def humanize_bytes(bytes, precision=1):
    """Return a humanized string representation of a number of bytes.

    Assumes `from __future__ import division`.

    >>> humanize_bytes(1)
    '1 byte'
    >>> humanize_bytes(1024)
    '1.0 kB'
    >>> humanize_bytes(1024*123)
    '123.0 kB'
    >>> humanize_bytes(1024*12342)
    '12.1 MB'
    >>> humanize_bytes(1024*12342,2)
    '12.05 MB'
    >>> humanize_bytes(1024*1234,2)
    '1.21 MB'
    >>> humanize_bytes(1024*1234*1111,2)
    '1.31 GB'
    >>> humanize_bytes(1024*1234*1111,1)
    '1.3 GB'
    """
    abbrevs = (
        (1<<50L, 'PB'),
        (1<<40L, 'TB'),
        (1<<30L, 'GB'),
        (1<<20L, 'MB'),
        (1<<10L, 'kB'),
        (1, 'bytes')
    )
    if bytes == 1:
        return '1 byte'
    for factor, suffix in abbrevs:
        if bytes >= factor:
            break
    return '%.*f %s' % (precision, bytes / factor, suffix)

    
def measure(func, type='cpu'):
	"""measure the time of the func

	@params:
		func -- func to measure
		type -- cpu or wall-clock

	"""
	def wrapper(*args, **kwargs):
		# get the start time
		start = time.clock() if type == 'cpu' else time.time()
		# run the function
		ret = func(*args, **kwargs)
		# get stop time
		stop = time.clock() if type == 'cpu' else time.time()
		# show the time
		print (
				"{_ident}\n" + 
				"measure func: {func}\n" +
				"measure type: {type}\n" +
				"time delta: {delta: f}\n" +
				"{ident_}"
		).format(_ident='-'*80, func=func.__name__, type=type, delta=stop-start, ident_='-'*80)
		return ret
	return wrapper


def get_fsize(path):
	"""get the file size

	@params:
		path -- local file path

	"""
	if not os.path.isfile(path):
		raise ValueError('path is not a valid file')

	finfo = os.stat(path)

	return finfo.st_size


def get_fmd5(path):
	"""get file md5

	@params:
		path --  local file path
	"""
	if not os.path.isfile(path):
		raise ValueError('path is not a valid file')

	bsize = 65536
	hasher = hashlib.md5()

	with open(path, 'rb') as fobj:
		hasher.update(fobj.read(bsize))

	return hasher.digest()
