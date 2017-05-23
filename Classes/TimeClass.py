class Time(object):
    ''' time in hours minutes seconds'''
    def __init__(self, h=0, m=0, s=0):
        self.h = int(h);
        self.m = int(m);
        self.s = int(s);

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.h, self.m, self.s)

    def is_valid(self):
        if self.h < 24 or self.h >= 0 or self.m <60 or self.m >= 0 or self.s <60 or self.s >=0:
            return True
        else:
            return False
    def add_time(t1,t2):
        return 0

    def convert_to_seconds(self):
        return self.h*3600 + self.m*60 + self.s

    def convert_to_hms(s):
        time = Time()
        m     , time.s = divmod(s,60)
        time.h, time.m = divmod(m,60)
        return time

    def mul_time(n,time_obj):
        m=time_obj.convert_to_seconds()
        return Time.convert_to_hms(m*n)

    def increment(self, seconds):
        return convert_to_hms(convert_to_seconds(self)+seconds)



t1 = Time(15,25,54)
s=t1.convert_to_seconds()
print(s)
t2 = Time.convert_to_hms(s)
t3 = Time.mul_time(2,t2)
print(t1, '   ', t3)
