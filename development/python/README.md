<br>

**Python Environments**

<br>

## Python & Docker

Notes:
* [Base Images](https://pythonspeed.com/articles/base-image-python-docker-images/)

<br>

## Tensorflow

### GPU (Graphics Processing Unit) Computing Environment

Foremost, a virtual conda environment for tensorflow - within a WSL (Windows Subsystem for Linux) operating system ...

```shell
conda create --prefix /opt/miniconda3/envs/tensors python=3.11
```

Next, activate the environment then inspect ...

```shell
conda activate tensors
python -m pip list
conda list
```

Next, the core/background installations for tensorflow ... `cudatoolkit` & `cuDNN`

```shell
conda install -c conda-forge cudatoolkit=11.8.0
python -m pip install nvidia-cudnn-cu11==8.6.0.163

# Additionally (verification via ptxas --version)
conda install -c nvidia cuda-nvcc --yes
ptxas --version
```

... hence, the setting-up of their path variables

```shell
# ascertain that this variable has a value
echo $CONDA_PREFIX

# subsequently
mkdir -p $CONDA_PREFIX/etc/conda/activate.d

echo 'CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))' \
  >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
  
echo 'export LD_LIBRARY_PATH=$CONDA_PREFIX/lib/:$CUDNN_PATH/lib:$LD_LIBRARY_PATH' \
  >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
```

... and probably

```shell
echo 'export XLA_FLAGS=--xla_gpu_cuda_data_dir=$CONDA_PREFIX/lib' \
  >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
```

Additionally ...

```commandline
cd C:\Windows\System32\lxss\lib
del libcuda.so
del libcuda.so.1
mklink libcuda.so libcuda.so.1.1
mklink libcuda.so.1 libcuda.so.1.1
```

<br>

Now, **install `tensorflow`**

```shell
pip install tensorflow==2.12.*
```

Perhaps [TensorRT](https://www.tensorflow.org/install/pip#windows-wsl2:~:text=improve%20latency%20and%20throughput%20for%20inference)

```shell
pip install --upgrade tensorrt
```

and [DASK](https://www.dask.org), [scikit-learn](https://scikit-learn.org/stable/), and code analysis packages; [pytest](https://docs.pytest.org/en/latest/), [coverage](https://coverage.readthedocs.io/en/7.3.3/), [pylint](https://pylint.readthedocs.io/en/latest/), [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/), [flake8](https://flake8.pycqa.org/en/latest/).

```shell
pip install "dask[complete]"
pip install scikit-learn
pip install pytest coverage pylint pytest-cov flake8
```


<br>
<br>

<br> 
<br>

<br> 
<br>

<br> 
<br>