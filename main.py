# -*- coding: utf-8 -*-

"""

test the encryption and decryption

"""

from SEF import encrypt, decrypt


def main():
	"""encrypt a message and test the decrypt process

	"""
	key = "3E"
	mask = 3
	message = 'hello, my name is smileboywtu.'.encode('utf-8')

	print 'source message(utf-8): %s' % message

	cliper = encrypt(message, key, mask)

	print 'encrypted message: %s' % cliper.getvalue()

	message_ = decrypt(cliper.getvalue(), key, mask)

	print 'decrypted message: %s' % message_.getvalue()

	assert message_.getvalue() == message



if __name__ == '__main__':
	main()
