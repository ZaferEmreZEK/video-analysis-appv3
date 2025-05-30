import boto3

rekognition = boto3.client('rekognition', region_name='us-east-1')

try:
    rekognition.delete_stream_processor(Name='live-video-processor')
    print("✅ Stream processor 'live-video-processor' deleted.")
except Exception as e:
    print("❌ Error deleting stream processor:", e)
