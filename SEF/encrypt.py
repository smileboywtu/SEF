# -*- coding: utf-8 -*-

"""

encrypt the data

using pkcs7 padding

"""

import io
from key import key_generate
from utils import _block_iter, PKCS7_pad, BLOCK_SIZE


def encrypt(data, key, mask, out=None, bsize=BLOCK_SIZE, pkcs7=True):
    """encrypt the data with the key and the mask

    @params:
        data -- encrypt source data
        key -- encrypt key
        mask -- mask for the key
        out -- output stream
        bsize -- encrypt data block size, current is 64 bits
    """
    def _encrypt(data):
        """encrypt the data

        @params:
            bindex -- start index of the block
            seq -- current write index
            locker -- global locker between process
            data -- encrypt data block
            out -- output bytes stream
        """
        B = [ord(data[index]) for index in xrange(bsize)]
        for key_ in key_generate(key, mask):
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
        return bytearray(B)

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
                out.write(_encrypt(last[:bsize]))
            else:
                _bytes = last[:]
        # encrypt the bytes
        out.write(_encrypt(_bytes))

    return out


if __name__ == '__main__':

    out = io.BytesIO()


