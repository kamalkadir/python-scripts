# string_times
```
def string_times(str, n):
  return str*n
```
# front_times
```
def front_times(str, n):
  if len(str)<3:
    return str*n
  else:
    return str[:3]*n
```
# string_bits
```
def string_bits(str):
  i = 0
  output=""
  while i < len(str):
    output = output+str[i]
    i+=2
  return output
```
