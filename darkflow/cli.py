from .defaults import argHandler #Import the default arguments
import os
from .net.build import TFNet
from picamera import PiCamera
import time

def cliHandler(args):
    FLAGS = argHandler()
    FLAGS.setDefaults()
    FLAGS.parseArgs(args)

    # make sure all necessary dirs exist
    def _get_dir(dirs):
        for d in dirs:
            this = os.path.abspath(os.path.join(os.path.curdir, d))
            if not os.path.exists(this): os.makedirs(this)
    
    requiredDirectories = [FLAGS.imgdir, FLAGS.binary, FLAGS.backup, os.path.join(FLAGS.imgdir,'out')]
    if FLAGS.summary:
        requiredDirectories.append(FLAGS.summary)

    _get_dir(requiredDirectories)

    # fix FLAGS.load to appropriate type
    try: FLAGS.load = int(FLAGS.load)
    except: pass

    tfnet = TFNet(FLAGS)
    
    if FLAGS.demo:
        tfnet.camera()
        exit('Demo stopped, exit.')

    if FLAGS.train:
        print('Enter training ...'); tfnet.train()
        if not FLAGS.savepb: 
            exit('Training finished, exit.')

    if FLAGS.savepb:
        print('Rebuild a constant version ...')
        tfnet.savepb(); exit('Done')
    tfnet.predict()
   # print('Taking picture')
    #with picamera.PiCamera() as camera:
     #   print("im inside")
      #  camera.resolution = (800,600)
       # print("set resolution")
        #camera.start_preview()
        #print("started sleep")
        #time.sleep(2)
        #print("ended slep")
       # os.chdir("/home/darkflow/sample_img/")
        #camera.capture("/home/darkflow/sample_img/a.jpg")
        #print("captured image")
        #camera.stop_preview()
       # os.chdir("/home/darkflow/darkflow/net")
    #print('Done MF')
    #camera=PiCamera()
    #camera.start_preview()
    #time.sleep(2)
    #os.chdir("/home/darkflow/sample_img/")
   # try:
    #    while True:
     #       camera.capture("/home/pi/darkflow/sample_img/a.jpg")
      #      camera.stop_preview()
       #     #os.chdir("/home/darkflow/darkflow/net")
         #   print("Done")
        #    tfnet.predict()
          #  os.remove("/home/pi/darkflow/sample_img/a.jpg")
  #  except KeyboardInterrupt:
   #     pass
   # camera.stop_preview()
