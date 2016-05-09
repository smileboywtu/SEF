# -*- coding: utf-8 -*-

"""

	python sef implementation

"""


def _encrypt(data, keys):
    """encrypt the data

    @params:
        bindex -- start index of the block
        seq -- current write index
        locker -- global locker between process
        data -- encrypt data block
        out -- output bytes stream
    """
    bsize = len(data)

    B = [ord(data[index]) for index in xrange(bsize)]
    for key_ in keys:
        B1 = [0] * bsize 
        for index in xrange(bsize):
            if index == 0:
                B1[index] = B[key_]
            else:
                B1[index] = B[key_ % bsize] ^ B1[index - 1]
            key_ += 1
        B = B1
    # convert to string
    B = [chr(item) for item in B]
    return ''.join(B)


def _decrypt(cliper, keys):
    """decrypt the cliper

    """
    bsize = len(cliper)

    B = [ord(cliper[index]) for index in xrange(bsize)]
    for key_ in keys: 
        B1 = [0] * bsize
        for index in xrange(bsize):
            if index == 0:
                B1[key_ % bsize] = B[index]
            else:
                B1[(key_ + index) % bsize] = B[index] ^ B[index - 1]
        B = B1
    # convert to string
    B = [chr(item) for item in B]
    return ''.join(B)