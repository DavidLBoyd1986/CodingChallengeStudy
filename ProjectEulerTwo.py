
fib_list = [1, 2]
while True:
    new_value = fib_list[-1] + fib_list[-2]
    if new_value > 4000000:
        break
    fib_list.append(new_value)
print(fib_list)
answer = 0
for i in fib_list:
    if i % 2 == 0:
        answer += i
print(answer)
