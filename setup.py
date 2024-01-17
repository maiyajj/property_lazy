import setuptools
from lazy_property import __version__

setuptools.setup(
    name='lazy_property',
    version=__version__,
    packages=setuptools.find_packages(),
    url='https://github.com/maiyajj/property_lazy.git',
    license='MIT',
    author='maiyajj',
    author_email='1045373828@qq.com',
    description='Makes properties lazy (ie evaluated only when called)'
)
