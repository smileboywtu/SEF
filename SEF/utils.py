# -*- coding:utf-8 -*-

"""

this module is the utils for the encrypt and decrypt process

"""

import io
import binascii
import StringIO


BLOCK_SIZE = 8L


def tester(func1, func2, data, keys):
    """test the func1 and func2 output for input data and keys


    """
    print 'source: ', data
    # copy data
    dcopy1 = (data + ' ')[:-1]
    dcopy2 = (data + ' ')[:-1]
    out1 = func1(dcopy1, keys)
    out2 = func2(dcopy2, keys)
    print 'func1: ', out1
    print 'func2: ', out2
    assert out1 == out2


def PKCS7_pad(block, bsize):
    """pkcs 7 padding

    always pad the block even the block is full
    """
    size_ = len(block)
    output = StringIO.StringIO()
    val = bsize - (size_ % bsize)
    if val == 0:
        output.write('{:02x}'.format(bsize) * bsize)
    else:
        output.write('{:02x}'.format(val) * val)
    return block + binascii.unhexlify(output.getvalue())


def PKCS7_depad(block, bsize):
    """pkcs 7 depadding

    make sure the block if full of the bsize
    """
    if len(block) != bsize:
        raise ValueError("block size if not equal to require size")
    val = int(binascii.hexlify(block[-1]), 16)
    # not pad
    if val > bsize:
        return block
    end = bsize - val
    return block[:end]


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
    message = 'hello, my little daughte'
    print 'message %s' % message
    q, r = divmod(len(message), bsize)
    for index, _bytes in enumerate(_block_iter(data=message, bsize=bsize)):
        if len(_bytes) < bsize:
            _bytes = PKCS7_pad(_bytes, bsize)
        elif index == q - 1:
            _bytes = PKCS7_pad(_bytes, bsize)
            print '%s:  %s' % (_bytes[:bsize], binascii.hexlify(_bytes[:bsize]))
            _bytes = _bytes[bsize:]
        print '%s:  %s' % (_bytes, binascii.hexlify(_bytes))
