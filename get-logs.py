import sys
import os
from twilio.rest import Client
from optparse import OptionParser

# options
parser=OptionParser()
parser.add_option("-s", "--sid", type="string")
parser.add_option("-t", "--token", type="string")
parser.add_option("-o", "--outfile", type="string", dest="filename")
(options, args)=parser.parse_args()

# get the logs
print("\nRetrieve logs from Twilio now?")
answer=None
while answer not in ("y", "n"):
   answer=input("\n(y)es/(n)o? ")
   if answer == "n":
    sys.exit("\nGoodbye")
   elif answer == "y":
    client = Client((options.sid),(options.token))
    calls = client.calls.list()
    print(client)
    for record in calls:
        print((record.sid, record.to_formatted, record.status, record.answered_by), file=open((options.filename), "w"))
   else:
    print("\nPlease enter y or n")