# -*- coding: utf-8 -*-

"""

	wrapper for c func

"""

from libc.stdlib cimport malloc, free
from libc.string cimport memset, memcpy

# encryption block size
cdef char dsize = 8

cpdef _encrypt(unsigned char* data, keys):
	"""sef encrypt func"""

	# define array and reset it to zero
	cdef unsigned char* cipher = <unsigned char*>malloc(dsize)
	for key in keys:
		memset(cipher, 0, dsize)
		for index in range(dsize):
			if index == 0:
				cipher[index] = data[key]
			else:
				cipher[index] = data[key % dsize] ^ cipher[index - 1]	
			key += 1
		memcpy(data, cipher, dsize)
	# free the memory
	free(cipher)
	return ''.join([chr(data[index]) for index in range(dsize)]) 


cpdef _decrypt(unsigned char* cipher, keys):
	"""sef decrypt func"""

	# define temp array
	cdef unsigned char* temp = <unsigned char*>malloc(dsize)
	for key in keys:
		memset(temp, 0, dsize)
		for index in range(dsize):
			if index == 0:
				temp[key % dsize] = cipher[index]
			else:
				temp[(key + index) % dsize] = cipher[index] ^ cipher[index - 1]
		memcpy(cipher, temp, dsize) 
    # free the memory
	free(temp)
	return ''.join([chr(cipher[index]) for index in range(dsize)])
