"""
Package manager for forecasting_framework
"""

from pathlib import Path
from setuptools import find_packages, setup

version_file = open(Path.joinpath(Path.cwd(), "VERSION"), encoding='utf8')
version = version_file.read().strip()
version_file.close()

setup(
    author="sayantikabanik",
    description="Forecasting FP2",
    include_package_data=True,
    name="forecasting_framework",
    packages=find_packages(),
    url="https://github.com/sayantikabnik/FP2",
    version=version)
