

## java

### Installing

```shell
# jdk & jre
# https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-on-ubuntu-22-04

java --version
javac --version
sudo apt install openjdk-19-jdk-headless

```

### Setting Environment Variables

The variable of interest is the `JAVA_HOME` variable, which depends on the installation directory string, i.e.,

```shell
sudo update-alternatives --config java
```
or 

```shell
readlink -f `which java`
```

The `JAVA_HOME` environment variable is defined as

```shell
readlink -f `which java` | sed "s:/bin/java::"
```

i.e., the `/bin/java` suffix of the penultimate command's output is excluded/removed. If the resulting string is `/usr/lib/jvm/java-19-openjdk-amd64`, then

```shell
export JAVA_HOME=/usr/lib/jvm/java-19-openjdk-amd64
```

Or rather, edit `/etc/environment` by appending the definition of `JAVA_HOME` at the end of the file.  An edit mode option is

```shell
sudo vi /etc/environment
```

Subsequently, append

```shell
JAVA_HOME=/usr/lib/jvm/java-19-openjdk-amd64
```

The command `i` starts the edit mode, `ESC` exits the mode, and `:wq` saves; [`vi` commands](https://www.cs.colostate.edu/helpdocs/vi.html).

<br>

## maven

References
* [Apache Maven](https://maven.apache.org/index.html)
* [Maven Installation Guide](https://www.baeldung.com/install-maven-on-windows-linux-mac) by Baeldung

### Installing

```shell
# https://www.man7.org/linux/man-pages/man1/tar.1.html
# https://linux.die.net/man/1/mv
sudo wget -P Downloads https://dlcdn.apache.org/maven/maven-3/3.9.6/binaries/apache-maven-3.9.6-bin.tar.gz
sudo tar -xzvf apache-maven-3.9.6-bin.tar.gz -C /opt
sudo mv /opt/apache-maven-3.9.6/ /opt/maven/
```

Operations
> -x, --extract, --get <br>
> Extract files from an archive.

Options
> -z, --gzip, --gunzip, --ungzip <br>
> Filter the archive through gzip.
>
> -v, --verbose <br>
> Verbosely list files processed.

Selections
> -f, --file=ARCHIVE <br>
> Use archive file or device ARCHIVE.


### Setting Environment Variables

Edit `~/.bashrc` by appending

```shell
export M2_HOME=/opt/maven 
export M2=$M2_HOME/bin 
export MAVEN_OPTS=-Xmx512m 
export PATH="$M2:$PATH"
```

Subsequently, reload the environment variable via command

```shell
source ~/.bashrc
```


<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>