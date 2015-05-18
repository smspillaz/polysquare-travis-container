# /setup.py
#
# Installation and setup script for psqtraviscontainer
#
# See /LICENCE.md for Copyright information
"""Installation and setup script for psqtraviscontainer."""

from setuptools import find_packages, setup

setup(name="psqtraviscontainer",
      version="0.0.4",
      description="Polysquare Travis-CI Container Root",
      long_description_markdown_filename="README.md",
      author="Sam Spilsbury",
      author_email="smspillaz@gmail.com",
      classifiers=["Development Status :: 3 - Alpha",
                   "Intended Audience :: Developers",
                   "Topic :: Software Development :: Build Tools",
                   "License :: OSI Approved :: MIT License",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3.3",
                   "Programming Language :: Python :: 3.4"],
      url="http://github.com/polysquare/polysquare-travis-container",
      license="MIT",
      keywords="development travis",
      packages=find_packages(exclude=["test"]),
      dependency_links=[
          ("https://github.com/smspillaz/urlgrabber/tarball/master"
           "#egg=urlgrabber-3.10.1")
      ],
      install_requires=["configargparse",
                        "pycurl",
                        "python-debian",
                        "six",
                        "shutilwhich",
                        "urlgrabber==3.10.1",
                        "colorama",
                        "tempdir",
                        "termcolor"],
      extras_require={
          "green": [
              "coverage",
              "testtools",
              "shutilwhich",
              "nose",
              "nose-parameterized",
              "mock",
              "setuptools-green",
              "tempdir"
          ],
          "polysquarelint": [
              "polysquare-setuptools-lint"
          ],
          "upload": [
              "setuptools-markdown"
          ]
      },
      entry_points={
          "console_scripts": [
              "psq-travis-container-create=psqtraviscontainer.create:main",
              "psq-travis-container-exec=psqtraviscontainer.use:main"
          ]
      },
      test_suite="nose.collector",
      zip_safe=True,
      include_package_data=True)
