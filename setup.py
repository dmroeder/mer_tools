import setuptools
import mer_tools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mer_tools",
    version=mer_tools.__version__,
    author="Dustin Roeder",
    author_email="dmroeder@gmail.com",
    description="Tools for extracting information from MER files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache License 2.0",
    url="https://github.com/dmroeder/pylogix",
    packages=setuptools.find_packages(),
    install_requires=['olefile',],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
