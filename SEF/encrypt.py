# -*- coding: utf-8 -*-

"""

encrypt the data

using pkcs7 padding

"""

import io
from cipher import _encrypt
from utils import _block_iter, PKCS7_pad, BLOCK_SIZE


def encrypt(data, keys, out=None, bsize=BLOCK_SIZE, pkcs7=True):
    """encrypt the data with the key and the mask

    @params:
        data -- encrypt source data
        key -- encrypt key
        mask -- mask for the key
        out -- output stream
        bsize -- encrypt data block size, current is 64 bits
    """
    # prepare to pad
    q, r = divmod(len(data), bsize)
    q = q if r == 0 else q + 1
    # check pkcs7 and block
    if not pkcs7 and r != 0:
        raise Exception('pkcs7 is disabled, but given unblocked data')

    # prepare the out stream
    if not out:
        out = io.BytesIO()

    for index, _bytes in enumerate(_block_iter(data=data, bsize=bsize)):
        # pad if not enough
        if index == q - 1:
            last = PKCS7_pad(_bytes, bsize) if pkcs7 else _bytes            
            if len(last) > bsize:
                _bytes = last[bsize:]
                out.write(_encrypt(last[:bsize], keys))
            else:
                _bytes = last[:]
        # encrypt the bytes
        out.write(_encrypt(_bytes, keys))

    return out


if __name__ == '__main__':

    out = io.BytesIO()


