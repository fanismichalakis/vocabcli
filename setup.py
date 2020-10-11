from setuptools import setup
setup(
    name = 'vocabcli',
    version = '0.1.0',
    packages = ['vocabcli'],
    entry_points = {
        'console_scripts': [
            'vocabcli = vocabcli.__main__:main'
        ]
    })