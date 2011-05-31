#!/usr/bin/python
import cherrypy
import travpy
import travpy.interface
from travpy.setting import TravSetting;
import sys, os, os.path
#from TravPyWeb import 
#from TravPyConsole import *

#simple script to demo functionality of Village
def main():
    sys.path.append(os.path.join(os.getcwd(),'data/templates/'))
    settings = TravSetting();
    cherrypy.config.update(settings.getCherryPyConfig());
    mountPoint = '/';
    cherrypy.tree.mount(travpy.interface.MainPage(mountPoint),mountPoint,config=settings.getAppConfig());
    cherrypy.server.start();


    #travPy = TravPyConsole();
    #travianInterface = TravianWebInterface();
	#game = TravianGame(travianInterface);
	#game.initialize();
	# updateThread = Thread(game.update());
	# playThread = Thread(game.play());
	# updateThread.start();
	# playThread.start();
	# while (travPy.isRunning()):            
	# 	game.follow(travPy.getInstuctions));
	#	travPy.update(game.getDatabase());

if __name__ == "__main__":
	main()
