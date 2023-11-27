#kid = 3
#adult = 10 
#tickets = 13
#tickets = tickets + adult + kid
#print(tickets * adult + kid)
total_price = 0 
i = 0
while i < 13:
    age = int(input())
    if age < 13:
        total_price += 0
    else: 
        total_price+=25
    i += 1
print(total_price)