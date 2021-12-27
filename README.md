# FP2

### Resources 
- [GitHub CI/CD](https://resources.github.com/ci-cd/)
- [PyTest](https://realpython.com/pytest-python-testing/)
- [Env management using conda](https://towardsdatascience.com/manage-your-python-virtual-environment-with-conda-a0d2934d5195)
- [Pre-Commit hooks](https://pre-commit.com/)

### Installing miniconda/light version of anaconda 
- [Info + details](https://docs.conda.io/en/latest/miniconda.html)

### Commands to create and use conda environment
We are pinning python version to 3.8 
```shell
conda env create --file environment.yml
conda activate fp2
conda list
conda info
conda deactivate
```
### Installing the package in local 
```shell
pip install -e .
```

### Basic flow how to make best use of the workflow
- Clone the repo
- Create the env using the above commands 
- Install the package 
- All the tests goes into the `tests` directory 
- Any random test experiements eg- checking data stats etc goes under `experiments` directory
- All modelling and related details into `forecasting_framework`, create subdirectories as required 
