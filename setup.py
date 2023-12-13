from setuptools import setup, find_packages

setup(
    author='cxdzc',
    description='A Python wrapper for the Torn City API, providing access to Torn City data.',
    install_requires=['requests'],
    license='MIT License',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    name='TornAPIWrapper',
    packages=find_packages(),
    url='https://github.com/cxdzc/TornAPIWrapper',
    version='v1.0.0',
)