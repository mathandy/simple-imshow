from setuptools import setup
import codecs
import os


VERSION = '1.0.post1'
AUTHOR_NAME = 'Andy Port'
AUTHOR_EMAIL = 'AndyAPort@gmail.com'


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    HERE = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


setup(name='simple-imshow',
      packages=['simshow'],
      version=VERSION,
      description=('A simple tool to display (and read to np.ndarray) images '
                   'from a url, file, image object, etc.'),
      long_description=read("README.rst"),
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
      url='https://github.com/mathandy/simple-imshow',
      download_url='http://github.com/mathandy/simple-imshow/tarball/'+VERSION,
      license='MIT',
      platforms="OS Independent",
      requires=['numpy', 'scipy', 'matplotlib', 'requests'],
      keywords=['image', 'images', 'display', 'read', 'imshow', 'imread'],
      classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Topic :: Multimedia :: Graphics",
            "Topic :: Scientific/Engineering :: Image Recognition",
            "Topic :: Scientific/Engineering :: Information Analysis",
            "Topic :: Scientific/Engineering :: Visualization",
            "Topic :: Software Development :: Libraries :: Python Modules",
            ],
      )
