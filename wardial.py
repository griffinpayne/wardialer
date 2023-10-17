import sys
import os
from twilio.rest import Client
from optparse import OptionParser

parser=OptionParser()
parser.add_option("-s", "--sid", type="string")
parser.add_option("-t", "--token", type="string")
parser.add_option("-f", "--frnum", type="string")
parser.add_option("-i", "--infile", type="string")
parser.add_option("-u", "--url", type="string")
parser.add_option("-o", "--outfile", type="string", dest="filename")
(options, args)=parser.parse_args()

num_file = open((options.infile), 'r')
numbers = num_file.readlines()
client = Client((options.sid),(options.token))

print("Dialed #       Call SID")
print(49 * "-")
print(("Dialed #           Call SID"), file=open((options.filename), "w"))
print((49 * "-"), file=open((options.filename), "a"))

def make_calls():
for line in numbers:
    call = client.calls.create(
                       url=(options.url),
                       to=(line),
                       from_=(options.frnum)
                               )
    print (call.to_formatted,call.sid)
    print ((call.to_formatted,call.sid), file=open((options.filename), "a"))

def get_logs():
   print("\nRetrieve logs from Twilio now?")
      answer=None
   while answer not in ("y", "n"):
    answer=input("\n(y)es/(n)o? ")
   if answer == "n":
    sys.exit("\nGoodbye")
   elif answer == "y":
    #client = Client((options.sid),(options.token))
    calls = client.calls.list()
    for record in calls:
        print((record.sid, record.to_formatted, record.status, record.answered_by), file=open((filename), "a"))
   else:
    print("\nPlease enter y or n")

make_calls()
get_logs()