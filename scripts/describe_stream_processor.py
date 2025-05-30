import boto3
from pprint import pprint

rekognition = boto3.client('rekognition', region_name='us-east-1')

response = rekognition.describe_stream_processor(Name='live-video-processor')

print(f"Status: {response['Status']}")
print("------")
for key in response:
    print(f"{key}:")
    pprint(response[key])
