#!/usr/bin/env python
# encoding: utf-8

import subprocess
import requests

def main():
    log_cat_cmd = "adb logcat -v raw SMSReceiver:D \*:S"
    p = subprocess.Popen([log_cat_cmd], shell=True, stdout=subprocess.PIPE)
    while 1:
        req = p.stdout.readline()
        sms_sender = req[req.find("SMS from")+9:req.find(":")]
        sms_body = req[req.find("sps")+4:-2]
        params = sms_body.split(" ")
        url = ""
        if len(params) == 4:
            url = "http://sps-ahmadghoul.rhcloud.com/reserve_num/%s/%s/%s/%s"%(
                  sms_sender, params[0], params[1], "SMS")
        elif len (params)==5:
            url = "http://sps-ahmadghoul.rhcloud.com/reserve_num/%s/%s/%s/%s"%(
                  sms_sender, params[0], params[1],  params[2]+ "SMS")
        if url != "":
            requests.get(url)

if __name__ == '__main__':
    main()
