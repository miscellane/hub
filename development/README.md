<br>

# Linux Environment


Including [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/) kernels.  Apriori

```shell
sudo apt update
sudo apt upgrade
```

Additionally, often inspect the GNU Privacy Guard (<abbr title="GNU Privacy Guard">GPG</abbr>) keys via

```shell
gpg --list-keys
gpg --list-secret-keys
```

Print environment variables via

```shell
# https://www.cyberciti.biz/faq/linux-list-all-environment-variables-env-command/
printenv
```

<br>

**CONTENT**

* [wget](#wget)
* [GIT](#git)
* [CONDA](#conda)
* [IntelliJ IDEA](#intellij-idea)
* [NVIDIA](#nvidia)
* [Docker & JAX](#docker--jax)
* [Docker, NVIDIA, Windows 11, & Windows Subsystem for Linux Kernels](#docker-nvidia-windows-11--windows-subsystem-for-linux-kernels)
  * [Docker Desktop](#docker-desktop)
  * [NVIDIA Docker](#nvidia-docker)
  * [NVIDIA Container Toolkit](#nvidia-container-toolkit)
  * [Development Containers](#development-containers)

<br>

## wget

The <a href="https://www.gnu.org/software/wget/manual/wget.html" target="_blank">wget</a> utility:

```shell
sudo apt install wget ca-certificates
```

`ca-certificates` allows applications that are secure sockets layer (SSL) dependent to verify the authenticity of SSL connections; SSL is a deprecated tool.

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

## CONDA

Via `miniconda`.  Foremost, check the python version

```shell
python --version
```

### The Installer

Subsequently, `get` the [installer](https://docs.conda.io/en/latest/miniconda.html#linux-installers) relative to the system's python version, e.g.,

```shell
# if python 3.10.*
sudo wget -P Downloads https://repo.anaconda.com/miniconda/Miniconda3-py310_23.5.2-0-Linux-x86_64.sh
cd Downloads
sudo chmod +x Miniconda3-py310_23.5.2-0-Linux-x86_64.sh
```

### Install

Install in the specified directory

```shell
# Include <-b> for automatic acceptance of the terms & conditions
sudo bash Miniconda3-py310_23.5.2-0-Linux-x86_64.sh -p /opt/miniconda3

$ Do you wish the installer to initialize Miniconda3 by running conda init?
>>> no
```

### Set the Path Variable

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

### Set-up

Next, within a new terminal

```shell
conda init bash
conda config --set auto_activate_base false
sudo chown -R $USER:$USER /opt/miniconda3
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

References:
* [Connecting Docker](https://www.jetbrains.com/help/idea/docker.html#connect_to_docker)
  * [Containers](https://www.jetbrains.com/help/idea/connect-to-devcontainer.html#recent_projects)
  * [Demo](https://github.com/IdeaUJetBrains/idea-demo-devcontainers)
* [Remote Python Entities](https://www.jetbrains.com/help/idea/configuring-remote-python-sdks.html)


<br>

## NVIDIA

In progress ... https://developer.nvidia.com/

The references herein outline the fundamental NVIDIA installations required within Windows 11 that ensure the ability to run CUDA dependent programs within Windows 11 or a WSL (Windows Subsystem for Linux) kernel.  Beware of the mappings between CUDA Toolkit Version & CUDA Driver Version: [Matrix](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html#id5)

* Install [Drivers](https://www.nvidia.co.uk/Download/index.aspx?lang=en-uk)
* Install [NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)
  * [Release Notes](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html)
* Install [cuDNN](https://developer.nvidia.com/cudnn)
  * [Windows](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html#install-windows)

<br>

## Docker & JAX

References for running JAX dependent programs via docker containers.

* [Early Access JAX Containers](https://developer.nvidia.com/jax-container-early-access)
* [JAX Containers](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/jax)


<br>


## Docker, NVIDIA, Windows 11, & Windows Subsystem for Linux Kernels

This set-up ensures that docker containers can run CUDA GPU (Graphics Processing Unit) enabled programs.


### Docker Desktop

Foremost, uninstall docker within each WSL (Windows Subsystem for Linux) operating system that will be associated with Docker Desktop

```shell
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

[This avoids conflicts](https://docs.docker.com/desktop/wsl/#:~:text=To%20avoid%20any%20potential%20conflicts).  Subsequently, [install Docker Desktop](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers#install-docker-desktop).  Read [...](https://www.docker.com/products/docker-desktop/alternatives/) for an outline of the advantages of Docker Desktop vis-à-vis Docker Engine.


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

### Development Containers

* https://containers.dev/implementors/json_reference/
* https://code.visualstudio.com/docs/devcontainers/containers#_quick-start-open-an-existing-folder-in-a-container
* https://code.visualstudio.com/docs/devcontainers/tutorial


<br>
<br>

<br> 
<br>

<br> 
<br>

<br> 
<br>
