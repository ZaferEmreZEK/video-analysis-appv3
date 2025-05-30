import boto3

region = "us-east-1"
kinesis_video_stream_arn = "arn:aws:kinesisvideo:us-east-1:779846804321:stream/live-video-stream/1748263064807"
role_arn = "arn:aws:iam::779846804321:role/RekognitionStreamProcessorRole"
stream_processor_name = "live-video-processor"
bucket_name = "rekognition-output-bucket33"
sns_topic_arn = "arn:aws:sns:us-east-1:779846804321:rekognition-events-topic"

rekognition = boto3.client('rekognition', region_name=region)

try:
    response = rekognition.create_stream_processor(
        Input={
            'KinesisVideoStream': {
                'Arn': kinesis_video_stream_arn
            }
        },
        Output={
            'S3Destination': {
                'Bucket': bucket_name
            }
        },
        Name=stream_processor_name,
        RoleArn=role_arn,
        Settings={
            'ConnectedHome': {
                'Labels': ['Person', 'Package', 'Pet'],
                'MinConfidence': 50.0
            }
        },
        NotificationChannel={
            'SNSTopicArn': sns_topic_arn
        },
        DataSharingPreference={
            'OptIn': True
        }
    )
    print("✅ Stream processor created successfully:")
    print(response)
except Exception as e:
    print("❌ Error creating stream processor:", e)
