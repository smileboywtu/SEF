# -*- coding: utf-8 -*-

"""

	wrapper for c func

"""

from libc.stdlib cimport malloc, free
from libc.string cimport memset, memcpy


dsize = 8L


cpdef str _encrypt(char* data, keys):
	"""sef encrypt func"""

	# define array and reset it to zero
	cdef char* cipher = <char*>malloc(dsize)

	for key in keys:
		memset(cipher, 0, dsize)
		for index in xrange(dsize):
			if index == 0:
				cipher[index] = data[key]
			else:
				cipher[index] = data[key % dsize] ^ cipher[index - 1]	
			key += 1
		memcpy(data, cipher, dsize)

	# free the memory
	free(cipher)
	return ''.join([chr(data[index]) for index in xrange(dsize)]) 



cpdef str _decrypt(char* cipher, keys):
	"""sef decrypt func"""

	# define temp array
	cdef char* temp = <char*>malloc(dsize)

	for key in keys:
		memset(temp, 0, dsize)
		for index in xrange(dsize):
			if index == 0:
				temp[key % dsize] = cipher[index]
			else:
				temp[(key + index) % dsize] = cipher[index] ^ cipher[index - 1]
		memcpy(cipher, temp, dsize) 

    # free the memory
	free(temp)
	return ''.join([chr(cipher[index]) for index in xrange(dsize)])