s = str(input())
q = 1
x = list(s)
i = 0

opening = x.count('(') + x.count('[') + x.count('{')
closing = x.count(')') + x.count(']') + x.count('}')

if opening != closing:
    q = 2
else:
    while i < len(x):
        try:
            if x[i] == '(':
                if x[i+1] == ')':
                    q = 0
                if x[i+1] == ']' or x[i+1] == '}':
                    q = 2
                    break
            
            if x[i] == '[':
                if x[i+1] == ')' or x[i+1] == '}':
                    q = 2
                    break
                if x[i+1] == ']':
                    q = 0
                
            if x[i] == '{':
                if x[i+1] == ')' or x[i+1] == ']':
                    q = 2
                    break
                if x[i+1] == '}':
                    q = 0
                
            i += 1
        
        except IndexError:
            print('false')
            break
         
         
if q == 0:
    print('true')
elif q == 2:
    print('false')
    