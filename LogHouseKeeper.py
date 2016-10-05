#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# find ! -mtime -7  -type f

import yaml
import os

class LogHouseKeeper:

   def __init__(self, config_file):
      self.config_file = config_file
      self.config = ''

   def __enter__(self):
      with open(self.config_file, 'r') as stream:
         try:
            self.config = yaml.load(stream)
         except yaml.YAMLError as exc:
            print(exc)
      return self

   def __exit__(self, type, msg, traceback):
      if type:
         print(msg)
      return False

   def print_config(self):
      print(self.config)

   '''取得所有路徑'''
   def get_pathes(self, action):
      pathes = self.config['pathes']
      full_pathes = []
      for path in(pathes):
         if 'action' in path and 'parent' in path and 'child' in path:
            for child_path in(path['child']):
               full_pathes.append(path['parent'] + '/' + child_path)
      return full_pathes

   def do_action(self, file, action):
      pass

   def go(self):
      all_pathes = self.get_pathes('delete')
      for path in(all_pathes):
         print(path)
#               try:
#                  os.system('ls -l ' + full_path)
#                  i = i+1
#               except OSError:
#                  pass

if __name__ == '__main__':
   with LogHouseKeeper("config.yml") as keeper:
        keeper.go()
