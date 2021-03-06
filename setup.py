import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='responsive-img',
    version='0.9',
    packages=['responsive'],
    include_package_data=True,
    license='MIT License',  # example license
    description='Create resized versions of existing images using a url schema',
    long_description=README,
    url='http://www.ostmodern.co.uk/',
    author='Kip Parker',
    author_email='kip@kipparker.co.uk',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        "Django>=1.6",
        "Pillow>=2.8.1"
    ],
    test_suite="runtests.runtests",
    tests_require=[],
)
