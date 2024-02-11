import argparse
import boto3
from botocore.exceptions import NoCredentialsError

def buff_banner():
    print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
BBBBBBBBBBBBBBBBB   UUUUUUUU     UUUUUUUUFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀
B::::::::::::::::B  U::::::U     U::::::UF::::::::::::::::::::FF::::::::::::::::::::F     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣿⣿⣿⣿⣷⣦⣄
B::::::BBBBBB:::::B U::::::U     U::::::UF::::::::::::::::::::FF::::::::::::::::::::F     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⠿⡏⢿⡟⠿⠁⢸⣿⣷⡄
BB:::::B     B:::::BUU:::::U     U:::::UUFF::::::FFFFFFFFF::::FFF::::::FFFFFFFFF::::F     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣁⣀⡀⢠⣶⠶⠀⠁⣽⣿⣆
B::::B     B:::::B U:::::U     U:::::U   F:::::F       FFFFFF  F:::::F       FFFFFF      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠘⣿⣿⣷⡀
B::::B     B:::::B U:::::D     D:::::U   F:::::F               F:::::F                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣆⠀
B::::BBBBBB:::::B  U:::::D     D:::::U   F::::::FFFFFFFFFF     F::::::FFFFFFFFFF          ⢀⣠⣴⣶⣶⣶⣦⣄⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⣼⣿⣿⣿⣿⣧⠀  
B:::::::::::::BB   U:::::D     D:::::U   F:::::::::::::::F     F:::::::::::::::F         ⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣐⢾⣿⣿⣿⣿⣷⣦⣌⡻⣿⣿⣿⣿⣿⣧
B::::BBBBBB:::::B  U:::::D     D:::::U   F:::::::::::::::F     F:::::::::::::::F         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⡇
B::::B     B:::::B U:::::D     D:::::U   F::::::FFFFFFFFFF     F::::::FFFFFFFFFF         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢋⡉⠛⠿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⡇
B::::B     B:::::B U:::::D     D:::::U   F:::::F               F:::::F                   ⣿⣿⣿⣿⣿⣿⣿⣿⡏⢠⣿⣿⣷⡦⠀⣈⣉⣀⣤⣶⣿⣟⣛⠛⠛⠛⠛⠃
B::::B     B:::::B U::::::U   U::::::U   F:::::F               F:::::F                   ⣿⣿⣿⣿⣿⣿⣿⡿⠀⠾⠛⠋⠁⠐⠺⠿⠿⠿⠛⠛⠉⠁
BB:::::BBBBBB::::::B U:::::::UUU:::::::U FF:::::::FF           FF:::::::FF               ⣿⣿⣿⣿⣿⣿⠟⢁⣴⣶⣾⠇⠀
B:::::::::::::::::B   UU:::::::::::::UU  F::::::::FF           F::::::::FF               ⣿⣿⣿⣿⠿⠋⣰⣿⣿⣿⠏⠀
B::::::::::::::::B      UU:::::::::UU    F::::::::FF           F::::::::FF               ⠛⠛⠋⠁⠐⠛⠛⠛⠛⠋⠀
BBBBBBBBBBBBBBBBB         UUUUUUUUU      FFFFFFFFFFF           FFFFFFFFFFF
    
                                    Basic Utility for Finding Faults (in an AWS Account)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)

def tildes():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def public_s3_buckets():
    def list_all_buckets():
        s3_client = boto3.client('s3')
        response = s3_client.list_buckets()
        print(" * S3 - Checking for publicly accessible buckets:")
        found_public_bucket = False
        for bucket in response['Buckets']:
            bucket_name = bucket['Name']
            bucket_arn = f"arn:aws:s3:::{bucket_name}"
            found_public_bucket |= check_block_public_access(bucket_name, bucket_arn)
        if not found_public_bucket:
            print(" --- No publicly accessible S3 buckets found")

    def check_block_public_access(bucket_name, bucket_arn):
        s3_client = boto3.client('s3')
        response = s3_client.get_public_access_block(Bucket=bucket_name)
        if response['PublicAccessBlockConfiguration']['BlockPublicAcls'] or \
            response['PublicAccessBlockConfiguration']['IgnorePublicAcls'] or \
            response['PublicAccessBlockConfiguration']['BlockPublicPolicy'] or \
            response['PublicAccessBlockConfiguration']['RestrictPublicBuckets']:
            return False
        else:
            print(f" !!! Bucket Name: {bucket_name} - ARN: {bucket_arn}")
            return True
    list_all_buckets()

def public_amis():
    ec2_client = boto3.client('ec2')
    sts_client = boto3.client('sts')
    account_id = sts_client.get_caller_identity()['Account']
    response = ec2_client.describe_images(Owners=[account_id], Filters=[{'Name': 'is-public', 'Values': ['true']}])
    print(" * AMI - Checking for publicly accessible images:")
    if not response['Images']:
        print(" --- No publicly accessible AMIs were found")
        return
    for image in response['Images']:
        print(f" !!! AMI ID: {image['ImageId']} - Name: {image.get('Name', 'N/A')} - Description: {image.get('Description', 'N/A')}")

def security_groups_open_access():
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_security_groups()
    print(" * SG - Checking for 0.0.0.0/0 source rules:")
    open_access_groups = []
    for group in response['SecurityGroups']:
        for permission in group['IpPermissions']:
            if permission.get('IpRanges'):
                for ip_range in permission['IpRanges']:
                    if ip_range['CidrIp'] == '0.0.0.0/0':
                        open_access_groups.append(group)
                        break
        if open_access_groups and group in open_access_groups:
            print(f" !!! Group ID: {group['GroupId']} - Group Name: {group['GroupName']}")
            for permission in group['IpPermissions']:
                protocol = permission['IpProtocol']
                from_port = permission.get('FromPort', 'All')
                to_port = permission.get('ToPort', 'All')
                print(f"     - Protocol: {protocol}, From Port: {from_port}, To Port: {to_port}")
    if not open_access_groups:
        print(" --- No security groups found with 0.0.0.0/0 source rules")
    return open_access_groups

def all_checks():
    public_s3_buckets()
    tildes()
    public_amis()
    tildes()
    security_groups_open_access()
    tildes()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basic Utility for Finding Faults (BUFF) in AWS")
    
    parser.add_argument("-s3", action="store_true", help="checks for publicly accessible S3 buckets")
    parser.add_argument("-ami", action="store_true", help="checks for publicly accessible AMIs")
    parser.add_argument("-sg", action="store_true", help="checks for Security Groups with inbound source rules for 0.0.0.0/0")
    parser.add_argument("-all", action="store_true", help="performs all available checks")
    args = parser.parse_args()

    if args.s3:
        try:
            buff_banner()
            public_s3_buckets()
        except NoCredentialsError:
            print("AWS credentials are not configured. Please run 'aws configure' to set them up.")
    elif args.ami:
        try:
            buff_banner()
            public_amis()
        except NoCredentialsError:
            print("AWS credentials are not configured. Please run 'aws configure' to set them up.")
    elif args.sg:
        try:
            buff_banner()
            security_groups_open_access()
        except NoCredentialsError:
            print("AWS credentials are not configured. Please run 'aws configure' to set them up.")
    elif args.all:
        try:
            buff_banner()
            all_checks()
        except NoCredentialsError:
            print("AWS credentials are not configured. Please run 'aws configure' to set them up.")
    else:
        print("Please provide a valid option. Use -h, or --help for available options")
