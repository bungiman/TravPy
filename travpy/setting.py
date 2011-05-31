import ConfigParser, os, os.path

class TravSetting:
    _settings_file = 'travpy.ini';
    def __init__(self):
        self._config = ConfigParser.ConfigParser();
        self._config.read(self._settings_file);
    def initialize(self):
        # Initializes the config file to default values
        self._config.add_section('TravPyWeb');
        self._config.set('TravPyWeb','socket_host','127.0.0.1')
        self._config.set('TravPyWeb','socket_port','8080')
        self._config.set('TravPyWeb','page_update','300')
        self._config.set('TravPyWeb','req_auth','0')
        self._config.set('TravPyWeb','user','')
        self._config.set('TravPyWeb','pass','')
        with open(self._settings_file, 'wb') as configfile:
            self._config.write(configfile);
    def dump(self):
        print self._config.sections();
    def getCherryPyConfig(self):
        cherryPyConf = dict();
        try:
            cherryPyConf['server.socket_host'] = self._config.get('TravPyWeb','socket_host');
            cherryPyConf['server.socket_port'] = self._config.getint('TravPyWeb','socket_port');
        except ConfigParser.NoSectionError:
            print "Did not automatically load data from " + self._settings_file + ", make sure the file is not corrupted.";
        return cherryPyConf;
        # if auth_req, deal with that shit
    def getAppConfig(self):
        conf = {'/favicon.ico':{
                    'tools.staticfile.on' : True,
                    'tools.staticfile.filename': os.path.join(os.getcwd(),'data/imgs/favicon.ico'),
                    }, 
                '/js':{
                    'tools.staticdir.on' : True,
                    'tools.staticdir.dir': os.path.join(os.getcwd(),'data/js/'),
                    'tools.staticdir.content_types': {
                        'js' : 'application/javascript'}
                    },
                '/css':{
                    'tools.staticdir.on' : True,
                    'tools.staticdir.dir': os.path.join(os.getcwd(),'data/css/'),
                    'tools.staticdir.content_types': {
                        'css' : 'text/css'}
                    }
                };
        return conf;
