#!/usr/bin/env python
# encoding: utf-8

import sys
import threading
import cherrypy
import os.path
import sqlite3
import time
import json
import re
from grequests import AsyncRequest

current_dir = os.path.dirname(os.path.abspath(__file__))
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
    'E4': 'red',
    'F1': 'red',
    'F2': 'green',
    'F3': 'green',
    'F4': 'green',
}

class Root:

    time_snap = time.time()
    time_snap2 = time.time()

    exposed = True
    
    @cherrypy.expose
    def index(self, location=None, value=None):
        # check if not logged in then redirect to signup
        if cherrypy.session.get('username') == None:
            raise cherrypy.HTTPRedirect("/sign") 
        # if request for example /?location=A1 return it's value line 8 
        # if request for example /?location=A1&value=green  change A1 value to green
        if location :
            if round(time.time() - Root.time_snap) > 5:
                Root.time_snap = time.time()
                self.update_indecators()
            if location in locations:  
                if value == 'green':
                    locations[location] = 'green'
                elif value == 'red':
                    locations[location] = 'red'
                return('%s' % (locations[location]))
            elif location in locations: 
                if value == 'green':
                    locations[location] = 'green'
                elif value == 'red':
                    locations[location] = 'red'
                return('%s' % (locations[location]))
        # if request / then return main.html
        raise cherrypy.HTTPRedirect("/main") 

    def update_indecators(self):
        current_date=time.strftime('%d.%m.%Y')
        if current_date[0]=='0':
            current_date = current_date[1:]
        current_date =  re.sub('\.0', '.', current_date)
        print  current_date 
        db = sqlite3.connect(current_dir+'/data.db')
        cursor = db.cursor()
        timenow = time.strftime('%H:%M')
        print timenow 
        for k in locations:
            cursor.execute('SELECT * FROM reserve where location =? and date=?',(k,current_date,))
            l = cursor.fetchall()
            print str(l)
            locations[k]='green'
            if l :
                for i in l:
                    if int(timenow.split(':')[0]) == int(i[4].split(':')[0]):
                        if int(timenow.split(':')[1]) == int(i[4].split(':')[1]):
                            locations[k]='red'
                        elif int(timenow.split(':')[1]) > int(i[4].split(':')[1]):
                            if int(timenow.split(':')[0]) == int(i[5].split(':')[0]):
                                if int(timenow.split(':')[1]) < int(i[5].split(':')[1]):
                                    locations[k]='red'
                            elif int(timenow.split(':')[0]) < int(i[5].split(':')[0]):
                                locations[k]='red'
                    elif int(timenow.split(':')[0]) > int(i[4].split(':')[0]):
                        if int(timenow.split(':')[0]) < int(i[5].split(':')[0]):
                            locations[k]='red'
                        if int(timenow.split(':')[0]) == int(i[5].split(':')[0]):
                            if int(timenow.split(':')[1]) < int(i[5].split(':')[1]):
                                locations[k]='red'


    @cherrypy.expose
    def alllocations(self):
        if round(time.time()-Root.time_snap) > 5:
            Root.time_snap = time.time()
            self.update_indecators()
        A1 = locations['A1']
        A2 = locations['A2']
        A3 = locations['A3']
        A4 = locations['A4']
        B1 = locations['B1']
        B2 = locations['B2']
        B3 = locations['B3']
        B4 = locations['B4']
        C1 = locations['C1']
        C2 = locations['C2']
        C3 = locations['C3']
        C4 = locations['C4']
        D1 = locations['D1']
        D2 = locations['D2']
        D3 = locations['D3']
        D4 = locations['D4']
        E1 = locations['E1']
        E2 = locations['E2']
        E3 = locations['E3']
        E4 = locations['E4']
        F1 = locations['F1']
        F2 = locations['F2']
        F3 = locations['F3']
        F4 = locations['F4']
        return('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s'
               % (A1,A2,A3,A4,B1,B2,B3,B4,C1,C2,C3,C4,D1,D2,D3,D4,E1,E2,E3,E4,F1,F2,F3,F4))

    @cherrypy.expose
    def echo(self):
        return  cherrypy.session.get('username')

    @cherrypy.expose
    def login(self, email, password):
        print email
        p_email = re.compile('^([a-z]{1,5}[0-9]{0,5}){1,20}@([a-z]{1,5}[0-9]{0,5}){1,20}[.](com|org|net|ps)$')
        if not p_email.match(email):
            return 'Unaccepted Emial'
        db = sqlite3.connect(current_dir+'/data.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users where email = ?',(email,) )
        l = cursor.fetchall()
        db.close()
        if l :
            username = str(l[0][1])
            if password == str(l[0][3]):
                cherrypy.session['username'] = username
            else:
                return 'wrong password'
        else:
            return 'Please Sign up , before login' 
        raise cherrypy.HTTPRedirect("/main") 

    @cherrypy.expose
    def login_app(self, email, password):
        p_email = re.compile('^([a-z]{1,5}[0-9]{0,5}){1,20}@([a-z]{1,5}[0-9]{0,5}){1,20}[.](com|org|net|ps)$')
        if not p_email.match(email):
            return 'Unaccepted Emial'
        db = sqlite3.connect(current_dir+'/data.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users where email = ?',(email,) )
        l = cursor.fetchall()
        db.close()
        if l :
            username = str(l[0][1])
            if password == str(l[0][3]):
                cherrypy.session['username'] = username
                return 'logged,%s'%(username)
            else:
                return 'Not Matched Password'
        else:
            return 'Please Sign up , before login' 
        return 'Unregistered Email'

    @cherrypy.expose
    def signup(self, username, email, password, mobile):
        p_email = re.compile('^([a-z]{1,5}[0-9]{0,5}){1,20}@([a-z]{1,5}[0-9]{0,5}){1,20}[.](com|org|net|ps)$')
        if not p_email.match(email):
            return 'Unaccepted Email'
        p_username = re.compile('^([a-z]{1,5}[0-9]{0,5}){1,20}$')
        username = username.lower()
        if not p_username.match(username):
            return 'Unaccepted Username'
        p_mobile = re.compile('^([0-9]{7,20}|[+][0-9]{12,20})$')
        if not p_mobile.match(mobile):
            return 'Unaccepted mobile'
        if len(password) < 6 :
            return 'Your password less than 6 characters'
        db = sqlite3.connect(current_dir+'/data.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users where username = ? or email = ?',(username, email) )
        l = cursor.fetchall()
        if l :
            return 'Please choose another username/email'
        cursor.execute('''INSERT INTO users(username, email, password,mobile )
                                     VALUES(?,?,?,?)''', (username, email, password, mobile))
        db.commit()
        db.close()
        raise cherrypy.HTTPRedirect("/sign") 

    @cherrypy.expose
    def records(self):
        rec = {"total": 9,"records": [{ "recid": 1, "username": "ahed", "location": "Doe", "date": "jdoe@gmail.com", "timefrom": "4/3/2012"  },{ "recid": 2, "username": "Stuart", "location": "Motzart", "date": "jdoe@gmail.com", "timefrom": "4/3/2012"  },{ "recid": 3, "username": "Jin", "location": "Franson", "date": "jdoe@gmail.com", "timefrom": "4/3/2012"  },{ "recid": 4, "username": "Susan", "location": "Ottie", "date": "jdoe@gmail.com", "timefrom": "4/3/2012"  },{ "recid": 5, "username": "Kelly", "location": "Silver", "date": "jdoe@gmail.com", "timefrom": "4/3/2012"  },{ "recid": 6, "username": "Francis", "location": "Gatos", "date": "jdoe@gmail.com", "timefrom": "4/3/2012"  },{ "recid": 7, "username": "Mark", "location": "Welldo", "date": "jdoe@gmail.com", "timefrom": "4/3/2012"  },{ "recid": 8, "username": "Thomas", "location": "Bahh", "date": "jdoe@gmail.com", "timefrom": "4/3/2012"  },{ "recid": 9, "username": "Sergei", "location": "Rachmaninov", "date": "jdoe@gmail.com", "timefrom": "4/3/2012"  }]}
        return json.dumps(rec) 
            
    @cherrypy.expose
    def contact(self,*pargs):
        first_name = pargs[0]
        last_name = pargs[1]
        email = pargs[2]
        message = pargs[3]
        db = sqlite3.connect(current_dir+'/data.db')
        cursor = db.cursor()
        cursor.execute('''INSERT INTO contact(firstname, lastname, email, body)
                                     VALUES(?,?,?,?)''', (first_name, last_name, email, message))
        db.commit()
        db.close()
        return 'Thanks for your interest'

    @cherrypy.expose
    def reserve(self,*pargs):
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
        db = sqlite3.connect(current_dir+'/data.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users where username = ?',(username,) )
        l = cursor.fetchall()
        if not l :
            cursor.execute('SELECT * FROM users where mobile = ?',(username,) )
            l = cursor.fetchall()
            if l :
                username = l[0][1]
            else:
                username = cherrypy.session.get('username')
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
        return 'Done'

    @cherrypy.expose
    def reserve_num(self,*pargs):
        username = pargs[0]
        timefrom = pargs[1]
        timeto = pargs[2]
        note = pargs[3]
        current_date=time.strftime('%d.%m.%Y')
        if current_date[0]=='0':
            current_date = current_date[1:]
        current_date =  re.sub('\.0', '.', current_date)
        if int(timefrom.split(':')[0]) > int(timeto.split(':')[0]):
            return 'Error Time Interval (timefrom hour > timeto hour)'
        if int(timefrom.split(':')[0]) == int(timeto.split(':')[0]):
            if int(timefrom.split(':')[1]) >= int(timeto.split(':')[1]):
                return 'Error Time Interval (timefrom min > timeto min)'
        # Connect to database
        db = sqlite3.connect(current_dir+'/data.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users where mobile = ?',(username,) )
        l = cursor.fetchall()
        if l :
            username = l[0][1]
        else:
            return 'Error mobile not registered'
        for location in locations:
            if location == 'D3' or location == 'D4':
                continue 
            cursor.execute('''SELECT * FROM reserve where location=? and date=?''',(location, current_date,) )
            l = cursor.fetchall()
            if not l:
                print 'there"s no reserve in %s today' %location
                cursor.execute('''INSERT INTO reserve(username, location, date, timefrom, timeto, note)
                                             VALUES(?,?,?,?,?,?)''', (username, location, current_date, timefrom, timeto, note))
                db.commit()
                db.close()
                return 'Done'
            for i in l:
                empty = 1
                print i
                if int(timefrom.split(':')[0]) == int(i[4].split(':')[0]):
                    if int(timefrom.split(':')[1]) == int(i[4].split(':')[1]):
                        print 'Choose another time or location(1timefrom equel old timrfrom)'
                        empty = 0
                    if int(timefrom.split(':')[1]) > int(i[4].split(':')[1]):
                        if int(timefrom.split(':')[0]) == int(i[5].split(':')[0]):
                            if int(timefrom.split(':')[1]) < int(i[5].split(':')[1]):
                                print 'Choose another time or location(1timefrom min less than old timeto)'
                                empty = 0
                        if int(timefrom.split(':')[0]) < int(i[5].split(':')[0]):
                            print 'Choose another time or location(1timefrom hour less than old timeto)'
                            empty = 0
                    if int(timefrom.split(':')[1]) < int(i[4].split(':')[1]):
                        if int(timeto.split(':')[0]) == int(i[4].split(':')[0]):
                            if int(timeto.split(':')[1]) > int(i[4].split(':')[1]):
                                print 'Choose another time or location(1timeto min more than old timeto)'
                                empty = 0
                        if int(timeto.split(':')[0]) > int(i[4].split(':')[0]):
                            print 'Choose another time or location(1timeto hour more than old timeto)'
                            empty = 0
                if int(timefrom.split(':')[0]) < int(i[4].split(':')[0]):
                    if int(timeto.split(':')[0]) > int(i[4].split(':')[0]):
                        print 'Choose another time or location(2timeto hour more than old timefrom)'
                        empty = 0
                    if int(timeto.split(':')[0]) == int(i[4].split(':')[0]):
                        if int(timeto.split(':')[1]) > int(i[4].split(':')[1]):
                            print 'Choose another time or location(2timeto min more than old timefrom)'
                            empty = 0
                if int(timefrom.split(':')[0]) > int(i[4].split(':')[0]):
                    if int(timefrom.split(':')[0]) < int(i[5].split(':')[0]):
                        print 'Choose another time or location(3timefrom hour less than old timeto)'
                        empty = 0
                    if int(timefrom.split(':')[0]) == int(i[5].split(':')[0]):
                        if int(timefrom.split(':')[1]) < int(i[5].split(':')[1]):
                            print 'Choose another time or location(3timefrom min less than old timeto)'
                            empty = 0
                if empty == 1:
                    print 'location %s' %location
                    cursor.execute('''INSERT INTO reserve(username, location, date, timefrom, timeto, note)
                                                 VALUES(?,?,?,?,?,?)''', (username, location, current_date, timefrom, timeto, note))
                    db.commit()
                    db.close()
                    return 'Done'
        return 'Undone'

    @cherrypy.expose
    def backup_reserve(self,*pargs):
        location = pargs[0]
        timefrom = pargs[1]
        current_date=time.strftime('%d.%m.%Y')
        if current_date[0]=='0':
            current_date = current_date[1:]
        current_date =  re.sub('\.0', '.', current_date)
        # Connect to database
        db = sqlite3.connect(current_dir+'/data.db')
        cursor = db.cursor()
        cursor.execute('''SELECT * FROM reserve where location=? and date=? and timefrom=?''',(location, current_date, timefrom) )
        row = cursor.fetchone()
        timeto = row[5]
        for location in ['D3', 'D4']:
            cursor.execute('''SELECT * FROM reserve where location=? and date=? ''',(location, current_date) )
            l = cursor.fetchall()
            if not l:
                print 'there"s no reserve in %s today' %location
                cursor.execute('''INSERT INTO reserve(username, location, date, timefrom, timeto, note)
                                             VALUES(?,?,?,?,?,?)''', (row[1], location, row[3], row[4], row[5], row[6]))
                db.commit()
                db.close()
                return 'Done'
            for i in l:
                empty = 1
                print i
                if int(timefrom.split(':')[0]) == int(i[4].split(':')[0]):
                    if int(timefrom.split(':')[1]) == int(i[4].split(':')[1]):
                        print 'Choose another time or location(1timefrom equel old timrfrom)'
                        empty = 0
                    if int(timefrom.split(':')[1]) > int(i[4].split(':')[1]):
                        if int(timefrom.split(':')[0]) == int(i[5].split(':')[0]):
                            if int(timefrom.split(':')[1]) < int(i[5].split(':')[1]):
                                print 'Choose another time or location(1timefrom min less than old timeto)'
                                empty = 0
                        if int(timefrom.split(':')[0]) < int(i[5].split(':')[0]):
                            print 'Choose another time or location(1timefrom hour less than old timeto)'
                            empty = 0
                    if int(timefrom.split(':')[1]) < int(i[4].split(':')[1]):
                        if int(timeto.split(':')[0]) == int(i[4].split(':')[0]):
                            if int(timeto.split(':')[1]) > int(i[4].split(':')[1]):
                                print 'Choose another time or location(1timeto min more than old timeto)'
                                empty = 0
                        if int(timeto.split(':')[0]) > int(i[4].split(':')[0]):
                            print 'Choose another time or location(1timeto hour more than old timeto)'
                            empty = 0
                if int(timefrom.split(':')[0]) < int(i[4].split(':')[0]):
                    if int(timeto.split(':')[0]) > int(i[4].split(':')[0]):
                        print 'Choose another time or location(2timeto hour more than old timefrom)'
                        empty = 0
                    if int(timeto.split(':')[0]) == int(i[4].split(':')[0]):
                        if int(timeto.split(':')[1]) > int(i[4].split(':')[1]):
                            print 'Choose another time or location(2timeto min more than old timefrom)'
                            empty = 0
                if int(timefrom.split(':')[0]) > int(i[4].split(':')[0]):
                    if int(timefrom.split(':')[0]) < int(i[5].split(':')[0]):
                        print 'Choose another time or location(3timefrom hour less than old timeto)'
                        empty = 0
                    if int(timefrom.split(':')[0]) == int(i[5].split(':')[0]):
                        if int(timefrom.split(':')[1]) < int(i[5].split(':')[1]):
                            print 'Choose another time or location(3timefrom min less than old timeto)'
                            empty = 0
                if empty == 1:
                    print 'location %s' %location
                    cursor.execute('''INSERT INTO reserve(username, location, date, timefrom, timeto, note)
                                                 VALUES(?,?,?,?,?,?)''', (row[1], location, row[3], row[4], row[5], row[6]))
                    db.commit()
                    db.close()
                    return 'Done'
        return 'Undone'

    @cherrypy.expose
    def getallfromdb(self):
        db = sqlite3.connect(current_dir+'/data.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users')
        l = []
        for _ in cursor.fetchall():
            l.append(_)
        cursor.execute('SELECT * FROM reserve')
        for _ in cursor.fetchall():
            l.append(_)
        db.close()
        return str(l).strip('[]').replace('),','),</br>')

    @cherrypy.expose
    def getanydatefromdb(self,*pargs):
        any_date= pargs[0]
        db = sqlite3.connect(current_dir+'/data.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM reserve where date=?',(any_date,))
        l = []
        for _ in cursor.fetchall():
            l.append(_)
        db.close()
        return str(l).strip('[]').replace('),','),</br>')

    @cherrypy.expose
    def gettodayfromdb(self):
        current_date=time.strftime('%d.%m.%Y')
        if current_date[0]=='0':
            current_date = current_date[1:]
        current_date =  re.sub('\.0', '.', current_date)
        db = sqlite3.connect(current_dir+'/data.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM reserve where date=?',(current_date,))
        l = []
        for _ in cursor.fetchall():
            l.append(_)
        db.close()
        return str(l).strip('[]').replace('),','),</br>')

    @cherrypy.expose
    def getcurrentfromdb(self, *pargs):
        if len(pargs) == 0 :
            return 'No location is inserted'
        current_date=time.strftime('%d.%m.%Y')
        if current_date[0]=='0':
            current_date = current_date[1:]
        current_date =  re.sub('\.0', '.', current_date)
        l=[]
        db = sqlite3.connect(current_dir+'/data.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM reserve where date=? and location=?',(current_date,pargs[0]))
        for _ in cursor.fetchall():
            l.append(_)
        db.close()
        current_min = int(time.strftime('%M'))
        current_hour = int(time.strftime('%H'))
        close_min = 59
        close_hour = 23
        index = -1
        index2 = -1
        if len(l):
            for idx,item in enumerate(l):
                if int(item[4].split(':')[0]) == current_hour:
                    index2 = -2
                    if int(item[4].split(':')[1]) >= current_min and  int(item[4].split(':')[1]) < close_min :
                        close_min = int(item[4].split(':')[1])
                        index = idx
            if index2 == -1 :
                for idx,item in enumerate(l):
                    if int(item[4].split(':')[0]) > current_hour  and int(item[4].split(':')[0]) <= close_hour :
                        if int(item[4].split(':')[0]) == close_hour :
                            if int(item[4].split(':')[1]) < close_min :
                                close_min = int(item[4].split(':')[1])
                                index = idx
                        if int(item[4].split(':')[0]) < close_hour :
                            close_hour = int(item[4].split(':')[0])
                            close_min = int(item[4].split(':')[1])
                            index = idx
            return str(l[index])
        return ''

    @cherrypy.expose
    def timefrom(self, *pargs):
        # check for sync
        if round(time.time() - Root.time_snap2) > 60:
            Root.time_snap2 = time.time()
            sync()
        if len(pargs) == 0 :
            return 'No location is inserted'
        current_date=time.strftime('%d.%m.%Y')
        if current_date[0]=='0':
            current_date = current_date[1:]
        current_date =  re.sub('\.0', '.', current_date)
        l=[]
        db = sqlite3.connect(current_dir+'/data.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM reserve where date=? and location=?',(current_date,pargs[0]))
        for _ in cursor.fetchall():
            l.append(_)
        db.close()
        print l
        if not l:
            return 'None'
        current_min = int(time.strftime('%M'))
        current_hour = int(time.strftime('%H'))
        close_min = 59
        close_hour = 23
        index = -1
        index2 = -1
        if len(l):
            for idx,item in enumerate(l):
                if int(item[5].split(':')[0]) == current_hour:
                    index2 = -2
                    if int(item[5].split(':')[1]) >= current_min and  int(item[5].split(':')[1]) < close_min :
                        close_min = int(item[5].split(':')[1])
                        index = idx
                if int(item[4].split(':')[0]) == current_hour:
                    index2 = -2
                    if int(item[4].split(':')[1]) >= current_min and  int(item[4].split(':')[1]) < close_min :
                        close_min = int(item[4].split(':')[1])
                        index = idx
            if index2 == -1 :
                for idx,item in enumerate(l):
                    if int(item[4].split(':')[0]) > current_hour  and int(item[4].split(':')[0]) <= close_hour :
                        if int(item[4].split(':')[0]) == close_hour :
                            if int(item[4].split(':')[1]) < close_min :
                                close_min = int(item[4].split(':')[1])
                                index = idx
                        if int(item[4].split(':')[0]) < close_hour :
                            close_hour = int(item[4].split(':')[0])
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

    @cherrypy.expose
    def timeto(self, *pargs):
        if len(pargs) == 0 :
            return 'No location is inserted'
        current_date=time.strftime('%d.%m.%Y')
        if current_date[0]=='0':
            current_date = current_date[1:]
        current_date =  re.sub('\.0', '.', current_date)
        l=[]
        db = sqlite3.connect(current_dir+'/data.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM reserve where date=? and location=?',(current_date, pargs[0]))
        for _ in cursor.fetchall():
            l.append(_)
        db.close()
        if not l:
            return 'None'
        print l
        current_min = int(time.strftime('%M'))
        current_hour = int(time.strftime('%H'))
        close_min = 59
        close_hour = 23
        index = -1
        index2 = -1
        if len(l):
            for idx,item in enumerate(l):
                if int(item[5].split(':')[0]) == current_hour:
                    index2 = -2
                    if int(item[5].split(':')[1]) >= current_min and  int(item[5].split(':')[1]) < close_min :
                        close_min = int(item[5].split(':')[1])
                        index = idx
                if int(item[4].split(':')[0]) == current_hour:
                    index2 = -2
                    if int(item[4].split(':')[1]) >= current_min and  int(item[4].split(':')[1]) < close_min :
                        close_min = int(item[4].split(':')[1])
                        index = idx
            if index2 == -1 :
                for idx,item in enumerate(l):
                    if int(item[4].split(':')[0]) > current_hour  and int(item[4].split(':')[0]) <= close_hour :
                        if int(item[4].split(':')[0]) == close_hour :
                            if int(item[4].split(':')[1]) < close_min :
                                close_min = int(item[4].split(':')[1])
                                index = idx
                        if int(item[4].split(':')[0]) < close_hour :
                            close_hour = int(item[4].split(':')[0])
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

    @cherrypy.expose
    def getcontact(self):
            db = sqlite3.connect(current_dir+'/data.db')
            cursor = db.cursor()
            cursor.execute('SELECT * FROM contact')
            l = []
            for _ in cursor.fetchall():
                l.append(_)
            db.close()
            return str(l).strip('[]').replace('),','),</br>')

    @cherrypy.expose
    def cleardb(self):
        # Get a cursor object
        db = sqlite3.connect(current_dir+'/data.db')
        cursor = db.cursor()
        cursor.execute('''DROP TABLE reserve''')
        db.commit()
        cursor.execute('''DROP TABLE contact''')
        db.commit()
        cursor.execute('''DROP TABLE users''')
        db.commit()
        db.close()
        return 'White Ya Database'

    @cherrypy.expose
    def calls(self):
        return str(locations.keys()) , '''</br> createdb </br>
                   contact </br>
                   reserve </br>
                   getallfromdb </br>
                   gettodayfromdb </br>
                   getcurrentfromdb </br>
                   get contact </br>
                   cleardb </br>

                '''

    @cherrypy.expose
    def default(self, *pargs, **kwargs):
        if cherrypy.session.get('username') == None:
            raise cherrypy.HTTPRedirect("/sign") 
        return('The %s is not defined '% (str(pargs)))

