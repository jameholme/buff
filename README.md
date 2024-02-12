# BUFF  
BUFF is a basic utility for finding faults in an AWS account.  
This utility focuses solely on potentially misconfigured resources that allow public access.

#### Requirements:  
* AWS CLI
* AWS credentials configured
* AWS permissions to query the resources
* Pip3
* Python3
  * Argparse 
  * Boto3
  * Botocore.exceptions

#### Usage:  
`python buff.py [-h] [-s3] [-ami] [-sg] [-all]`

#### Arguments:  
  `-h`                 Show this help message and exit  
  `-s3`                Checks for publicly accessible S3 buckets  
  `-ami`               Checks for publicly accessible AMIs  
  `-sg`                Checks for Security Groups with inbound source rules for 0.0.0.0/0  
  `-all`               Performs all available checks  
  
#### Sample Output:
```
[cloudshell-user@ip-10-132-53-132 ~]$ python buff.py -all

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
BBBBBBBBBBBBBBBBB   UUUUUUUU     UUUUUUUUFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀
B::::::::::::::::B  U::::::U     U::::::UF::::::::::::::::::::FF::::::::::::::::::::F     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣿⣿⣿⣿⣷⣦⣄
B::::::BBBBBB:::::B U::::::U     U::::::UF::::::::::::::::::::FF::::::::::::::::::::F     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⠿⡏⢿⡟⠿⠁⢸⣿⣷⡄
BB:::::B     B:::::BUU:::::U     U:::::UUFF::::::FFFFFFFFF::::FFF::::::FFFFFFFFF::::F     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣁⣀⡀⢠⣶⠶⠀⠁⣽⣿⣆
  B::::B     B:::::B U:::::U     U:::::U   F:::::F       FFFFFF  F:::::F       FFFFFF      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠘⣿⣿⣷⡀
  B::::B     B:::::B U:::::D     D:::::U   F:::::F               F:::::F                                           ⠀⠀⢹⣿⣿⣿⣆⠀
  B::::BBBBBB:::::B  U:::::D     D:::::U   F::::::FFFFFFFFFF     F::::::FFFFFFFFFF           ⢀⣠⣴⣶⣶⣶⣦⣄⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⣼⣿⣿⣿⣿⣧⠀  
  B:::::::::::::BB   U:::::D     D:::::U   F:::::::::::::::F     F:::::::::::::::F         ⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣐⢾⣿⣿⣿⣿⣷⣦⣌⡻⣿⣿⣿⣿⣿⣧
  B::::BBBBBB:::::B  U:::::D     D:::::U   F:::::::::::::::F     F:::::::::::::::F         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⡇
  B::::B     B:::::B U:::::D     D:::::U   F::::::FFFFFFFFFF     F::::::FFFFFFFFFF         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢋⡉⠛⠿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⡇
  B::::B     B:::::B U:::::D     D:::::U   F:::::F               F:::::F                   ⣿⣿⣿⣿⣿⣿⣿⣿⡏⢠⣿⣿⣷⡦⠀⣈⣉⣀⣤⣶⣿⣟⣛⠛⠛⠛⠛⠃
  B::::B     B:::::B U::::::U   U::::::U   F:::::F               F:::::F                   ⣿⣿⣿⣿⣿⣿⣿⡿⠀⠾⠛⠋⠁⠐⠺⠿⠿⠿⠛⠛⠉⠁
BB:::::BBBBBB::::::B U:::::::UUU:::::::U FF:::::::FF           FF:::::::FF                 ⣿⣿⣿⣿⣿⣿⠟⢁⣴⣶⣾⠇⠀
B:::::::::::::::::B   UU:::::::::::::UU  F::::::::FF           F::::::::FF                 ⣿⣿⣿⣿⠿⠋⣰⣿⣿⣿⠏⠀
B::::::::::::::::B      UU:::::::::UU    F::::::::FF           F::::::::FF                 ⠛⠛⠋⠁⠐⠛⠛⠛⠛⠋⠀
BBBBBBBBBBBBBBBBB         UUUUUUUUU      FFFFFFFFFFF           FFFFFFFFFFF
    
                                    Basic Utility for Finding Faults (in an AWS Account)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
 * S3 - Checking for publicly accessible buckets:
 !!! Bucket Name: buff-bucket - ARN: arn:aws:s3:::buff-bucket
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 * AMI - Checking for publicly accessible images:
 !!! AMI ID: ami-01a55e04833647668 - Name: buff-ami - Description: N/A
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 * SG - Checking for 0.0.0.0/0 source rules:
 !!! Group ID: sg-055d61af81fa86611 - Group Name: buff-security-group
     - Protocol: tcp, From Port: 22, To Port: 22
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```
#### To-do List:  
* Write a function that checks IAM policies for desired permissions (write, put, delete, etc.)
