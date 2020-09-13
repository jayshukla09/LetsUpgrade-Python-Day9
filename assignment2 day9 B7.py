Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def armstrong(range1 = 1, range2 = 1000):
    temp = num
    sum = 0
    while temp>0:
        digit=temp%10
        sum=sum+digit**3
        temp=temp//10
    
    if sum==num:
        yield num