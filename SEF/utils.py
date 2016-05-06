# -*- coding:utf-8 -*-

"""

this module is the utils for the encrypt and decrypt process

"""
import io
import binascii
import StringIO


def PKCS7_pad(block, key):
    """pkcs 7 padding"""
    l = len(block)
    output = StringIO.StringIO()
    val = key - (l % key)
    for _ in xrange(val):
        output.write('%02x' % val)
    return block + binascii.unhexlify(output.getvalue())


def PKCS7_depad(block, key):
    """pkcs 7 depadding"""
    nl = len(block)
    val = int(binascii.hexlify(block[-1]), 16)
    if val > key:
        raise ValueError('Input is not padded or padding is corrupt')

    l = nl - val
    return block[:l]


def _block_iter(stream=None, data=None, bsize=0):
    """iterate the block from data or stream
    @params:
        stream -- bytes stream
        data -- bytes block
        bsize -- return block size
    """

    if not (stream or data):
        raise Exception("one of stream of data must not be None Type")

    if data:
        _stream = io.BytesIO(data)

    fp = stream or _stream

    _bytes = fp.read(bsize)
    while _bytes:
        yield _bytes
        _bytes = fp.read(bsize)


if __name__ == '__main__':

    bsize = 3
    message = 'hello, my little daughter.'
    print 'message %s' % message
    for _bytes in _block_iter(data=message, bsize=bsize):
        if len(_bytes) < bsize:
            _bytes = PKCS7_pad(_bytes, bsize)
        print '%s:  %s' % (_bytes, binascii.hexlify(_bytes))