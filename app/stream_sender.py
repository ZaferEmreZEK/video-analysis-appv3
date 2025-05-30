import subprocess
import cv2

# FFmpeg komutu
FFMPEG_BIN = "ffmpeg"
kinesis_stream_name = "live-video-stream"
aws_region = "us-east-1"

def send_video_to_kinesis():
    cap = cv2.VideoCapture(0)  # Webcam

    if not cap.isOpened():
        print("Kamera açılamadı.")
        return

    # FFmpeg subprocess
    ffmpeg_cmd = [
        FFMPEG_BIN,
        '-f', 'rawvideo',
        '-pix_fmt', 'bgr24',
        '-s', '640x480',
        '-r', '25',
        '-i', '-',
        '-f', 'lavfi',
        '-i', 'anullsrc',
        '-acodec', 'aac',
        '-vcodec', 'libx264',
        '-preset', 'ultrafast',
        '-tune', 'zerolatency',
        '-f', 'flv',
        f"https://kinesisvideo.{aws_region}.amazonaws.com/putMedia?StreamName={kinesis_stream_name}"
    ]

    process = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            process.stdin.write(frame.tobytes())
    except KeyboardInterrupt:
        print("Durduruldu.")
    finally:
        cap.release()
        process.stdin.close()
        process.wait()

if __name__ == "__main__":
    send_video_to_kinesis()
