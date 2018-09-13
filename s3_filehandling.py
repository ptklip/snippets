# -*- coding: utf-8 -*-
"""
Upload files to Amazon S3

"""
import os
from os import listdir
from os.path import isfile, join
import boto3

curdir = os.getcwd() # Get current directory
filesdir = 'files' # Files firectory
filepath = os.path.join(curdir, filesdir)
print('\nFilepath: ', filepath, '\n')

# Create list of files in the directory.
fileslist = [f for f in listdir(filepath) if isfile(join(filepath, f))]

# Print the list of files.
print('Found files:\n')
for f in fileslist:
    print(join(filepath, f))



# Set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
# as environemnt variables.

s3 = boto3.resource('s3')
bucket = 'pk-100-001-bucket-01'

# List all S3 buckets
# for bucket in s3.buckets.all():
#     print(bucket.name)

# Upload files to S3
print('\nUploading files to S3:\n')
for f in fileslist:
    print('Filename: ', join(filepath, f))
    s3.meta.client.upload_file(join(filepath, f), bucket, f)


