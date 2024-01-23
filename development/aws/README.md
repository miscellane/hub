
<br>

**Amazon Web Services (AWS)**

<br>

### AWS Toolkit for Visual Studio Code

* [About](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html)
* [Set Up](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/setup-toolkit.html)

<br>

### AWS SAM (Serverless Application Model) CLI

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

<br>

### AWS IAM, Profiles, Policies

* [Getting IAM Identity Center user credentials for the AWS CLI or AWS SDKs](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtogetcredentials.html)
* [Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html)
* [Using temporary credentials with AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html)
* [Using temporary security credentials with the AWS software development kits](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html#using-temp-creds-sdk)
* [Configuring Tokens](https://docs.aws.amazon.com/cli/latest/userguide/sso-configure-profile-token.html#sso-configure-profile-token-auto-sso)
* [Switching to an IAM role (AWS API)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-api.html)
* [AWS managed policies](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/policy-list.html)

<br>

### Development Tools

* [Software Development Kits](https://docs.aws.amazon.com/sdkref/latest/guide/overview.html)
* [`man` reference](https://linux.die.net)

<br>

### Regions, Zones, Endpoints

* [Regional & Zonal Endpoints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-Regions-and-Zones.html)
* [Regions & Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)

<br>

### Amazon S3 (Simple Storage Service)

* [Get started with Amazon S3 buckets and objects using an AWS SDK](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example_s3_Scenario_GettingStarted_section.html)
* Cf. [create](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/bucket/create.html) & [create](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/create_bucket.html)
* Cf. [delete objects](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/bucket/objects.html) & [delete objects](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_objects.html#)


<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>