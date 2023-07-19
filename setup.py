from setuptools import setup, find_packages

setup(
    name='phpserve',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'phpserve = phpserve.__main__:main'
        ]
    },
    install_requires=[

    ],

    author='Szymon Matuszewski',
    description='A simple PHP server for local development.',
    license='MIT',
)
