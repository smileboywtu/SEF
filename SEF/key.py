# -*- coding: utf-8 -*-

"""

how to generate the key

"""

import os
import hashlib
import itertools


def generate_key(type, message):
    """generate the key type with message

    """
    q, r = divmod(type, 8)
    if q == 0 or q > 32 or r != 0:
        raise ValueError('key type not supported')
    seed = hashlib.sha512(message).hexdigest()
    return seed[:q*2]


def random_key(type):
    """generate random key for usage

    must be supported type
    """
    q, r = divmod(type, 8)
    if q == 0 or q > 32 or r != 0:
        raise ValueError('key type not supported')
    return os.urandom(512).encode('hex')[:q*2]


def key_check(key):
    """check if the key is a type of support type

    return true  if in support type false if not

    """
    ksize = len(key) * 4
    if isinstance(key, str):
        # not hex string
        try:
            int(key, 16)
        except ValueError:
            raise Exception('key not a valid hex str')
        # key not accept
        q, r = divmod(ksize, 8)
        if q == 0 or q > 32 or r != 0:
            return False
        return True
    return False


def mask_check(mask):
    """check if the mask is support

    return true if support
    """
    if isinstance(mask, int):
        return mask < 7
    return False


def key_generate(key, mask, reverse=False):
    """use the mask and key generate the key sequence

    return current key
    """

    if not isinstance(key, str):
        raise Exception("key only support hex str")

    if not isinstance(mask, int):
        raise Exception("mask only support int")

    if not key_check(key):
        raise Exception('key type error, not support')

    if not mask_check(mask):
        raise Exception('mask type error, not support')

    key_type = len(key) * 4

    str_ = bin(int(key, 16)).split('b')[1]
    key_str = ('0' * (key_type - len(str_)) + str_)

    key_iter = itertools.cycle(int(x) for x in key_str)
    b = next(key_iter)
    c = next(key_iter)
    keys = []
    for count in range(key_type):
        a, b = b, c
        c = next(key_iter)
        key = (a << 2) + (b << 1) + c
        keys.append(key ^ mask)

    if reverse:
        keys.reverse()

    return keys


if __name__ == '__main__':

    key = '333333'
    mask = 2
    keys = []
    for item in key_generate(key, mask):
        keys.append(item)
    print "sequence key: %s" % keys
    keys_ = []
    for item in key_generate(key, mask, reverse=True):
        keys_.append(item)
    print "reverse key: %s" % keys_
