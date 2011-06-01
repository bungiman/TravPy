#import travpy.web.write
#import travpy.gamedb

class TravianGame:

    def __init__(self,travianInterface):
        self.travIntf = travianInterface;
        self.__DB = TravianDB();

    def initialize(_self):
        travianInterface.initializeDB(_DB);
    
    def update():
        travianInterface.updateDB(self.__DB);
        
