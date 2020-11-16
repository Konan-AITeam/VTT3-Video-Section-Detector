import os
import copy
import requests

import shutil import copy2, rmtree
import datetime import datetime
import JSONImport import *


class Cataloger:
  def __init__(self, db_data, url, s):
    self.db_data = db_data
    self.url = url
    self.s = s

  def cataloging(self):
    pass
  
  def cut_scene(self):
    FMT = '%H:%M:%S.%f'
    duration = datetime.strptime(end_time, FMT) - datetime.strptime(start_time, FMT)
    scene_path = save_path + ("/SCENE_%010d.mp4" % sceneid)

    # cmd = "ffmpeg -i {0} -ss {1} -c copy -t {2} {3}".format(video_path, start_time, duration, scene_path)
    # subprocess.call(cmd, shell=True)

    return scene_path
  
  def get_shot_info(self):
    cmd = "ffmpeg -i {0} -filter:v \"select='gt(scene,0.24)',showinfo\" -f null - 2> {1}".format(video_path, save_path + '/tmp.log')
    subprocess.call(cmd, shell=True)

    cmd2 = "grep showinfo {0} | grep pts_time:[0-9.]* -o | grep '[0-9]*\\.[0-9]*' -o > {1}".format(save_path + '/tmp.log', save_path + '/tmp.txt')
    subprocess.call(cmd2, shell=True)
  
  def get_video_info(self):
    f = open(save_path + "/tmp.log", "r")
    duration = ""
    fps = 0.0

    while True:
      line = f.readline()
      if not line: break

      if line.find("Duration: ") != -1:
        duration = line.replace(", ", "@").replace(": ", "@").split("@")[1]

      elif line.find(" fps,") != -1:
        t = line.split(" fps,")[0]
        fps = float(t[t.rfind(" ") + 1:])
        break
    f.close()

    return duration, fps
  
  def calcStep(self):
    return int(video_fps / fps)
  
  def my_round(self):
    x = num - int(num)

    if x >= 0.9:
      return int(num) + 1
    else:
      return int(num)
  
  def second_to_ms(self):
    return int(float(second) * 1000)
  
  def time_to_ms(self):
    times = time.split(":")

    return (((int(times[0]) * 60 * 60) + (int(times[1]) * 60) + int(times[2].split(";")[0])) * 1000) + int(int(times[2].split(";")[1]) / video_fps * 1000)
  
  def second_to_time(self):
    second = int(second)

    h = second // (60 * 60)
    m = (second // 60) % 60
    s = second % 60

    return "%02d:%02d:%02d" % (h, m, s)
  
  def extract_all(self):
    if not os.path.exists(save_path):
      os.makedirs(save_path)

    cmd = "ffmpeg -i {0} -ss 00:00:00.000 -qscale:v 2 {1}/IMAGE_%010d.jpg".format(video_path, save_path)
    subprocess.call(cmd, shell=True)
  
  def post_data(self):
    params = {"status": 1, "progress": number, "error_msg": "", "startFlag": "N", "req_fps": 0}
    response = self.s.post(url=self.url, data=params)
    if response.status_code != 200:
      print("ERROR : failed the post request about '%d' progress" % number)
