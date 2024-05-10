s = str(input())

n = len(s)
one = s.upper()
two = s[0].lower() + (s[1:].upper() if n > 1 else '')
if s == one:
    print(s.lower())
elif s == two:
    print(s[0].upper() + (s[1:].lower() if n > 1 else ''))
else:
    print(s)