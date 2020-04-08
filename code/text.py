import requests

url = "https://www.fast2sms.com/dev/bulk"

headers = {
'authorization': "4GR5pJskCYOrKe7c2VlyujLahDFNZi6f0Ez8XBH39bPTgxqStm7AE9MlwUL3JrzcDCjak0mOXbZtR8Ye",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}


def sendSMS(mobileNo,accountNo,price):

    
    text='Rs.'+str(price)+' debited to '+str(accountNo)+' [PORUR TOLL PLAZA]'

    payload = "sender_id=FSTSMS&message="+str(text)+"&language=english&route=p&numbers="+str(mobileNo)

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)



