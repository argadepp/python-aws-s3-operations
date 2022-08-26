
import boto3

s3 = boto3.resource("s3", aws_access_key_id="AKIAQ5WOCCGHVW4W5LYN",aws_secret_access_key="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")


s3.Object("nodenscode","s3.py").delete()

