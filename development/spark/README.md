

### java

```shell
# jdk & jre
# https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-on-ubuntu-22-04

java --version
javac --version
sudo apt install openjdk-19-jdk-headless

```

For the installation location

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

i.e., the `/bin/java` suffix of the penultimate command's output is excluded/removed.


export JAVA_HOME=/usr/lib/jvm/java-19-openjdk-amd64
