#setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ma-lambdata-13", # the name that you will install via pip
    version="1.0",
    author="Miriam Ali",
    author_email="@gmail.com",
    description="A short description",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/maiali13/ma-lambdata-13",
    #keywords="",
    packages=find_packages() # ["ma13_lambdata"]
)