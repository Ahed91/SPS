#!/usr/bin/env python
# encoding: utf-8

import sys
import cherrypy
import os.path
import sqlite3
import time
import json
from grequests import AsyncRequest

locations = {
    'A1': 'red',
    'A2': 'green',
    'A3': 'red',
    'A4': 'green',
    'B1': 'red',
    'B2': 'green',
    'B3': 'red',
    'B4': 'green',
    'C1': 'red',
    'C2': 'green',
    'C3': 'red',
    'C4': 'green',
    'D1': 'red',
    'D2': 'green',
    'D3': 'red',
    'D4': 'green',
    'E1': 'red',
    'E2': 'green',
    'E3': 'red',
    'E4': 'green',
    'F1': 'red',
    'F2': 'green',
    'F3': 'red',
    'F4': 'green',
}

class Root:
    @cherrypy.expose
    def index(self):
        """TODO: Docstring for index.
        :returns: TODO

        """
        return file('static/main.html')

    @cherrypy.expose
    def function(self, arg1):
        pass


current_dir = os.path.dirname(os.path.abspath(__file__))

conf = {'/':
             {'tools.staticfile.root': current_dir},

        '/main':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/main.html'},

        '/grid':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/grid.html'},

        '/sign':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/sign.html'},

        '/style.css':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/css/style.css'},

        '/css/sign.css':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/css/sign.css'},

        '/css/reset.css':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/css/reset.css'},

        '/jquery.min.js':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/js/jquery.min.js'},

        '/w2ui-1.4.2.min.js':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/js/w2ui-1.4.2.min.js'},

        '/w2ui-1.4.2.min.css':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/css/w2ui-1.4.2.min.css'},

        '/script.js':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/js/script.js'},

        '/js/main.js':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/js/main.js'},

        '/js/modernizr.js':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/js/modernizr.js'},

         '/background.png':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/img/background.png'},

         '/green.png':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/img/green.png'},

         '/red.png':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/img/red.png'},

         '/contact.png':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/img/contact.png'},

         '/img/cd-logo.svg':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/img/cd-logo.svg'},

         '/img/cd-icon-username.svg':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/img/cd-icon-username.svg'},

         '/img/cd-icon-password.svg':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/img/cd-icon-password.svg'},

         '/img/cd-icon-menu.svg':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/img/cd-icon-menu.svg'},

         '/img/cd-icon-email.svg':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/img/cd-icon-email.svg'},

         '/img/cd-icon-close.svg':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/img/cd-icon-close.svg'},

         'global':{
                'server.socket_port':8080,
                'tools.sessions.on': True
                }}
cherrypy.quickstart(Root(), '/',conf
    )

