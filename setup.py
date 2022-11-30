from setuptools import setup, find_packages

setup(name='pkg_mc',
      version='0.1',
      description='mc modules and tests',
      url='https://github.com/ranjani-joseph/pkg-mc.git',
      author='Sivaranjani Kandasami',
      license='MIT',
      packages=['pkg_mc'],
      install_requires=['pandas >= 0.15.1'],)