<br>

**Notes**

<br>

* [java](#java)
  * [Installing](#installing-java)
  * [Environment Variables](#environment-variables-java)
* [maven](#maven)
  * [Installing](#installing-maven)
  * [Environment Variables](#environment-variables-maven)
* [hadoop](#hadoop)
  * [Installing](#installing-hadoop)
  * [Environment Variables](#environment-variables-hadoop)
* [scala](#scala)
  * [Installing](#installing-scala)
  * [Environment Variables](#environment-variables-scala)


<br>

## JAVA

References
* [Installing JAVA](https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-on-ubuntu-22-04)

### Installing: Java

```shell
# jdk & jre
sudo apt install openjdk-19-jdk-headless
java --version
javac --version
```

### Environment Variables: Java

The environment variable of interest is the `JAVA_HOME` variable, which depends on the installation directory string, i.e.,

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

## MAVEN

References
* [Apache Maven](https://maven.apache.org/index.html)
* [Maven Installation Guide](https://www.baeldung.com/install-maven-on-windows-linux-mac) by Baeldung

### Installing: Maven

```shell
# get
sudo wget -P Downloads https://dlcdn.apache.org/maven/maven-3/3.9.6/binaries/apache-maven-3.9.6-bin.tar.gz

# https://www.man7.org/linux/man-pages/man1/tar.1.html
sudo tar -xzvf apache-maven-3.9.6-bin.tar.gz -C /opt

# https://linux.die.net/man/1/mv
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


### Environment Variables: Maven

Edit `~/.bashrc` by appending

```shell
export M2_HOME=/opt/maven 
export M2=$M2_HOME/bin 
export MAVEN_OPTS=-Xmx512m 
export PATH="$M2:$PATH"
```

Subsequently, reload the environment variables via command

```shell
source ~/.bashrc
```

Hence

```shell
mvn -version
```

<br>

## HADOOP

### Installing: Hadoop

* [Installing](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html#Installing_Software)

```shell
# get
sudo wget -P Downloads https://dlcdn.apache.org/hadoop/common/stable/hadoop-3.3.6.tar.gz

# https://www.man7.org/linux/man-pages/man1/tar.1.html
sudo tar -xzvf Downloads/hadoop-3.3.6.tar.gz -C /opt

# https://linux.die.net/man/1/mv
sudo mv /opt/hadoop-3.3.6/ /opt/hadoop/
```

### Environment Variables: Hadoop

Edit `/etc/hadoop/hadoop-env.sh`; ref. [Environment Variables: Java](#environment-variables-java)

```shell
export JAVA_HOME=/usr/lib/jvm/java-19-openjdk-amd64
export HADOOP_HOME=/opt/hadoop
```

Edit `~/.bashrc` by appending

```shell
export HADOOP_HOME=/opt/hadoop 
export PATH="$HADOOP_HOME/bin:$PATH"
```

Subsequently, reload the environment variables via command

```shell
source ~/.bashrc
```

Hence

```shell
hadoop version
```

<br>

## Scala

### Installing: Scala

```shell
sudo wget -P Downloads https://downloads.lightbend.com/scala/2.13.12/scala-2.13.12.tgz
sudo tar -xzvf Downloads/scala-2.13.12.tgz -C /opt
sudo mv /opt/scala-2.13.12/ /opt/scala/
```

### Environment Variables: Scala

Edit `~/.bashrc` by appending

```shell
export SCALA_HOME=/opt/scala 
export PATH="$SCALA_HOME/bin:$PATH"
```

Subsequently, reload the environment variables via command

```shell
source ~/.bashrc
```

Hence

```shell
scala -version
```

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>