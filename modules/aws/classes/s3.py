from ..aws import AWS


class S3:
    default_bucket: str = 'insta-watch'
    region: str = 'ap-northeast-2'

    # images/파일명 과 같이 main.py 의 실행 위치에 relative 합니다.
    @classmethod
    def save_file(cls, from_file: str, to_file: str, bucket: str = default_bucket):
        s3 = AWS.session.resource('s3')
        s3.Bucket(bucket).upload_file(from_file, to_file)
        return f"https://{bucket}.s3.{cls.region}.amazonaws.com/{to_file}"
