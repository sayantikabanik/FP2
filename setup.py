from pathlib import Path
from setuptools import find_packages, setup

version_file = open(Path.joinpath(Path.cwd(), "VERSION"))
version = version_file.read().strip()

setup(
    author="sayantikabanik",
    description="Forecasting FP2",
    include_package_data=True,
    name="forecasting_framework",
    packages=find_packages(),
    url="https://github.com/sayantikabnik/FP2",
    version=version)
