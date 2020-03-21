from setuptools import setup

setup(
    name='webotron-80',
    version='0.1',
    author='me',
    author_email='test@test.com',
    description='Webotron 80 is a tool to deploy static sites',
    licens='GPLv+',
    packages=['webotron'],
    url='https://github.com/Alvarosantoma/automating-aws-with-python',
    install_requirs=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        webotron=webotron.webotron:cli
        '''
)
