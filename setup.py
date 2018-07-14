from os.path import dirname, join
from setuptools import find_packages, setup

KEYWORDS = []
CLASSIFIERS = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Natural Language :: French',
    'Operating System :: Unix',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python',
    'Topic :: Software Development',
    'Topic :: Utilities',
    'Topic :: Multimedia :: Sound/Audio :: Speech',
]
INSTALL_REQUIRES = [
    'click==6.7.*',
    'colorama==0.3.*',
    'paho-mqtt==1.3.*',
    'python-dotenv==0.8.*',
    'spotipy==2.4.*',
]

PROJECT_DIR = dirname(__file__)
README_FILE = join(PROJECT_DIR, 'README.md')
ABOUT_FILE = join(PROJECT_DIR, 'src', 'bob', '__about__.py')


def get_readme():
    with open(README_FILE) as fileobj:
        return fileobj.read()


def get_about():
    about = {}
    with open(ABOUT_FILE) as fileobj:
        exec(fileobj.read(), about)
    return about


ABOUT = get_about()

setup(
    name=ABOUT['__title__'],
    version=ABOUT['__version__'],
    description=ABOUT['__summary__'],
    long_description=get_readme(),
    author=ABOUT['__author__'],
    author_email=ABOUT['__email__'],
    url=ABOUT['__uri__'],
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    entry_points={
        'console_scripts': [
            'mirror-bob=bob.__main__:main',
        ],
    },
    install_requires=INSTALL_REQUIRES,
    # TODO: doesn't work
    dependency_links=[
        "git+https://github.com/plamere/spotipy.git"
    ],
    python_requires='>=3.6',
    zip_safe=False
)
