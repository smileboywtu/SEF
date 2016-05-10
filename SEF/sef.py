# -*- coding: utf-8 -*-

"""

	class method for sef cipher


"""


from .encrypt import encrypt
from .decrypt import decrypt

from .key import key_check
from .key import random_key
from .key import key_generate
from .key import generate_key

from .utils import PKCS7_pad
from .utils import PKCS7_depad


class Sef:
	"""symmetric data encryption"""

	# static members
	block_size = 8L
	key_size = [i * 8 for i in range(1, 33)]

	def __init__(self, key, mask):
		"""init the ciphter"""

		if not key_check(key):
			raise ValueError('key not supported')

		if not isinstance(mask, int):
			raise TypeError('mask must be integer')

		if not (-1 < mask < 8):
			raise ValueError('mask must be less than 8')

		self.keys = key_generate(key, mask, reverse=False)

	def get_keys(self, reverse=False):
		"""return the keys"""
		return self._keys[::-1] if reverse else self._keys[:]

	def encrypt(self, message):
		"""encrypt the message with the key and mask

		make sure the key and mask is input
		"""
		return encrypt(message, self.keys[:]).getvalue()

	def decrypt(self, message):
		"""decrypt the cipher with the key and mask

		"""
		return decrypt(message, self.keys[::-1]).getvalue()


class Key:
	"""sef key tool"""

	random_key = staticmethod(random_key)
	generate_key = staticmethod(generate_key)


class PKCS7:
	"""PKCS7 tool for sef"""

	pad = staticmethod(PKCS7_pad)
	depad = staticmethod(PKCS7_depad)
