# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAuomation')
session = boto3.Session(profile_name='pythonAutomation')
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
s3 = session.resource('s3')
bucket = s3.create_bucket(Bucket='robinvideolyzervideos')
bucket = s3.create_bucket(Bucket='alvaroideolyzervideos')
bucket = s3.create_bucket(Bucket='alvaroideolyzervideos')
bucket = s3.create_bucket(Bucket='alvaroideolyzervideos')
from pathlib import Path
get_ipython().run_line_magic('ls', '/Users/Alvaro Santoma/')
get_ipython().run_line_magic('ls', '"/Users/Alvaro Santoma"')
get_ipython().run_line_magic('ls', '"/Users/Alvaro Santoma/Downloads/*.mp4"')
get_ipython().run_line_magic('ls', '"/Users/Alvaro Santoma/Downloads/"')
get_ipython().run_line_magic('ls', '"/Users/Alvaro Santoma/Downloads/*.mp4"')
get_ipython().run_line_magic('ls', '"/Users/Alvaro Santoma/Downloads/video.mp4"')
pathname="/Users/Alvaro Santoma/Downloads/video.mp4"
path = Path(pathname).expanduser().resolve()
print(path)
bucket.upload_file(str(path), str(path.name))
rekognition_client = session.client('rekognition')
response = rekognition_client.start_label_detection(Video={'S3Object': {'Bucket': bucket.name, 'Name': path.name)
response = rekognition_client.start_label_detection(Video={'S3Object': {'Bucket': bucket.name, 'Name': path.name}})
response
