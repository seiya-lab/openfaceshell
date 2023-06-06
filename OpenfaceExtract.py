# -*- coding: utf-8 -*-
import os
import subprocess

# docker command
# docker run -it -v "C:\Users\tanaka\Develop\openfaceshell\":/src -v "C:\Users\tanaka\Downloads\angle_test":/dataset --rm algebr/openface:latest
INPUT_FOLDER = '/dataset/angle_test'
OUTPUT_FOLDER = '/dataset/angle_test_processed'
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
        
    subprocess.call([OPENFACE_BIN, '-f', video_path, '-out_dir', output_dir])

def convert_avi_to_mp4(avi_path, mp4_path):
    """
    引数avi_pathで指定されたaviファイルをmp4に変換する関数
    """
    try:
        subprocess.call([FFMPEG_BIN, '-i', avi_path, mp4_path])
        os.remove(avi_path)
    except:
        print("Failed to convert avi to mp4.")
        print("avi_path: {}".format(avi_path))
        print("mp4_path: {}".format(mp4_path))
        print()

def remove_files(file_paths):
    """
    引数file_pathsで指定されたファイル,ディレクトリを削除する関数
    """
    for file_path in file_paths:
        if os.path.exists(file_path):
            if os.path.isfile(file_path):
                os.remove(file_path)
            else:
                # ディレクトリの場合、中身を削除してからディレクトリを削除する
                for file in os.listdir(file_path):
                    os.remove(os.path.join(file_path, file))
                os.rmdir(file_path)

if __name__ == '__main__':
    os.system(MAKE_CMD)
    
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        
    videoes = [os.path.join(INPUT_FOLDER, file) for file in os.listdir(INPUT_FOLDER) if not file.startswith('.')]
    
    total_videos = len(videoes)
    processed_videos = 0
    
    for video_path in videoes:
        video_name = os.path.splitext(os.path.basename(video_path))[0]
        output_dir = os.path.join(OUTPUT_FOLDER, "{}_FaceFeature".format(video_name))
        
        feature_extract(video_path, output_dir)
        
        avi_path = os.path.join(output_dir, "{}.avi".format(video_name))
        mp4_path = os.path.join(output_dir, "{}.mp4".format(video_name))
        
        convert_avi_to_mp4(avi_path, mp4_path)
        
        remove_files([os.path.join(output_dir, "{}.hog".format(video_name)), os.path.join(output_dir, "{}_aligned".format(video_name))])
        processed_videos += 1
        
        progress = (processed_videos / total_videos) * 100
        print("Processing video: {}".format(video_name))
        print("Progress: {}/{} ({:.2f}%)".format(processed_videos, total_videos, progress))
        print()

    print("Processing completed.")
