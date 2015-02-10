from agenda.DB import backup
from time import sleep
from threading import Timer
from AP_Agenda.settings import MYTIMER

class RepeatedTimer(object):
    def __init__(self, interval, function):
        self._timer     = None
        self.interval   = interval
        self.function   = function
#        self.args       = args
#        self.kwargs     = kwargs
        self.is_running = False
#        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function()

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

class tempo:
    rt = RepeatedTimer(MYTIMER, backup.hacerBackUp)
    
    
    def iniciar(self):
        print ("starting back up...")
        self.rt.start()
        #rt = RepeatedTimer(2, backup.hacerBackUp, "World") # it auto-starts, no need of rt.start()
        
        #try:
        #    sleep(20) # your long-running job goes here...
        #finally:
        #    rt.stop() # better in a try/finally block to make sure the program ends!
        
    
    def detener(self):
        print ("stop back up...")
        self.rt.stop()
        
            