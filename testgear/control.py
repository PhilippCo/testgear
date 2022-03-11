import redis

class control():
    def __init__(self):
        self.r = redis.Redis(decode_responses=True)
        self.r.set('testgear_control', 'run')


    def running(self):
        if self.r.get('testgear_control') == "run":
            return True
        else:
            return False


    def stop(self):
        self.r.set('testgear_control', 'stop')
