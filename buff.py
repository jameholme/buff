import argparse
import boto3
from botocore.exceptions import NoCredentialsError

def public_s3_buckets():
    s3_client = boto3.client('s3')
    response = s3_client.list_buckets()
    public_buckets = [bucket['Name'] for bucket in response['Buckets'] if public_s3_buckets(s3_client, bucket['Name'])]
    print("Checking for publicly accessible S3 buckets")
    if public_buckets:
        print("Publicly accessible S3 buckets:")
        for bucket in public_buckets:
            print(f"- {bucket}")
    else:
        print("No publicly accessible S3 buckets found")

def iam_write_access():
    iam_client = boto3.client('iam')
    #response =
    print("Checking for IAM policies with Write access")

def iam_full_access():
    iam_client = boto3.client('iam')
    #response =
    print("Checking for IAM policies with full access")

def public_amis():
    ec2_client = boto3.client('ec2')
    #response =
    print("Checking for publicly accessible AMIs")

def security_groups_open_access():
    ec2_client = boto3.client('ec2')
    #response =
    print("Checking for Security Groups with open access")

def all_checks():
    public_s3_buckets()
    iam_write_access()
    iam_full_access()
    public_amis()
    security_groups_open_access()
    print("Performing all available checks")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basic Utility for Finding Faults (BUFF) in AWS")

    parser.add_argument("--public-s3", action="store_true", help="checks for publicly accessible S3 buckets")
    parser.add_argument("--iam-write", action="store_true", help="checks for IAM policies with Write access")
    parser.add_argument("--iam-full-access", action="store_true", help="checks for IAM policies with full access or administrator level access")
    parser.add_argument("--public-ami", action="store_true", help="checks for publicly accessible AMIs")
    parser.add_argument("--security-groups", action="store_true", help="checks for Security Groups with inbound rules with open access")
    parser.add_argument("--all", action="store_true", help="performs all available checks")

    args = parser.parse_args()

    if args.public_s3:
        try:
            public_s3_buckets()
        except NoCredentialsError:
            print("AWS credentials are not configured. Please run 'aws configure' to set them up.")
    elif args.iam_write:
        try:
            iam_write_access()
        except NoCredentialsError:
            print("AWS credentials are not configured. Please run 'aws configure' to set them up.")
    elif args.iam_full_access:
        try:
            iam_full_access()
        except NoCredentialsError:
            print("AWS credentials are not configured. Please run 'aws configure' to set them up.")
    elif args.public_ami:
        try:
            public_amis()
        except NoCredentialsError:
            print("AWS credentials are not configured. Please run 'aws configure' to set them up.")
    elif args.security_groups:
        try:
            security_groups_open_access()
        except NoCredentialsError:
            print("AWS credentials are not configured. Please run 'aws configure' to set them up.")
    elif args.all:
        try:
            all_checks()
        except NoCredentialsError:
            print("AWS credentials are not configured. Please run 'aws configure' to set them up.")
    else:
        print("Please provide a valid option. Use --help for available options")
