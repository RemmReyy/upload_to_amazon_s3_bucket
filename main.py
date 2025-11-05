import os
from pathlib import Path
import boto3
from dotenv import load_dotenv

# Get data from .env
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')  # за замовчуванням
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'files')

# Checking mandatory variables
required_vars = ['AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY', 'S3_BUCKET_NAME']
missing = [var for var in required_vars if not os.getenv(var)]
if missing:
    raise EnvironmentError(f"There are no variables in .env: {', '.join(missing)}")

# Create session with keys
session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

#S3
s3 = session.resource('s3')
bucket = s3.Bucket(S3_BUCKET_NAME)


def upload_objects():
    """Download local directory in S3"""
    if not Path(UPLOAD_FOLDER).exists():
        print(f"Directory {UPLOAD_FOLDER} not found!")
        return

    files = [f for f in Path(UPLOAD_FOLDER).iterdir() if f.is_file()]
    if not files:
        print(f"Dictionary {UPLOAD_FOLDER} is empty.")
        return

    print(f"Start downloading {len(files)} files in bucket {S3_BUCKET_NAME}...")

    for file_path in files:
        try:
            object_key = file_path.name  # ім'я файлу в S3
            print(f"  Downloading: {file_path.name} → s3://{S3_BUCKET_NAME}/{object_key}")
            bucket.upload_file(str(file_path), object_key)
        except Exception as e:
            print(f"  Error loading {file_path.name}: {e}")

    print("Download complete!")


if __name__ == '__main__':
    upload_objects()