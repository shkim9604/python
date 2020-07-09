print("hello python")
print()
print("hello python")
#separator 옵션 사용
print('T','E','S','T',sep='')
print('2020','06','02',sep='-')
print("niceman","google.com",sep="@")

#end 옵션 사용
print("welcom to",end='')
print("the black parade",end='')
print("piano notes")
print("test")

#format 사용 [],{},()
print('{} and {}'.format('you','me'))
print('{0} and {1} and {0}'.format('you','me'))
print('{a} are {b}'.format(a='you',b='me'))

# %s:문자 %d: 정수 %f:실수
print("%s's favorite number is %d "%("eunki",7))
print("TEST1: %5d, price: %4.2f"%(776,6534.123))
print("TEST1: {0: 5d}, price:{1: 4.2f}".format(776,6534.123))
print("TEST1: {a: 5d}, price:{b: 4.2f}".format(a=776, b=6534.123))

print("'you'")