import os
from pathlib import Path
from ..aws import AWS


class S3:
    default_bucket: str = 'insta-watch'
    region: str = 'ap-northeast-2'
    s3 = AWS.session.resource('s3')

    # images/파일명 과 같이 main.py 의 실행 위치에 relative 합니다.
    @classmethod
    def save_file(cls, from_file: str, to_file: str, bucket: str = default_bucket):
        cls.s3.Bucket(bucket).upload_file(from_file, to_file)
        return f"https://{bucket}.s3.{cls.region}.amazonaws.com/{to_file}"

    @classmethod
    def download_bucket(cls, to_file: str, bucket: str = default_bucket):
        my_bucket = cls.s3.Bucket(bucket)
        for s3_object in my_bucket.objects.all():
            path, filename = os.path.split(s3_object.key)
            if filename == '':
                Path(to_file + s3_object.key).mkdir(parents=True, exist_ok=True)
            else:
                my_bucket.download_file(s3_object.key, to_file + s3_object.key)
