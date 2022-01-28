# FP2

### Resources 
- [GitHub CI/CD](https://resources.github.com/ci-cd/)
- [PyTest](https://realpython.com/pytest-python-testing/)
- [Env management using conda](https://towardsdatascience.com/manage-your-python-virtual-environment-with-conda-a0d2934d5195)
- [Pre-Commit hooks](https://pre-commit.com/)

### Installing miniconda/light version of anaconda 
- [Info + details](https://docs.conda.io/en/latest/miniconda.html)

### Commands to create and use conda environment
We are pinning versions of the packages
<details>
  <summary> "conda list" look and feel after you complete the below steps </summary>
  
  ```python

# Name                    Version                   Build  Channel
appdirs                   1.4.4              pyh9f0ad1d_0    conda-forge
attrs                     21.4.0             pyhd8ed1ab_0    conda-forge
brotli                    1.0.9                h3422bc3_6    conda-forge
brotli-bin                1.0.9                h3422bc3_6    conda-forge
brotlipy                  0.7.0           py38hea4295b_1003    conda-forge
ca-certificates           2021.10.8            h4653dfc_0    conda-forge
certifi                   2021.10.8        py38h10201cd_1    conda-forge
cffi                      1.15.0           py38hc67bbb8_0    conda-forge
cfgv                      3.3.1              pyhd8ed1ab_0    conda-forge
charset-normalizer        2.0.9              pyhd8ed1ab_0    conda-forge
cryptography              36.0.1           py38h10d4710_0    conda-forge
cycler                    0.11.0             pyhd8ed1ab_0    conda-forge
distlib                   0.3.4              pyhd8ed1ab_0    conda-forge
editdistance-s            1.0.0            py38h1670459_2    conda-forge
filelock                  3.4.2              pyhd8ed1ab_0    conda-forge
fonttools                 4.28.5           py38hea4295b_0    conda-forge
freetype                  2.10.4               h17b34a0_1    conda-forge
identify                  2.3.7              pyhd8ed1ab_0    conda-forge
idna                      3.1                pyhd3deb0d_0    conda-forge
iniconfig                 1.1.1              pyh9f0ad1d_0    conda-forge
jbig                      2.1               h3422bc3_2003    conda-forge
joblib                    1.1.0              pyhd8ed1ab_0    conda-forge
jpeg                      9d                   h27ca646_0    conda-forge
kiwisolver                1.3.2            py38h1670459_1    conda-forge
lcms2                     2.12                 had6a04f_0    conda-forge
lerc                      3.0                  hbdafb3b_0    conda-forge
libblas                   3.9.0           12_osxarm64_openblas    conda-forge
libbrotlicommon           1.0.9                h3422bc3_6    conda-forge
libbrotlidec              1.0.9                h3422bc3_6    conda-forge
libbrotlienc              1.0.9                h3422bc3_6    conda-forge
libcblas                  3.9.0           12_osxarm64_openblas    conda-forge
libcxx                    12.0.1               h168391b_0    conda-forge
libdeflate                1.8                  h3422bc3_0    conda-forge
libffi                    3.4.2                h3422bc3_5    conda-forge
libgfortran               5.0.0.dev0      11_0_1_hf114ba7_23    conda-forge
libgfortran5              11.0.1.dev0         hf114ba7_23    conda-forge
liblapack                 3.9.0           12_osxarm64_openblas    conda-forge
libopenblas               0.3.18          openmp_h5dd58f0_0    conda-forge
libpng                    1.6.37               hf7e6567_2    conda-forge
libtiff                   4.3.0                h74060c4_2    conda-forge
libwebp-base              1.2.1                h3422bc3_0    conda-forge
libzlib                   1.2.11            hee7b306_1013    conda-forge
llvm-openmp               12.0.1               hf3c4609_1    conda-forge
lz4-c                     1.9.3                hbdafb3b_1    conda-forge
matplotlib                3.5.1            py38h150bfb4_0    conda-forge
matplotlib-base           3.5.1            py38hb140015_0    conda-forge
more-itertools            8.12.0             pyhd8ed1ab_0    conda-forge
munkres                   1.1.4              pyh9f0ad1d_0    conda-forge
ncurses                   6.2                  h9aa5885_4    conda-forge
nodeenv                   1.6.0              pyhd8ed1ab_0    conda-forge
numpy                     1.21.5           py38hb29071a_0    conda-forge
olefile                   0.46               pyh9f0ad1d_1    conda-forge
openjpeg                  2.4.0                h062765e_1    conda-forge
openssl                   1.1.1l               h3422bc3_0    conda-forge
packaging                 21.3               pyhd8ed1ab_0    conda-forge
pandas                    1.3.5            py38h3777fb4_0    conda-forge
patsy                     0.5.2              pyhd8ed1ab_0    conda-forge
pillow                    8.4.0            py38h02acf36_0    conda-forge
pip                       21.3.1             pyhd8ed1ab_0    conda-forge
pluggy                    1.0.0            py38h10201cd_2    conda-forge
pre-commit                2.16.0           py38h10201cd_0    conda-forge
py                        1.11.0             pyh6c4a22f_0    conda-forge
pycparser                 2.21               pyhd8ed1ab_0    conda-forge
pyopenssl                 21.0.0             pyhd8ed1ab_0    conda-forge
pyparsing                 3.0.6              pyhd8ed1ab_0    conda-forge
pysocks                   1.7.1            py38h10201cd_4    conda-forge
pytest                    6.2.5            py38h10201cd_1    conda-forge
python                    3.8.12          hab31e5c_2_cpython    conda-forge
python-dateutil           2.8.2              pyhd8ed1ab_0    conda-forge
python_abi                3.8                      2_cp38    conda-forge
pytz                      2021.3             pyhd8ed1ab_0    conda-forge
pyyaml                    6.0              py38hea4295b_3    conda-forge
readline                  8.1                  hedafd6a_0    conda-forge
requests                  2.26.0             pyhd8ed1ab_1    conda-forge
scikit-learn              1.0.2            py38h2cd4032_0    conda-forge
scipy                     1.7.3            py38hd0c9ec0_0    conda-forge
seaborn                   0.11.2               hd8ed1ab_0    conda-forge
seaborn-base              0.11.2             pyhd8ed1ab_0    conda-forge
setuptools                60.1.1           py38h10201cd_0    conda-forge
six                       1.16.0             pyh6c4a22f_0    conda-forge
sqlite                    3.37.0               h72a2b83_0    conda-forge
statsmodels               0.13.1           py38h691f20f_0    conda-forge
threadpoolctl             3.0.0              pyh8a188c0_0    conda-forge
tk                        8.6.11               he1e0b03_1    conda-forge
toml                      0.10.2             pyhd8ed1ab_0    conda-forge
tornado                   6.1              py38hea4295b_2    conda-forge
unicodedata2              14.0.0           py38hea4295b_0    conda-forge
urllib3                   1.26.7             pyhd8ed1ab_0    conda-forge
virtualenv                20.4.7           py38h10201cd_1    conda-forge
wheel                     0.37.1             pyhd8ed1ab_0    conda-forge
xz                        5.2.5                h642e427_1    conda-forge
yaml                      0.2.5                h642e427_0    conda-forge
zlib                      1.2.11            hee7b306_1013    conda-forge
zstd                      1.5.1                h861e0a7_0    conda-forge
  ```
  
</details>

```shell
conda env create --file environment.yml
```
```shell
conda activate fp2
```
```shell
conda list
```
```shell
conda info
```
```shell
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
- Any test experiements eg- `pickle files generated from autoML` goes under `experiments` directory
- All modelling and related details into `forecasting_framework`, create subdirectories as required 
- Under forecasting_framework there are three submodules `utils`, `model`, `data` 
  - `utils` reusable code components
  - `model` all modelling aspects (python scripts are highly encouraged)
  - `data` pipepine and raw data

### How to contribute to the repo
- Create a separate branch for your usecase 
- Raise PR (dont commit to main under any circumstance)

### Running the data pipline 
- `python pipeline.py` - returns the processed data in ~/data directory
- `dagit -f pipeline.py` - Dagster UI

### Running tests
Install pytest (it is not part of environment.yml/package)
It should be installed locally
- `pip install pytest==6.2.5`
- `pytest tests`
