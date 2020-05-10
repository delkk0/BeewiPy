import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BeewiPy",
    version="0.0.1",
    author="David Polo",
    author_email="dpolot@gmail.com",
    description="A python library to interact with Beewi SmartBulb",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/delkk0/BeewiPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Topic :: Home Automation",
    ],
    python_requires='>=3.3',
)

