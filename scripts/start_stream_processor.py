import boto3
import time

rekognition = boto3.client('rekognition', region_name='us-east-1')

response = rekognition.start_stream_processor(
    Name='live-video-processor',
    StartSelector={
        'KVSStreamStartSelector': {
            'ProducerTimestamp': int(time.time() * 1000)  # Şu anki zaman (ms cinsinden)
        }
    },
    StopSelector={
        'MaxDurationInSeconds': 120
    }
)

print("✅ Stream processor başlatıldı:", response)
