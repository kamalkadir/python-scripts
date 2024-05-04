# sleep_in
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
```
def sleep_in(weekday, vacation):
  if vacation:
    return True
  elif not weekday:
    return True
  else:
    return False
```
# monkey_trouble
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
```
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  elif  not a_smile and not b_smile:
    return True
  else:
    return False
```
# sum_double
Given two int values, return their sum. Unless the two values are the same, then return double their sum.
```
def sum_double(a, b):
  if a == b:
    return 2 * (a+b)
  else:
    return a+b
```
# diff21
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
```
def diff21(n):
  if n > 21:
    return abs(21-n)*2
  else:
    return abs(21-n)
```
# parrot_trouble
We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
```
def parrot_trouble(talking, hour):
  if not talking:
    return False
  elif hour > 20 or hour < 7:
    return True
  else:
    return False
```
# makes10
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
```
def makes10(a, b):
  if a ==10 or b == 10 or a + b == 10:
    return True
  else:
    return False
```
# near_hundred
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
```
def near_hundred(n):
  if abs(100-n) <=10 or abs(200-n) <=10:
    return True
  else:
    return False
```
# pos_neg
Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.
```
def pos_neg(a, b, negative):
  if negative:
    if a < 0 and b < 0:
      return True
    else:
      return False
  elif a < 0 and b < 0:
    return False
  elif a > 0 and b > 0:
    return False
  else:
    return True
```




# front3
Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
```
def front3(str):
  if len(str)<3:
    return str*3
  else:
    return str[:3]*3
```
