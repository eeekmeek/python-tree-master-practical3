# Converting milliseconds to hours, minutes, and seconds

def convert_ms(n):
    # 1h = 60 mins = 3600 sec = 3600 * 1000 ms
    secConverted = int(mSec/1000)       
    time = '{0}:{1}:{2}'.format(int(secConverted/3600), int((secConverted%3600)/60), secConverted%60 )
    
    return _time

n = int(input())
print(convert_ms(n))



