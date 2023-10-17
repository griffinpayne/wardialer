# wardialer
Wardialer built on Twilio

Makes calls from a file of numbers and retrieves the call logs

Requires a Twilio (https://www.twilio.com/) account

USAGE:
wardial.py -s [SID] -t [TOKEN] -f [ORIGINATING_PHONE_NUMBER] -i [FILE_OF_PHONE_NUMBERS] -u [TWILIO_CALL_HANDLER_URL] -O [OUTPUT_FILE]

EXAMPLE:
wardial.py -s AC4a7000000000000000 -t 0a0cd0000000000000 -f 12125551212 -i numbers.txt -u https://handler.twilio.com/twiml/EH5fc890f5d8adc5500000000000000 -o wardial-log.txt

It's best to use the stand-alone get-logs.py after some time has passed to give all of the calls a chance to complete.

USAGE:
get-logs.py -s [`SID`] -t [`TOKEN`] -O [`OUTPUT_FILE`]

EXAMPLE:
get-logs.py -s AC4a7000000000000000 -t 0a0cd0000000000000 -o wardial-log.txt
