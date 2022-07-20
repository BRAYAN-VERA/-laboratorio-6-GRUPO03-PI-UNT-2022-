def tribonacci(n):

        if n==1:
           return 0
        if n==2 or n==3:
            return 1
        else:
            return tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)
       

print(tribonacci(int(input('indique el tn a encontrar: '))))
# print('indique el Tn a encontrar')
# x=input(int())
# print(tribonacci(x))
