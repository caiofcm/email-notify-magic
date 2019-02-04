import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="email-notify-magic",
    version="0.0.1",
    description="A Jupyter magic for sending e-mail after cell completion",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/caiofcm/email-notify-magic",
    author='Caio Marcellos',
    author_email='caiocuritiba@gmail.com',
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    # packages=["vscode_debugger_magic"],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=["ipython"],
)
