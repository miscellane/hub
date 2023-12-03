<br>

**LINUX Environment Notes**

Especially [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/).  Apriori

```shell
sudo apt update
sudo apt upgrade
```

Inspecting the GNU Privacy Guard (<abbr title="GNU Privacy Guard">GPG</abbr>) keys

```shell
gpg --list-keys
gpg --list-secret-keys
```

<br>

## IntelliJ IDEA

```shell
# get
sudo wget -P Downloads https://download.jetbrains.com/idea/ideaIC-2022.3.3.tar.gz
sudo tar -xzf ideaIC-2022.3.3.tar.gz -C /opt 

# starting within idea bin
cd .../bin
./idea.sh
```

<br>
<br>

## GNU `wget`

The <a href="https://www.gnu.org/software/wget/manual/wget.html" target="_blank">wget</a> utility:

```shell
sudo apt install wget ca-certificates
```

`ca-certificates` allows applications that are secure sockets layer (SSL) dependent to verify the authenticity of SSL connections; SSL is a deprecated tool.

<br>
<br>

## GIT

Update `git` via the `git-core/ppa` <abbr title="Personal Package Archive">PPA</abbr> (Personal Package Archive).

```shell
sudo add-apt-repository ppa:git-core/ppa
sudo apt update
sudo apt list --upgradable
sudo apt install git-all
```

