# BUFF
*Basic Utility for Finding Faults (BUFF) in AWS*

#### requirements:  
* aws cli
* aws credentials configured
* python3
  * argparse 
  * boto3
  * botocore.exceptions

#### usage:  
`buff.py [-h] [--public-s3] [--iam-write] [--iam-full-access] [--public-ami] [--security-groups] [--all]`

#### arguments:  
  `-h`, `--help`       show this help message and exit  
  `--public-s3`        checks for publicly accessible S3 buckets  
  `--iam-write`        checks for IAM policies with Write access  
  `--iam-full-access`  checks for IAM policies with full access or administrator level access  
  `--public-ami`       checks for publicly accessible AMIs  
  `--security-groups`  checks for Security Groups with inbound rules with open access  
  `--all`              performs all available checks  
