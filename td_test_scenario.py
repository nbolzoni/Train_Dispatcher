from train_dispatcher import *

track1seg001 = Track(pos_x=0,pos_y=350)
track1seg002 = Track(pos_x=101,pos_y=350)
track1seg003 = Track(pos_x=202,pos_y=350)
track1seg004 = Track(pos_x=303,pos_y=350)
track1swi005 = Switch(direction = 0,pos_x=404,pos_y=350,ID="sw1005")
track1seg006 = Track(pos_x=505,pos_y=350)
track1seg007 = Track(pos_x=606,pos_y=350)
track1seg008 = Track(pos_x=707,pos_y=350)
track1seg009 = Track(pos_x=808,pos_y=350)

track2seg001 = Track(pos_x=505,pos_y=400)
track2seg002 = Track(pos_x=606,pos_y=400)
track2seg003 = Track(pos_x=707,pos_y=400)

track1seg001.next = track1seg002
track1seg002.next = track1seg003
track1seg003.next = track1seg004
track1seg004.next = track1swi005
track1swi005.next = track1seg006
track1seg006.next = track1seg007
track1seg007.next = track1seg008
track1seg008.next = track1seg009

track1swi005.div = track2seg001
track2seg001.next = track2seg002
track2seg002.next = track2seg003

track1seg002.prev = track1seg001
track1seg003.prev = track1seg002
track1seg004.prev = track1seg003
track1swi005.prev = track1seg004
track1seg006.prev = track1swi005
track1seg007.prev = track1seg006
track1seg008.prev = track1seg007
track1seg009.prev = track1seg008

track2seg001.prev = track1swi005
track2seg002.prev = track2seg001
track2seg003.prev = track2seg002

signal_101E = ABS_Signal(track1seg002,0,pos_x=101,pos_y=350,signum="101E")
signal_102E = Controlled_Signal(track1swi005,0,pos_x=404,pos_y=350,signum="102E")
signal_103E = End_Signal(track1seg009,0,pos_x=808,pos_y=350,signum="103E")

signal_101E.nextSig = signal_102E
signal_102E.nextSig = signal_103E

signal_101W = End_Signal(track1seg001,1,pos_x=0,pos_y=350,signum="101W")
signal_102W = Controlled_Signal(track1seg006,1,pos_x=505,pos_y=350,signum="102W")
signal_103W = ABS_Signal(track1seg008,1,pos_x=707,pos_y=350,signum="103W")

signal_103W.nextSig = signal_102W
signal_102W.nextSig = signal_102W.divSig = signal_101W

signal_202W = Controlled_Signal(track2seg001,1,pos_x=505,pos_y=400,signum="202W")
signal_202W.nextSig = signal_202W.divSig = signal_101W

signal_203E = End_Signal(track2seg003,0,pos_x=707,pos_y=400,signum="203E")
signal_102E.divSig = signal_203E

train001 = Train(track1seg001,"East")
train002 = Train(track2seg003,"West")

signals = [signal_101E,
           signal_102E,
           signal_103E,
           signal_101W,
           signal_102W,
           signal_103W,

           signal_202W,
           signal_203E]

tracks = [track1seg001,
          track1seg002,
          track1seg003,
          track1seg004,
          track1swi005,
          track1seg006,
          track1seg007,
          track1seg008,
          track1seg009,

          track2seg001,
          track2seg002,
          track2seg003]

trains = [train001,
          train002]

globalMovement(trains,tracks,signals)
