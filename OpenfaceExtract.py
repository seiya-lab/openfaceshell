import os
import subprocess

INPUT_FOLDER = '/tmp/presentation'
OUTPUT_FOLDER = '/tmp/presentation_processed'
MAKE_CMD = '/home/openface-build/build/make'
OPENFACE_BIN = '/home/openface-build/build/bin/FeatureExtraction'
FFMPEG_BIN = 'ffmpeg'

def run_cmd(cmd):
    """
    コマンドを実行する関数
    """
    process = subprocess.Popen(cmd, shell=True)
    process.wait()

def feature_extract(video_path, output_dir):
    """
    引数video_pathの動画ファイルをOpenFaceで処理する関数
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    run_cmd(f"{OPENFACE_BIN} -f {video_path} -out_dir {output_dir}")

def convert_avi_to_mp4(avi_path, mp4_path):
    """
    引数avi_pathで指定されたaviファイルをmp4に変換する関数
    """
    run_cmd(f"{FFMPEG_BIN} -i {avi_path} -vcodec libx264 {mp4_path}")
    os.remove(avi_path)

def remove_files(file_paths):
    """
    引数file_pathsで指定されたファイルを削除する関数
    """
    for file_path in file_paths:
        os.remove(file_path)

if __name__ == '__main__':
    os.system(MAKE_CMD)
    
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        
    videoes = [os.path.join(INPUT_FOLDER, file) for file in os.listdir(INPUT_FOLDER) if not file.startswith('.')]
    
    total_videos = len(videoes)
    processed_videos = 0
    
    for video_path in videoes:
        video_name = os.path.splitext(os.path.basename(video_path))[0]
        output_dir = os.path.join(OUTPUT_FOLDER, f"{video_name}_FaceFeature")
        
        feature_extract(video_path, output_dir)
        
        avi_path = os.path.join(output_dir, f"{video_name}.avi")
        mp4_path = os.path.join(output_dir, f"{video_name}.mp4")
        
        convert_avi_to_mp4(avi_path, mp4_path)
        
        remove_files([os.path.join(output_dir, f"{video_name}.hog"), os.path.join(output_dir, f"{video_name}_aligned")])
        processed_videos += 1
        
        progress = (processed_videos / total_videos) * 100
        print(f"Processing video: {video_path}")
        print(f"Progress: {processed_videos}/{total_videos} ({progress:.2f}%)")
        print()

    print("Processing completed.")
