#!/usr/bin/env python
# encoding: utf-8

import sys
import cherrypy
import os.path
import sqlite3
import time

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
}

class Root:

    exposed = True

    def GET(self, id=None, *pargs):

        if id == None:
            raise cherrypy.HTTPRedirect('/index')

        elif id in locations:
            return('%s' % (locations[id]))

        elif id == 'createdb':
            # Get a cursor 
            db = sqlite3.connect('data.db')
            cursor = db.cursor()
            cursor.execute('''
                       CREATE TABLE IF NOT EXISTS reserve(id INTEGER PRIMARY KEY, username TEXT,location TEXT,
                                            date TEXT, timefrom TEXT, timeto TEXT , note TEXT)   
                           ''')
            db.commit()
            
            cursor.execute('''
                       CREATE TABLE IF NOT EXISTS contact(id INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT,
                                            email TEXT, body TEXT)   
                           ''')
            db.commit()
            db.close()
            return 'Database Created'

        if not os.path.exists('data.db'):
            self.GET(id='createdb')

        elif id == 'contact':
            first_name = pargs[0]
            last_name = pargs[1]
            email = pargs[2]
            message = pargs[3]
            db = sqlite3.connect('data.db')
            cursor = db.cursor()
            cursor.execute('''INSERT INTO contact(firstname, lastname, email, body)
                                         VALUES(?,?,?,?)''', (first_name, last_name, email, message))
            db.commit()
            db.close()
            id = cursor.lastrowid
            print('contact inserted', id)
            return 'Thanks for your interest'

        elif id == 'reserve':
            username = pargs[0]
            location = pargs[1]
            date = pargs[2]
            timefrom = pargs[3]
            timeto = pargs[4]
            note = pargs[5]
            if int(timefrom.split(':')[0]) > int(timeto.split(':')[0]):
                return 'Error Time Interval (timefrom hour > timeto hour)'
            if int(timefrom.split(':')[0]) == int(timeto.split(':')[0]):
                if int(timefrom.split(':')[1]) >= int(timeto.split(':')[1]):
                    return 'Error Time Interval (timefrom min > timeto min)'
            # Connect to database
            db = sqlite3.connect('data.db')
            cursor = db.cursor()
            cursor.execute('''SELECT * FROM reserve where date=?''',(date,) )
            for i in cursor.fetchall():
                if location == i[2]:
                    if int(timefrom.split(':')[0]) == int(i[4].split(':')[0]):
                        if int(timefrom.split(':')[1]) == int(i[4].split(':')[1]):
                            return 'Choose another time or location(1timefrom equel old timrfrom)'
                        if int(timefrom.split(':')[1]) > int(i[4].split(':')[1]):
                            if int(timefrom.split(':')[0]) == int(i[5].split(':')[0]):
                                if int(timefrom.split(':')[1]) < int(i[5].split(':')[1]):
                                    return 'Choose another time or location(1timefrom min less than old timeto)'
                            if int(timefrom.split(':')[0]) < int(i[5].split(':')[0]):
                                return 'Choose another time or location(1timefrom hour less than old timeto)'
                        if int(timefrom.split(':')[1]) < int(i[4].split(':')[1]):
                            if int(timeto.split(':')[0]) == int(i[4].split(':')[0]):
                                if int(timeto.split(':')[1]) > int(i[4].split(':')[1]):
                                    return 'Choose another time or location(1timeto min more than old timeto)'
                            if int(timeto.split(':')[0]) > int(i[4].split(':')[0]):
                                return 'Choose another time or location(1timeto hour more than old timeto)'
                    if int(timefrom.split(':')[0]) < int(i[4].split(':')[0]):
                        if int(timeto.split(':')[0]) > int(i[4].split(':')[0]):
                            return 'Choose another time or location(2timeto hour more than old timefrom)'
                        if int(timeto.split(':')[0]) == int(i[4].split(':')[0]):
                            if int(timeto.split(':')[1]) > int(i[4].split(':')[1]):
                                return 'Choose another time or location(2timeto min more than old timefrom)'
                    if int(timefrom.split(':')[0]) > int(i[4].split(':')[0]):
                        if int(timefrom.split(':')[0]) < int(i[5].split(':')[0]):
                            return 'Choose another time or location(3timefrom hour less than old timeto)'
                        if int(timefrom.split(':')[0]) == int(i[5].split(':')[0]):
                            if int(timefrom.split(':')[1]) < int(i[5].split(':')[1]):
                                return 'Choose another time or location(3timefrom min less than old timeto)'

            cursor.execute('''INSERT INTO reserve(username, location, date, timefrom, timeto, note)
                                             VALUES(?,?,?,?,?,?)''', (username, location, date, timefrom, timeto, note))
            db.commit()
            db.close()
            id = cursor.lastrowid
            print('reserve inserted', id)
            return 'Done'

        if id == 'getallfromdb':
            db = sqlite3.connect('data.db')
            cursor = db.cursor()
            cursor.execute('SELECT * FROM reserve')
            l = []
            for _ in cursor.fetchall():
                l.append(_)
            db.close()
            return str(l).strip('[]').replace('),','),</br>')

        if id == 'gettodayfromdb':
            current_date=time.strftime('%d.%m.%Y')
            if current_date[0]=='0':
                current_date = current_date[1:]
            db = sqlite3.connect('data.db')
            cursor = db.cursor()
            cursor.execute('SELECT * FROM reserve where date=?',(current_date,))
            l = []
            for _ in cursor.fetchall():
                l.append(_)
            db.close()
            return str(l).strip('[]').replace('),','),</br>')

        if id == 'getcurrentfromdb':
            current_date=time.strftime('%d.%m.%Y')
            if current_date[0]=='0':
                current_date = current_date[1:]
            l=[]
            db = sqlite3.connect('data.db')
            cursor = db.cursor()
            cursor.execute('SELECT * FROM reserve where date=?',(current_date,))
            for _ in cursor.fetchall():
                l.append(_)
            db.close()
            print l
            current_min = int(time.strftime('%M'))
            current_hour = int(time.strftime('%H'))
            close_min = 59
            close_hour = 23
            index = -1
            index2 = -2
            if len(l):
                for idx,item in enumerate(l):
                    if int(item[4].split(':')[0]) == current_hour:
                        index2 = -2
                        if int(item[4].split(':')[1]) >= current_min and  int(item[4].split(':')[1]) < close_min :
                            close_min = int(item[4].split(':')[1])
                            index = idx
                if index2 == -1 :
                    for idx2,item2 in enumerate(l):
                        if int(item[4].split(':')[0]) > current_hour  and int(item[4].split(':')[0]) < close_hour :
                            close_hour = int(item[4].split(':')[0])
                            index2 = idx2
                    if int(item[4].split(':')[0]) == close_hour :
                        if int(item[4].split(':')[1]) < close_min :
                            close_min = int(item[4].split(':')[1])
                            index = idx
                return str(l[index])
            return ''

        if id == 'timefrom':
            current_date=time.strftime('%d.%m.%Y')
            if current_date[0]=='0':
                current_date = current_date[1:]
            l=[]
            db = sqlite3.connect('data.db')
            cursor = db.cursor()
            cursor.execute('SELECT * FROM reserve where date=? and location=?',(current_date,pargs[0]))
            for _ in cursor.fetchall():
                l.append(_)
            db.close()
            print l
            current_min = int(time.strftime('%M'))
            current_hour = int(time.strftime('%H'))
            close_min = 59
            close_hour = 23
            index = -1
            index2 = -2
            if len(l):
                for idx,item in enumerate(l):
                    if int(item[4].split(':')[0]) == current_hour:
                        index2 = -2
                        if int(item[4].split(':')[1]) >= current_min and  int(item[4].split(':')[1]) < close_min :
                            close_min = int(item[4].split(':')[1])
                            index = idx
                if index2 == -1 :
                    for idx2,item2 in enumerate(l):
                        if int(item[4].split(':')[0]) > current_hour  and int(item[4].split(':')[0]) < close_hour :
                            close_hour = int(item[4].split(':')[0])
                            index2 = idx2
                    if int(item[4].split(':')[0]) == close_hour :
                        if int(item[4].split(':')[1]) < close_min :
                            close_min = int(item[4].split(':')[1])
                            index = idx
            if  int(l[index][3].split('.')[0])< 10:
                if  int(l[index][3].split('.')[1])< 10:
                    if int(l[index][4].split(':')[0]) < 10:
                        return '0', l[index][3].split('.')[0], '/0', l[index][3].split('.')[1], '/', l[index][3].split('.')[2][2:] ,' 0', l[index][4]
                    else: 
                        return '0', l[index][3].split('.')[0], '/0', l[index][3].split('.')[1], '/', l[index][3].split('.')[2][2:] ,' ', l[index][4]
                else:
                    if int(l[index][4].split(':')[0]) < 10:
                        return '0', l[index][3].split('.')[0], '/', l[index][3].split('.')[1], '/', l[index][3].split('.')[2][2:] ,' 0', l[index][4]
                    else: 
                        return '0', l[index][3].split('.')[0], '/', l[index][3].split('.')[1], '/', l[index][3].split('.')[2][2:] ,' ', l[index][4]
            else:
                if  int(l[index][3].split('.')[1])< 10:
                    if int(l[index][4].split(':')[0]) < 10:
                        return '', l[index][3].split('.')[0], '/0', l[index][3].split('.')[1], '/', l[index][3].split('.')[2][2:] ,' 0', l[index][4]
                    else: 
                        return '', l[index][3].split('.')[0], '/0', l[index][3].split('.')[1], '/', l[index][3].split('.')[2][2:] ,' ', l[index][4]
                else:
                    if int(l[index][4].split(':')[0]) < 10:
                        return '', l[index][3].split('.')[0], '/', l[index][3].split('.')[1], '/', l[index][3].split('.')[2][2:] ,' 0', l[index][4]
                    else: 
                        return '', l[index][3].split('.')[0], '/', l[index][3].split('.')[1], '/', l[index][3].split('.')[2][2:] ,' ', l[index][4]
            return ''

        if id == 'timeto':
            current_date=time.strftime('%d.%m.%Y')
            if current_date[0]=='0':
                current_date = current_date[1:]
            l=[]
            db = sqlite3.connect('data.db')
            cursor = db.cursor()
            cursor.execute('SELECT * FROM reserve where date=? and location=?',(current_date, pargs[0]))
            for _ in cursor.fetchall():
                l.append(_)
            db.close()
            print l
            current_min = int(time.strftime('%M'))
            current_hour = int(time.strftime('%H'))
            close_min = 59
            close_hour = 23
            index = -1
            index2 = -2
            if len(l):
                for idx,item in enumerate(l):
                    if int(item[4].split(':')[0]) == current_hour:
                        index2 = -2
                        if int(item[4].split(':')[1]) >= current_min and  int(item[4].split(':')[1]) < close_min :
                            close_min = int(item[4].split(':')[1])
                            index = idx
                if index2 == -1 :
                    for idx2,item2 in enumerate(l):
                        if int(item[4].split(':')[0]) > current_hour  and int(item[4].split(':')[0]) < close_hour :
                            close_hour = int(item[4].split(':')[0])
                            index2 = idx2
                    if int(item[4].split(':')[0]) == close_hour :
                        if int(item[4].split(':')[1]) < close_min :
                            close_min = int(item[4].split(':')[1])
                            index = idx
                if  int(l[index][3].split('.')[0])< 10:
                    if  int(l[index][3].split('.')[1])< 10:
                        if int(l[index][5].split(':')[0]) < 10:
                            return '0', l[index][3].split('.')[0], '/0', l[index][3].split('.')[1], '/', l[index][3].split('.')[2][2:] ,' 0', l[index][5]
                        else: 
                            return '0', l[index][3].split('.')[0], '/0', l[index][3].split('.')[1], '/', l[index][3].split('.')[2][2:] ,' ', l[index][5]
                    else:
                        if int(l[index][5].split(':')[0]) < 10:
                            return '0', l[index][3].split('.')[0], '/', l[index][3].split('.')[1], '/', l[index][3].split('.')[2][2:] ,' 0', l[index][5]
                        else: 
                            return '0', l[index][3].split('.')[0], '/', l[index][3].split('.')[1], '/', l[index][3].split('.')[2][2:] ,' ', l[index][5]
                else:
                    if  int(l[index][3].split('.')[1])< 10:
                        if int(l[index][5].split(':')[0]) < 10:
                            return '', l[index][3].split('.')[0], '/0', l[index][3].split('.')[1], '/', l[index][3].split('.')[2][2:] ,' 0', l[index][5]
                        else: 
                            return '', l[index][3].split('.')[0], '/0', l[index][3].split('.')[1], '/', l[index][3].split('.')[2][2:] ,' ', l[index][5]
                    else:
                        if int(l[index][5].split(':')[0]) < 10:
                            return '', l[index][3].split('.')[0], '/', l[index][3].split('.')[1], '/', l[index][3].split('.')[2][2:] ,' 0', l[index][5]
                        else: 
                            return '', l[index][3].split('.')[0], '/', l[index][3].split('.')[1], '/', l[index][3].split('.')[2][2:] ,' ', l[index][5]
            return ''

        if id == 'getcontact':
            db = sqlite3.connect('data.db')
            cursor = db.cursor()
            cursor.execute('SELECT * FROM contact')
            l = []
            for _ in cursor.fetchall():
                l.append(_)
            db.close()
            return str(l).strip('[]').replace('),','),</br>')
        elif id == 'cleardb':
            # Get a cursor object
            db = sqlite3.connect('data.db')
            cursor = db.cursor()
            cursor.execute('''DROP TABLE reserve''')
            db.commit()
            cursor.execute('''DROP TABLE contact''')
            db.commit()
            db.close()
            return 'White Ya Database'

        elif id == 'calls':
            return str(locations.keys()) , '''</br> createdb </br>
                       contact </br>
                       reserve </br>
                       getallfromdb </br>
                       gettodayfromdb </br>
                       getcurrentfromdb </br>
                       get contact </br>
                       cleardb </br>

                    '''

        else:
            return('The %s is not defined ' % id)

    def PUT(self, location = None, value =None):
        locations[location] = value or locations[location] 
        return location,value

    def POST(self,*pargs):
        return 'none'

current_dir = os.path.dirname(os.path.abspath(__file__))

conf = {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.staticfile.root': current_dir },


        '/index':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/index.html'},

        '/img.html':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/img.html'},

        '/style.css':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/style.css'},

        '/jquery.min.js':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/jquery.min.js'},

        '/w2ui-1.4.2.min.js':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/w2ui-1.4.2.min.js'},

        '/w2ui-1.4.2.min.css':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/w2ui-1.4.2.min.css'},

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

         '/contact.svg':
            {'tools.staticfile.on': True,
            'tools.staticfile.filename':
            'static/contact.svg'},

         'global':{
                'server.socket_port':8080
                }}
cherrypy.quickstart(Root(), '/',conf
    )

