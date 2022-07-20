def tribonacci(n):

        if n==0:
           return 0
        if n==1 or n==2:
            return 1
        else:
            return tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)
       

print(tribonacci(int(input('indique el tn a encontrar'))))
# print('indique el Tn a encontrar')
# x=input(int())
# print(tribonacci(x))