Subsequently, [set up & configure](https://git-scm.com/book/en/v2/Appendix-C%3A-Git-Commands-Setup-and-Config) `git` ...

```shell
git config --global user.name ""
git config --global user.email "...@users.noreply.github.com"
git config --global core.editor "vim --nofork"
git config --global init.defaultBranch master

ssh-keygen -t ed25519 -C "...@users.noreply.github.com"

cat ~/.ssh/id_ed25519.pub
```

There are instances whereby multiple accounts have to be managed per git client, e.g., study [GitHub Multiple Accounts](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-your-personal-account/managing-multiple-accounts).

<br>
<br>

## NVIDIA

In progress ... https://developer.nvidia.com/

### Steps

Beware of the mappings between CUDA Toolkit Version & CUDA Driver Version: [Matrix](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html#id5)

* Install [Drivers](https://www.nvidia.co.uk/Download/index.aspx?lang=en-uk)
* Install [NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)
  * [Release Notes](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html)
* Install [cuDNN](https://developer.nvidia.com/cudnn)
  * [Linux](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html#install-linux)
  * [Windows](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html#install-windows)

<br>

### Complimentary Tools

JAX
* [Early Access JAX Containers](https://developer.nvidia.com/jax-container-early-access)
* [JAX Containers](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/jax)


<br>
<br>


## Docker

<br>

### Docker Desktop

Foremost, uninstall docker within each WSL (Windows Subsystem for Linux) operating system that will be associated with Docker Desktop

```shell
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

[This avoids conflicts](https://docs.docker.com/desktop/wsl/#:~:text=To%20avoid%20any%20potential%20conflicts).  Subsequently, [install Docker Desktop](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers#install-docker-desktop).  Read [...](https://www.docker.com/products/docker-desktop/alternatives/) for an outline of the advantages of Docker Desktop vis-à-vis Docker Engine.

<br>
<br>

### NVIDIA Docker

**Initially**, [address possible conflict points](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/troubleshooting.html) between NVIDIA Docker & NVIDIA Container Toolkit

```shell
sudo rm /etc/apt/sources.list.d/nvidia-docker.list && rm /etc/apt/sources.list.d/nvidia-container-toolkit.list && \
	rm /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg && rm /usr/share/keyrings/nvidia-docker-keyring.gpg
```

In addition to `/etc/apt/sources.list.d/` & `/usr/share/keyrings/`, the directory `/etc/apt/trusted.gpg.d` will sometimes be of interest.  **Then**

```shell
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)

echo $distribution

curl -fsSL https://nvidia.github.io/nvidia-docker/gpgkey | \
    sudo gpg --dearmour -o /usr/share/keyrings/nvidia-docker-keyring.gpg
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-docker-keyring.gpg] https://#g' | \
      sudo tee /etc/apt/sources.list.d/nvidia-docker.list
```

Next

```shell
sudo apt update
sudo apt install -y nvidia-docker2
```

<br>
<br>

### NVIDIA [Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/index.html)

[**Setting Up NVIDIA Container Toolkit**](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#setting-up-nvidia-container-toolkit) outlines the setting-up steps; [installing](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installing-the-nvidia-container-toolkit).  Foremost, set up the package directory & <abbr title="GNU Privacy Guard">GPG</abbr> key

```shell
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | \
  sudo gpg --dearmour -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg     
curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

Next install `nvidia-container-toolkit`

```shell
sudo apt update
sudo rm -r /etc/nvidia-container-runtime
sudo apt install -y nvidia-container-toolkit
```

The second command ensures that the final command can create/recreate the directory `/etc/nvidia-container-runtime`. Subsequently, ensure the Docker daemon recognises NVIDIA Container Runtime by running a configuration script

```shell
# Initially, ensure /etc/docker exists; option -p ensures all the directories of a path hierarchy exist
sudo mkdir -p /etc/docker
sudo nvidia-ctk runtime configure --runtime=docker
```

Restart Docker Desktop; perhaps run `sudo nvidia-ctk runtime configure --runtime=containerd` also, and restart Desktop Docker.  Subsequently, run

```shell
docker run --rm --gpus all nvidia/cuda:{cuda_version}-base-ubuntu{ubuntu_version} nvidia-smi
```

wherein

* `cuda_version`: {major}.{minor}.{build}, e.g., 12.2.2
* `ubuntu_version`: {major}.{minor}, e.g., 22.04

e.g.,

```shell
docker run --rm --gpus all nvidia/cuda:12.2.2-base-ubuntu22.04 nvidia-smi
```

Important, ensure that a [`nvidia/cuda` tag](https://hub.docker.com/r/nvidia/cuda/tags) that is inline with the machine's CUDA & Ubuntu versions exists.  The machine's cuda version is retrievable via

```shell
nvidia-smi
```

within a linux system.  Alternatively, the Windows Command Prompt command

```commandline
nvcc -V
```

will print the cuda version.  In the case of Ubuntu

```shell
cat /etc/os-release
```

prints the Ubuntu version, amongst other details; alternatively, `lsb_release -a` or `cat /etc/issue`.

<br>
<br>

## Virtual Environments

<br>

### Software: `miniconda`

Foremost, check the python version

```shell
python --version
```

#### Get

Subsequently, `get` the [installer](https://docs.conda.io/en/latest/miniconda.html#linux-installers) relative to the system's python version, e.g.,

```shell
# if python 3.10.*
sudo wget -P Downloads https://repo.anaconda.com/miniconda/Miniconda3-py310_23.5.2-0-Linux-x86_64.sh
cd Downloads
sudo chmod +x Miniconda3-py310_23.5.2-0-Linux-x86_64.sh
```

#### Install

Install in the specified directory

```shell
# Include <-b> for automatic acceptance of the terms & conditions
sudo bash Miniconda3-py310_23.5.2-0-Linux-x86_64.sh -p /opt/miniconda3

$ Do you wish the installer to initialize Miniconda3 by running conda init?
>>> no
```

#### Path Variable

Open `/etc/profile`, i.e.,

```shell
sudo vi profile
```

and append

```bash
if ! [[ $PATH =~ "/opt/miniconda3/bin" ]]; then
	PATH="/opt/miniconda3/bin:$PATH"
fi
```

The command `i` starts the edit mode, `ESC` exits the mode, and `:wq` saves; [`vi` commands](https://www.cs.colostate.edu/helpdocs/vi.html).  **Exit** the terminal.

#### Set-up

Next, within a new terminal

```shell
conda init bash
conda config --set auto_activate_base false
sudo chown -R $USER:$USER /opt/miniconda3
```

<br>
<br>

### A sample *Tensorflow GPU (Graphics Processing Unit)* virtual environment

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

The upcoming sample project depends on ...

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
