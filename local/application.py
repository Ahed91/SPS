import sys
import cherrypy
import os.path

states = {
    'LED1': 'Off',
    'LED2': 'On',
    'POT' : 0
}

class States:

    exposed = True

    def GET(self, id=None):
    
        if id == None:
            raise cherrypy.HTTPRedirect('/api/states/index.html')


        elif id in states:
            return('%s' % (states[id]))
        else:
            return('The %s is not defined ' % id)

    def PUT(self, led1=None, led2=None, pot=None):
        states['LED1'] = led1 or states['LED1']
        states['LED2'] = led2 or states['LED2']
        states['POT'] = pot or states['POT']
        return led1 or led2 or pot

current_dir = os.path.dirname(os.path.abspath(__file__))

conf = {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.staticfile.root': current_dir },

        '/index.html':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/index.html'},

        '/style.css':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/style.css'},

        '/jquery.js':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/jquery.js'},

        '/jquery-ui.min.js':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/jquery-ui.min.js'},

        '/script.js':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/script.js'},
            
         '/background.png':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/background.png'},

         '/green.png':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/green.png'},

         '/red.png':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/red.png'},

         'global':{
                'server.socket_port':8080
                }}
cherrypy.quickstart(States(), '/api/states',conf                
    )





