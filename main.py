a=0
n=int(input('Nhập số N cần kiểm tra: '))

if n < 2:
  print(n,'không phải là một số nguyên tố.')
else:
  for i in range(n):
    if n%(i+1)==0:
      so_chia_het=so_chia_het+1
  if so_chia_het == 2:
    print(n,' là một số nguyên tố.')
  else:
    print(n,' không phải là một số nguyên tố.')