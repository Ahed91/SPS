package com.ahed.smsreceiver;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.telephony.SmsMessage;
import android.util.Log;
import android.widget.EditText;
import android.widget.Toast;

import java.util.Objects;

/**
 * Created by ahed on 16/12/14.
 */
public class SMSReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        Bundle bundle = intent.getExtras();
        SmsMessage[] msgs = null;
        String str = "SMS from ";
        Integer iscleint = 0;
        String sms_body = "";
        String sms_sender = "";
        if (bundle != null)
        {
            Object[] pdus = (Object[]) bundle.get("pdus");
            msgs = new SmsMessage[pdus.length];
            for (int i=0; i<msgs.length; i++){
                msgs[i] = SmsMessage.createFromPdu((byte[])pdus[i]);
                if (i==0) {
                    sms_sender = msgs[i].getOriginatingAddress();
                    str += sms_sender;
                    str += ": ";
                }
                sms_body = msgs[i].getMessageBody().toString();
                str += sms_body;
            }

            Toast.makeText(context, str, Toast.LENGTH_SHORT).show();
            if (sms_body.subSequence(0,3).equals("sps")) {
                Log.d("SMSReceiver", str);
            }
            if (iscleint == 1) {
                MainActivity AA = new MainActivity();
                AA.sendSMS(sms_sender, "Done man , thnx");
            }
        }
    }
}
