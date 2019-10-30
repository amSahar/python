import mymodule
import datetime as mx

print('1 + 8 =',mymodule.add(1,8))
print('4 - 2 =',mymodule.sub(4,2))
print('6 x 6 =',mymodule.mul(6,6))
print('8 / 2 =',mymodule.div(8,2))

x=mx.datetime.now()
print('Year: ',x.strftime('%Y'))
print('Month: ',x.strftime('%B'))
print('Day: ',x.strftime('%A'))
print('Time: ',x.strftime('%X'))
print('Date: ',x.strftime('%x'))

print('Tomorrow :',mx.datetime.now() + mx.timedelta(days=1))
print('Yesterday :',mx.datetime.now() - mx.timedelta(days=1))