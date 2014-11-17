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
            return """
<!DOCTYPE HTML>
<html>
<head>

<title>Full Screen</title>

<meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=no">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="viewport" content="width=device-width" />
<link rel="stylesheet" href="style.css" />
<script src="jquery.js"></script>
<script src="script.js"></script>

</head>
<body>
<img src="background.png">
<img id='led1' src="green.png" onclick="javascript:test()">
<img id='led2' src="green.png" onclick="javascript:test()">
<img id='led3' src="green.png" onclick="javascript:test()">
<img id='led4' src="green.png" onclick="javascript:test()">
<img id='led5' src="green.png" onclick="javascript:test()">
<img id='led6' src="green.png" onclick="javascript:test()">
<img id='led7' src="green.png" onclick="javascript:test()">
<img id='led8' src="green.png" onclick="javascript:test()">
<img id='led9' src="green.png" onclick="javascript:test()">
<img id='led10' src="green.png" onclick="javascript:test()">
<img id='led11' src="green.png" onclick="javascript:test()">
<img id='led12' src="green.png" onclick="javascript:test()">
<img id='led13' src="green.png" onclick="javascript:test()">
<img id='led14' src="green.png" onclick="javascript:test()">
<img id='led15' src="green.png" onclick="javascript:test()">
<img id='led16' src="green.png" onclick="javascript:test()">
<div id="container">
	
	<div id="home-page">
		<div class="slide-content">
			<div class="content">
				<p>Control Cloud</p>
			</div>
			<div class="show-menu">
            </br></br>
                led_ahed1 : <i id="led1" >off</i></br></br>
                led2 : <i id="led2" >off</i></br></br>
                pot : <i id="pot" >55</i></br></br></br>
			</div>
		</div>
	</div>
	
</div>
</body>
</html> 

        """


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

        '/style.css':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/style.css'},

        '/jquery.js':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/jquery.js'},

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





