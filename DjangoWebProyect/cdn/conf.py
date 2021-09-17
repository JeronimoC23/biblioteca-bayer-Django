import os

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME= os.getenv('AWS_BUCKET_NAME')
AWS_STORAGE_BUCKET_NAME = "bayermedia"
AWS_S3_ENDPOINT_URL = 'https://nyc3.digitaloceanspaces.com'
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",

}
AWS_LOCATION = "https://bayermedia.nyc3.digitaloceanspaces.com"

DEFAULT_FILE_STORAGE = 'DjangoWebProyect.cdn.backends.MediaRootS3Boto3Storage'
