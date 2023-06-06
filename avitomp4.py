# �w�肵���t�H���_�����ċA�I�ɒT�����Aavi�t�@�C����mp4�ɕϊ�����X�N���v�g
import os
import subprocess

FFMPEG_BIN = "ffmpeg"

def convert_avi_to_mp4(avi_path):
    """
    ����avi_path�Ŏw�肳�ꂽavi�t�@�C����mp4�ɕϊ�����֐�
    """
    mp4_path = avi_path.replace(".avi", ".mp4")
    
    try:
        subprocess.call([FFMPEG_BIN, '-i', avi_path, mp4_path])
        os.remove(avi_path)
    except:
        print("Failed to convert avi to mp4.")
        print("avi_path: {}".format(avi_path))
        print("mp4_path: {}".format(mp4_path))
        print()
        
def convert_avi_to_mp4_recursive(folder_path):
    """
    ����folder_path�Ŏw�肳�ꂽ�t�H���_�����ċA�I�ɒT�����Aavi�t�@�C����mp4�ɕϊ�����֐�
    """
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        
        if os.path.isfile(file_path):
            if file_path.endswith(".avi"):
                convert_avi_to_mp4(file_path)
        else:
            convert_avi_to_mp4_recursive(file_path)
            
if __name__ == '__main__':
    PATH = "C:\Users\tanaka\Downloads\syozemi_dataset\presentation_processed"
    convert_avi_to_mp4_recursive(PATH)