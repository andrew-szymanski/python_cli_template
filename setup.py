from distutils.core import setup

setup(
    name='python_cli_template',
    version='1.0',
    author='Andrew Szymanski',
    author_email='',
    packages=['cli'],
    scripts=['cli/cli.py',],
    url='https://github.com/andrew-szymanski/python_cli_template',
    license='LICENSE.txt',
    description='Python CLI template',
    long_description=open('README.txt').read(),
    install_requires=[
        "simplejson>=2.5.2",
    ],
)