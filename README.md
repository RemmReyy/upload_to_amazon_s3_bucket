# upload_to_amazon_s3_bucket

Simple Python script to upload files or directories to an Amazon S3 bucket using `boto3`.

## Features
- Upload single files or entire directories
- Supports AWS credentials via config, env, or IAM roles
- Optional progress bar (`tqdm`)
- Lightweight & easy to extend

## Requirements
- Python 3.7+
- `boto3`: `pip install boto3`
- AWS credentials with `s3:PutObject` permission
- (Optional) `tqdm`: `pip install tqdm`

---

License
MIT © RemmReyy

