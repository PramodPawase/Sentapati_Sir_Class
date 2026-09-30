
list1=[1,2,[2,3,4],3,4,4]
print(list1)

print('\n')

df=list1[2][1]
print(df)

print(issubclass(bool,int))

print(issubclass(bool,bool))

print(issubclass(int,str))
f=issubclass(int,int)
print(f'type(f) and values is={f}')


ff=True+True
fg=True+False
print(f' {ff}  and {fg}')

df=233+2j
fg=True+23j

print(f' {df} and {fg}')

print('\n')

tp=(12,2,2,3,3)
tp1=('this','new','demo',('text','fstring'))

print(tp[2])
print(tp1[3])
print('=============================================')


a=1222.233
b=float(a)
c=int(a)
d=int(b)
print(f'b {b} c={a} d={d}')

str1='hello'

lt=list(str1)
st=set(str1)
#st[1]='e'
tp=tuple(str1)
tp[0]='h'
print(f' list {lt} , set {st} , tuple {tp}')