#პითონი: უნდა გააკეთოთ ბანკის სისტემა სადაც შეგეძლებათ თანხის შეტანა გამოტანა, აქაუნთის გაკეთება, აგრეთვე უნდა აკონტროლოთ თუ მომხმარებელი იმაზე მეტ თანხას გამოიტანს ვიდრე აქვს მაშინ არ გამოატანიოთ თანხა.
def banki(cash):
    cash = 0
    choose = input('Do u want to withdraw or deposit? ')
    if choose == 'Deposit':
        input_cash = int(input('Enter Deposit Cash: '))
        cash += input_cash
        print(cash)
    if choose == 'Withdraw':
        output_cash = int(input('Enter Withdraw Money: '))
    if cash < output_cash:
        print('You cant withdraw because on your account is ', cash - output_cash, 'lari')

print(banki(100))