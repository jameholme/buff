# BUFF
*Basic Utility for Finding Faults (BUFF) in AWS*

#### requirements:  
* aws cli
* aws credentials configured
* pip3
* python3
  * argparse 
  * boto3
  * botocore.exceptions

#### usage:  
`buff.py [-h] [--public-s3] [--public-ami] [--security-groups] [--all]`

#### arguments:  
  `-h`, `--help`       show this help message and exit  
  `--public-s3`        checks for publicly accessible S3 buckets  
  `--public-ami`       checks for publicly accessible AMIs  
  `--security-groups`  checks for Security Groups with inbound rules with open access  
  `--all`              performs all available checks  

#### to-do list:  
* write a function that checks iam policies for desired permissions
