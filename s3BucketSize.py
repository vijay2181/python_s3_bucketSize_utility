import argparse
import sys
import boto3
import os
parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-a','--all', nargs='?', const='all', type=str, help='provide all option to get all buckets sizes')  #setting default value('all') to argument all
parser.add_argument('-b','--bucket', help='provide single bucket name to get single bucket size')
args = vars(parser.parse_args())

session = boto3.Session(region_name='us-west-2', profile_name='default')
s3client = session.client('s3')
allbuckets = s3client.list_buckets()

if args['all']=='all':
    print("all buckets")
    print("*"*60)
    for bucket in allbuckets['Buckets']:
        lst=list(bucket.values())
        print("bucket --",lst[0])
        os.system('''aws s3 ls --summarize --human-readable --recursive s3://'''+ lst[0] +''' | grep "Total" ''')
        print("*"*60)
else:
    if args['bucket']!=None:
        bucket=args['bucket']
        print("single bucket")
        os.system('''aws s3 ls --summarize --human-readable --recursive s3://'''+ bucket +''' | grep "Total" ''')
        sys.exit()
    else:
        pass
    print("pls dont provide any arguments with -a option, except all option")