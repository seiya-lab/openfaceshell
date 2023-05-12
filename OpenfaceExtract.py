# -*- coding: utf-8 -*-
#OpenFace?øΩ?øΩp?øΩ?øΩ?øΩƒÉr?øΩf?øΩI?øΩf?øΩ[?øΩ^?øΩ?øΩ?øΩ?øΩ?øΩ?øΩ?øΩ?øΩ Çíäèo?øΩ?øΩ?øΩ?øΩ
import glob
import os
import subprocess
import time

default_path = '/tmp/loggerstation_syozemi_processed'
# default_path = './loggerstation'
# users = ['OMU-122','omu-123','OMU-124','OMU-125','omu126','OMU-127','OMU-128','OMU-129','OMU-130','OMU-131']
# users = ['s2022-3','s2022-4','s2022-5','s2022-7','s2022-8','s202211','s2022-13','sa2022-15','s2022-15','s2022-16']
# users = ['s2022-15', 's2022-16']
users = ['s2022-1', 's2022-2', 's2022-6', 's2022-9', 's2022-10', 's2022-12', 's2022-14', 's2022-17']
############################################################################
make_cmd = '/home/openface-build/build/make'
# print(make_cmd)
os.system(make_cmd)

total_loop = 0
for user in users:
    total_loop += len(os.listdir(default_path + '/' + user))

now_loop = 0
start = time.time()
for user in users:
    user_loop_record = 0
    date_dirs = os.listdir(default_path + '/' + user)
    for date_dir in date_dirs:
        user_loop_record += 1
        now_loop += 1
        video_path = os.path.join(default_path, user, date_dir, 'camera_raw.mp4') 
        out_path = os.path.join(default_path, user, date_dir)
        # out_path2 = os.path.join(default_path, 'syozemi_give', user)
        
        run_cmd = "/home/openface-build/build/bin/FeatureExtraction -f " + video_path + " -out_dir " + out_path + "/FaceFeature"
        # ffmpeg_cmd = 'ffmpeg -i ' + os.path.join(out_path, 'camera_raw.avi') + ' ' + os.path.join(out_path, 'openface.mp4')
        rm_avi_cmd = 'rm ' + os.path.join(out_path, 'FaceFeature', 'camera_raw.avi')
        rm_hog_cmd = 'rm ' + os.path.join(out_path, 'FaceFeature', 'camera_raw.hog')
        rm_bmp_cmd = 'rm -rf ' + os.path.join(out_path, 'FaceFeature', 'camera_raw_aligned')
        
        
        # print(run_cmd)
        print('#########################################')
        print('user:', user)
        print('path:', video_path)
        print('loop: {}/{}, {}%'.format(now_loop, total_loop, float(now_loop)*100/total_loop))
        now_time = time.time()-start
        print('now time:', now_time)
        print('remaining time:', now_time*float(total_loop)/(now_loop-0.99)-now_time)
        print('#########################################')
        print()
        
        os.system(run_cmd)
        if user_loop_record != 6:
            os.system(rm_avi_cmd)
            os.system(rm_hog_cmd)
            os.system(rm_bmp_cmd)
            print('Deleted!')
        else:
            pass