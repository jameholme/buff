import argparse
import boto3
from botocore.exceptions import NoCredentialsError
from botocore.exceptions import ClientError

def public_s3_buckets():
    def check_block_public_access(bucket_name):
        s3_client = boto3.client('s3')
        try:
            response = s3_client.get_public_access_block(Bucket=bucket_name)
            if response['PublicAccessBlockConfiguration']['BlockPublicAcls'] or \
            response['PublicAccessBlockConfiguration']['IgnorePublicAcls'] or \
            response['PublicAccessBlockConfiguration']['BlockPublicPolicy'] or \
            response['PublicAccessBlockConfiguration']['RestrictPublicBuckets']:
                pass
            else:
                print(f"*~~> {bucket_name}")
        except ClientError as e:
            print(f"An error occurred while checking Block Public Access for {bucket_name}: {e}")
    def list_public_buckets():
        s3_client = boto3.client('s3')
        response = s3_client.list_buckets()
        bucket_names = [bucket['Name'] for bucket in response['Buckets']]
        print("S3 buckets with public access:")
        for bucket_name in bucket_names:
            check_block_public_access(bucket_name)
    list_public_buckets()

def iam_write_access():
    def gather_iam_groups():
        def list_groups():
            iam_client = boto3.client('iam')
            response = iam_client.list_groups()
            group_names = [group['GroupName'] for group in response['Groups']]
            return group_names

        def check_write_access_policies(group_name, iam_client):
            response = iam_client.list_attached_group_policies(GroupName=group_name)
            for attached_policy in response.get('AttachedPolicies', []):
                policy_arn = attached_policy['PolicyArn']
                policy_response = iam_client.get_policy(PolicyArn=policy_arn)
                policy_document = get_policy_document(iam_client, policy_arn)
                if has_write_access_permissions(policy_document):
                    print(f"*~~> '{group_name}': {policy_arn}")

        def get_policy_document(iam_client, policy_arn):
            policy_response = iam_client.get_policy(PolicyArn=policy_arn)
            if 'DefaultVersionId' in policy_response['Policy']:
                version_id = policy_response['Policy']['DefaultVersionId']
                version_response = iam_client.get_policy_version(PolicyArn=policy_arn, VersionId=version_id)
                return version_response['PolicyVersion']['Document']
            elif 'Policy' in policy_response:
                return policy_response['Policy']['Document']
            else:
                raise ValueError("Unsupported response structure for get_policy")

        def has_write_access_permissions(policy_document):
            for statement in policy_document.get('Statement', []):
                if 'Action' in statement and any('Write' in action for action in statement['Action']):
                    return True

            return False

        def check_iam_groups():
            iam_client = boto3.client('iam')
            group_names = list_groups()
            for group_name in group_names:
                check_write_access_policies(group_name, iam_client)
        check_iam_groups()
    print("Groups with Write Access:")
    gather_iam_groups()

    def gather_iam_users():

        def list_users():
            iam_client = boto3.client('iam')
            response = iam_client.list_users()
            user_names = [user['UserName'] for user in response['Users']]
            return user_names

        def check_write_access_policies(user_name, iam_client):
            response = iam_client.list_attached_user_policies(UserName=user_name)
            for attached_policy in response.get('AttachedPolicies', []):
                policy_arn = attached_policy['PolicyArn']
                policy_response = iam_client.get_policy(PolicyArn=policy_arn)
                policy_document = get_policy_document(iam_client, policy_arn)
                if has_write_access_permissions(policy_document):
                    print(f"*~~> '{user_name}': {policy_arn}")
                else:
                    pass

        def get_policy_document(iam_client, policy_arn):
            policy_response = iam_client.get_policy(PolicyArn=policy_arn)
            if 'DefaultVersionId' in policy_response['Policy']:
                version_id = policy_response['Policy']['DefaultVersionId']
                version_response = iam_client.get_policy_version(PolicyArn=policy_arn, VersionId=version_id)
                return version_response['PolicyVersion']['Document']
            elif 'Policy' in policy_response:
                return policy_response['Policy']['Document']
            else:
                raise ValueError("Unsupported response structure for get_policy")

        def has_write_access_permissions(policy_document):
            for statement in policy_document.get('Statement', []):
                if 'Action' in statement and any('Write' in action for action in statement['Action']):
                    return True
            return False

        def check_iam_users():
            iam_client = boto3.client('iam')
            user_names = list_users()
            for user_name in user_names:
                check_write_access_policies(user_name, iam_client)
        check_iam_users()
    print("Users with Write Access:")
    gather_iam_users()

def iam_full_access():
    iam_client = boto3.client('iam')
    #response =
    print("IAM policies with full access:")

def public_amis():
    ec2_client = boto3.client('ec2')
    #response =
    print("Publicly accessible AMIs:")


def security_groups_open_access():
    ec2_client = boto3.client('ec2')
    #response =
    print("Security Groups with open access:")

def all_checks():
    print("===================================")
    public_s3_buckets()
    print("===================================")
    iam_write_access()
    print("===================================")
    iam_full_access()
    print("===================================")
    public_amis()
    print("===================================")
    security_groups_open_access()
    print("===================================")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basic Utility for Finding Faults (BUFF) in AWS")

    parser.add_argument("--public-s3", action="store_true", help="checks for publicly accessible S3 buckets")
    parser.add_argument("--iam-write-access", action="store_true", help="checks for groups and users with with write access")
    parser.add_argument("--iam-full-access", action="store_true", help="checks for groups and users with full access")
    parser.add_argument("--public-ami", action="store_true", help="checks for publicly accessible AMIs")
    parser.add_argument("--security-groups", action="store_true", help="checks for Security Groups with inbound rules with open access")
    parser.add_argument("--all", action="store_true", help="performs all available checks")

    args = parser.parse_args()

    if args.public_s3:
        try:
            public_s3_buckets()
        except NoCredentialsError:
            print("AWS credentials are not configured. Please run 'aws configure' to set them up.")
    elif args.iam_write_access:
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
