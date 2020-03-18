# -*- coding: utf-8 -*-
"""Classes for S3 Buckets."""

import mimetypes
from pathlib import Path


class BucketManager:
    """Manage an S3 Bucket."""

    def __init__(self, session):
        """Create a BucketManager object."""
        self.s3 = session.resource('s3')

    def all_buckets(self):
        """Get an iterator for all buckets."""
        return self.s3.buckets.all()

    def all_objects(self, bucket):
        """Get an iterator for all objects in bucket."""
        return self.s3.Bucket(bucket).objects.all()

    def init_bucket(self, bucket_name):
        """Initialize the bucket."""
        return self.s3.create_bucket(Bucket=bucket_name)

    def set_policy(self, bucket):
        """Set bucket policy to be readable by everyone."""
        policy = """
        {
            "Version":"2012-10-17",
            "Statement":[{
            "Sid":"PublicReadForGetBucketObjects",
            "Effect":"Allow",
            "Principal": "*",
                "Action":["s3:GetObject"],
                "Resource":["arn:aws:s3:::%s/*"
                ]
            }
        ]}
        """ % bucket.name
        policy = policy.strip()

        pol = bucket.Policy()
        pol.put(Policy=policy)

    def configure_website(self, bucket):
        """Configure site."""
        bucket.Website().put(WebsiteConfiguration={
            'ErrorDocument': {
                'Key': 'error.html'
            },
            'IndexDocument': {
                'Suffix': 'index.html'
            }
        })

    @staticmethod
    def upload_file(bucket, path, key):
        """Upload path to s3 bucket at key."""
        content_type = mimetypes.guess_type(key)[0] or 'text/plain'

        return bucket.upload_file(
            path,
            key,
            ExtraArgs={
                'ContentType': content_type
            })

    def sync(self, pathname, bucket_name):
        """Syncronization of the file tree."""
        bucket = self.s3.Bucket(bucket_name)
        root = Path(pathname).expanduser().resolve()

        def handle_directory(target):
            for path in target.iterdir():
                if path.is_dir():
                    handle_directory(path)
                if path.is_file():
                    self.upload_file(bucket, str(path),
                                     str(path.relative_to(root)))
        handle_directory(root)
