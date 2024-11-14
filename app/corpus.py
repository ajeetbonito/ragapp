import boto3
import os
from pathlib import Path
from dotenv import load_dotenv
import logging

load_dotenv()

# Load environment variables
DOCS_PATH = os.getenv("CORPUS_FOLDER")
AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")

# Initialize logging
logger = logging.getLogger(__name__)

class Corpus:
    def __init__(self):
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY"),
        )
        self.s3_bucket_name  = os.getenv("AWS_BUCKET_NAME")
        self.folder_path  = os.getenv("CORPUS_FOLDER")


    def fetch_pdfs_from_s3(self):
        """Download all PDFs from S3 and save them in the docs directory"""
        try:
            # Create the local docs directory if it doesn't exist
            if not os.path.exists(self.folder_path):
                os.makedirs(self.folder_path)

            # List all objects in the S3 bucket
            response = self.s3_client.list_objects_v2(Bucket=self.s3_bucket_name)
            if "Contents" in response:
                for obj in response["Contents"]:
                    key = obj["Key"]
                    if key.endswith(".pdf"):  # Only download PDFs
                        file_path = os.path.join(self.folder_path, key)
                        logger.info(f"Downloading {key} to {file_path}")
                        self.s3_client.download_file(self.s3_bucket_name, key, file_path)
            else:
                logger.info("No files found in the bucket.")
        except Exception as e:
            logger.error(f"Error fetching PDFs from S3: {e}")
            raise