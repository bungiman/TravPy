import cherrypy
import travpy
from Cheetah.Template import Template

class MainPage:
    def __init__(self,root):
        self.__root = root;

    @cherrypy.expose
    def index(self):
        template = Template(file="data/templates/main.tmpl", searchList=[{'body':'test'}]);
        return template.respond();

    @cherrypy.expose
    def createDatabase(self):
        travpy.pretendAction();
        template = Template(file="data/templates/main.tmpl", searchList=[{'body':'test2'}]);
        return template.respond();

    @cherrypy.expose
    def updateTest(self):
        body = travpy.updateGameDB();
        template = Template(file="data/templates/main.tmpl", searchList=[{'body':body}]);
        return template.respond(); 
