a=0
n=int(input('Nhập số N cần kiểm tra:'))

if n < 2:
  print(n,'không phải là một số nguyên tố.')
else:
  for i in range(n):
    if n%(i+1)==0:
      a=a+1
  if a == 2:
    print(n,'là một số nguyên tố.')
  else:
    print(n,'không phải là một số nguyên tố.')