def startup_init():
    createdb()
    sync()

def createdb():
    # Get a cursor 
    db = sqlite3.connect(current_dir+'/data.db')
    cursor = db.cursor()
    cursor.execute('''
               CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT, email TEXT,
                                    password TEXT, mobile TEXT)   
                   ''')
    db.commit()
    cursor.execute('''INSERT INTO users(username, email, password,mobile )
                                 VALUES(?,?,?,?)''', ('admin', 'admin', '123456','0000000'))
    db.commit()
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
    print 'Database Created'


def sync():
    # Connect to database
    db = sqlite3.connect(current_dir+'/data.db')
    cursor = db.cursor()
    cursor.execute('''SELECT max(id) FROM reserve''')
    max_id = cursor.fetchone()[0]
    if max_id == None:
        print max_id , 'maxid None'
        max_id = 0
    try:
        req = AsyncRequest('GET','http://sps-ahmadghoul.rhcloud.com/sync/%s'%str(max_id+1))
        print 'http://sps-ahmadghoul.rhcloud.com/sync/%s'%str(max_id+1)
        req.send()
        s = req.response.text.split(')')
        print s
    except AttributeError:
        print 'AttributeError'
        return 'found AttributeError'
    for i in range(0,len(s)):
        if i==0:
            a = s[i].replace('u\'','').replace('\'','').replace('(','').split(', ')
        elif i== len(s)-1:
            continue
        else:
            a = s[i].replace('u\'','').replace('\'','').replace(', (','').split(', ')
        if len(a)<6 :
            continue
        cursor.execute('''INSERT INTO reserve(username, location, date, timefrom, timeto, note)
                                     VALUES(?,?,?,?,?,?)''', (a[0], a[1], a[2], a[3], a[4], a[5]))
        db.commit()
    db.close()
    return 'yes'


conf = {'/':
             {
             'tools.staticfile.root': current_dir ,
              },


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

cherrypy.engine.subscribe('start', startup_init)
cherrypy.quickstart(Root(), '/',conf
    )

