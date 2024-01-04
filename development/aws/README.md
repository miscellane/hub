

AWS SAM CLI

[Installing](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)

```shell
sudo wget -P Downloads https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip 
sudo mkdir Downloads/sam
sudo unzip Downloads/aws-sam-cli-linux-x86_64.zip -d Downloads/sam
sudo mv Downloads/sam/ /opt/sam/
```

Within the `sam` directory

```shell
sudo ./install
sam --version
```