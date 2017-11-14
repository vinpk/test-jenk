#!/usr/bin/python

import yaml
import subprocess
import sys

if __name__ == '__main__':

   fsn = 0
   fsi = ""
   flist = subprocess.check_output("find $(pwd)",shell=True)

   for fi in flist.split("\n"):
      if fi.endswith(('.yml','.yaml')):
         try:
            fc = open(fi,'r')
            parse = yaml.load(fc)
         except:
#            print "Failed to parse ",fi
            fsn += 1
            fsi += fi + "\n"

   if fsn > 0:
      print "Failed to parse ",fsn," files and templates\nFailed files list:\n",fsi
      sys.exit(1)
