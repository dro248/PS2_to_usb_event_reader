#!/usr/bin/python
import struct
import time
import sys

steering_table = {
	
}


button_table = {
	288 : 'TRIANGLE_BUTTON',
	289 : 'CIRCLE_BUTTON',
	290 : 'X_BUTTON',
    291 : 'SQUARE_BUTTON',
    292 : 'L2_BUTTON',
	293 : 'R2_BUTTON',
    294 : 'L1_BUTTON',
    295 : 'R1_BUTTON',
    296 : 'SELECT_BUTTON',
    297 : 'START_BUTTON',
    298 : 'L_STICK_BUTTON',
    299 : 'R_STICK_BUTTON',
}

value_table = { 0:'RELEASED', 1:'PRESSED'}


#################################
# 		free FUNCTIONS			#
#################################
def interpret(button_table, value_table, etype, code, value):
	
    if etype == 1:
        try:
            print button_table[code], value_table[value]
        except:
            print "button not found!"

    elif etype == 3:
        # up/down BUTTON(?): value ranges from (UP:0, to DOWN:255), middle is 127 or 128 (?)
        if code == 0:
            if value < 120:     print "LEFT_ARROW PRESSED", value
            elif value > 130:   print "RIGHT_ARROW PRESSED", value
        if code == 1:
            if value < 120:     print "UP_ARROW PRESSED", value
            elif value > 130:   print "DOWN_ARROW PRESSED", value
        if code == 2:
            # print "etype", etype, "code", code, "value", value
            if value < 128:     print "viewing UP:", value
            elif value > 128:   print "viewing DOWN:", value
        if code == 5:
            # print "etype", etype, "code", code, "value", value
            if value < 128:     print "viewing LEFT:", value
            elif value > 128:   print "viewing RIGHT:", value

    if etype == 0:
        return

    # print "etype", etype, "code", code, "value", value
    # print "-------------------"







#####################################################################
#                             MAIN                                  #
#####################################################################

##########
#  args  #
##########
if len(sys.argv) < 2:
    print "Please include the event number (ps2 controller is 15)."
    print "Usage: ./eventCapture.py [eventNumber]"
    sys.exit(1)


infile_path = "/dev/input/event" + (sys.argv[1] if len(sys.argv) > 1 else "0")


#################################
#  READ FROM /dev/input/eventX  #
#################################
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