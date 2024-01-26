from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'API Integration of the BotAds service'


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='botadsapi',
    version=VERSION,
    author='Anton',
    author_email='<api@botads.pro>',
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    long_description=readme(),
    packages=find_packages(),
    install_requires=['aiohttp'],
    python_requires='>=3.7',
    keywords=['python', 'botads', 'async', 'asyncio'],
    classifiers=[
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
    ],
    url='https://github.com/BotAdsCod/botads',
    project_urls={
        'Homepage': 'https://github.com/BotAdsCod/botads',
        'Bug Tracker': 'https://github.com/BotAdsCod/botads/issues',
    },
)
