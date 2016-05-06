# -*- coding: utf-8 -*-

"""

decrypt the data from encliper message
PKCS7 depad

"""

import io
from key import key_generate
from utils import PKCS7_depad, _block_iter


BLOCK_SIZE = 8L


def decrypt(cliper, key, mask, out=None, bsize=BLOCK_SIZE):
    """decrypt the cliper with key a bsize

    @params:
        cliper -- encrypted message
        key -- encrypt key
        mask -- mask using with the key
        out -- message output stream
        bsize -- data block size
    """
    def _decrypt(cliper, key, mask):
        """decrypt the cliper

        """
        B = [ord(cliper[index]) for index in xrange(bsize)]
        for key_ in key_generate(key, mask, reverse=True):
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

    # check the output buffer
    if not out:
        out = io.BytesIO()

    # check the cliper
    q, r = divmod(len(cliper), bsize)
    if r != 0:
        raise Exception("cliper is broken")

    for index, _bytes in enumerate(_block_iter(data=cliper, bsize=bsize)):
        # decrypt the block
        data = _decrypt(_bytes, key, mask)
        # if the last block, depad
        if index == q - 1:
            data = PKCS7_depad(data, bsize)
        # write to output stream
        out.write(data)

    return out
