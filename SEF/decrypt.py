# -*- coding: utf-8 -*-

"""

decrypt the data from encliper message
PKCS7 depad

"""

import io
from cipher import _decrypt
from utils import PKCS7_depad, _block_iter, BLOCK_SIZE


def decrypt(cliper, keys, out=None, bsize=BLOCK_SIZE, pkcs7=True):
    """decrypt the cliper with key a bsize

    @params:
        cliper -- encrypted message
        keys -- encrypt key sequence
        out -- message output stream
        bsize -- data block size
    """
    # check the output buffer
    if not out:
        out = io.BytesIO()

    # check the cliper
    q, r = divmod(len(cliper), bsize)
    if r != 0:
        raise Exception("cliper is broken")

    for index, _bytes in enumerate(_block_iter(data=cliper, bsize=bsize)):
        # decrypt the block
        data = _decrypt(_bytes, keys)
        # if the last block, depad
        if index == q - 1:
            data = PKCS7_depad(data, bsize) if pkcs7 else data
        # write to output stream
        out.write(data)

    return out
