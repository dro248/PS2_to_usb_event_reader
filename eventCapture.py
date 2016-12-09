#!/usr/bin/python
import struct
import time
import sys


button_table = {
	288 : 'TRIANGLE_BUTTON',
	289 : 'CIRCLE_BUTTON',
	290 : 'X_BUTTON',
	291 : 'SQUARE_BUTTON'
}

value_table = { 0:'RELEASED', 1:'PRESSED'}


#################################
# 		free FUNCTIONS			#
#################################
def interpret(button_table, value_table, etype, code, value):
	# print "interpreting..."
	if etype == 1:
		print button_table[code], value_table[value]
	    # print "type", etype, "code", code, "value", value
	    # print "-------------------"






#####################################################################
# MAIN

if len(sys.argv) < 2:
	print "Please include the event number (ps2 controller is 15)."
	print "Usage: ./eventCapture.py [eventNumber]"
	sys.exit(1)


infile_path = "/dev/input/event" + (sys.argv[1] if len(sys.argv) > 1 else "0")

#long int, long int, unsigned short, unsigned short, unsigned int
FORMAT = 'llHHI'
EVENT_SIZE = struct.calcsize(FORMAT)

#open file in binary mode
in_file = open(infile_path, "rb")

event = in_file.read(EVENT_SIZE)

while event:
    (tv_sec, tv_usec, etype, code, value) = struct.unpack(FORMAT, event)
    # print "event"
    # if etype > 0:
	   #  print "etype", etype, "code", code, "value", value
	   #  print "-------------------"
    
    interpret(button_table, value_table, etype, code, value)

    event = in_file.read(EVENT_SIZE)



    # if type != 0 or code != 0 or value != 0:
    #     print("Event type %u, code %u, value %u at %d.%d" % \
    #         (type, code, value, tv_sec, tv_usec))

    # else:
    #     # Events with code, type and value == 0 are "separator" events
    #     print("===========================================")

    # event = in_file.read(EVENT_SIZE)

in_file.close()