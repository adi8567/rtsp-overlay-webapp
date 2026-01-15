import subprocess

def convert_rtsp_to_hls(rtsp_url):
    output_path = "static/stream.m3u8"

    command = [
        "ffmpeg",
        "-i", rtsp_url,
        "-c:v", "copy",
        "-f", "hls",
        "-hls_time", "2",
        "-hls_list_size", "3",
        output_path
    ]

    subprocess.Popen(command)
    return output_path
