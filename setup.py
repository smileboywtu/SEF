# -*-  coding: utf-8 -*-

"""

    sef encrypt and decrypt use the cython

"""


from Cython.Distutils import build_ext
from setuptools import setup, find_packages, Extension

cipher = Extension(
    'cipher',
    sources=['lib/cipher.pyx', ],
    include_dirs=['lib/']
)

setup(
    name='SEF',
    version='1.0',
    install_requires=['cython'],
    ext_modules=[cipher],
    cmdclass={'build_ext': build_ext},
    packages=find_packages(),
    description='symmetry data encryption based on fountain code',
    author='smileboywtu',
    author_email='smileboywtu@gmail.com',
    url='https://github.com/smileboywtu/SEF',
    license='Apache2'
)
