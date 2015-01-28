"""setup.py for the berth package."""

from setuptools import setup

setup(
    name='berth',
    version='1.0.0',
    description='Utility to generate package files using Docker containers',
    author='Falcon Social',
    url='https://github.com/FalconSocial/berth',
    license='MIT',
    packages=['berth'],
    install_requires=[
        'click >= 3, < 4',
        'docker-py >= 0.7, < 0.8',
        'PyYAML >= 3, < 4',
    ],
    entry_points={
        'console_scripts': [
            'berth = berth.cli:main',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: System :: Archiving :: Packaging',
        'Topic :: System :: Software Distribution',
        'Topic :: Utilities',
    ],
)
