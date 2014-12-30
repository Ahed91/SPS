#!/usr/bin/env python
# encoding: utf-8

import subprocess
import requests
import time
import re

def main():
    log_cat_cmd = "adb logcat -v raw SMSReceiver:D \*:S"
    p = subprocess.Popen([log_cat_cmd], shell=True, stdout=subprocess.PIPE)
    while 1:
        current_date=time.strftime('%d.%m.%Y')
        if current_date[0]=='0':
            current_date = current_date[1:]
        current_date =  re.sub('\.0', '.', current_date)
        req = p.stdout.readline()
        sms_sender = req[req.find("SMS from")+9:req.find(":")]
        sms_body = req[req.find("sps")+4:-2]
        params = sms_body.split(" ")
        url = ""
        if len(params) == 4:
            url = "http://sps-ahmadghoul.rhcloud.com/reserve/%s/%s/%s/%s/%s/%s"%(
                  sms_sender, params[0], current_date, params[2], params[3], "SMS")
        elif len (params)==5:
            url = "http://sps-ahmadghoul.rhcloud.com/reserve/%s/%s/%s/%s/%s/%s"%(
                  sms_sender, params[0], current_date, params[2], params[3], params[4]+ "SMS")
        if url != "":
            r = requests.get(url)

if __name__ == '__main__':
    main()
