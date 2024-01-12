#პითონი: უნდა გააკეთოთ ბანკის სისტემა სადაც შეგეძლებათ თანხის შეტანა გამოტანა, აქაუნთის გაკეთება, აგრეთვე უნდა აკონტროლოთ თუ მომხმარებელი იმაზე მეტ თანხას გამოიტანს ვიდრე აქვს მაშინ არ გამოატანიოთ თანხა.
def Bank(Cash):
    Cash = 0
    Choice = "Do You Want To Withdraw Or Deposit?"
    if Choice == "Deposit":
        input_Cash = int(input("How Much money Do you Want To Deposit?"))
        Cash += input_Cash
        print(Cash)
    if Choice == "Withdraw":
        Output_Cash = int(input("How much money Do you Want To Withdraw?"))
    if Cash < Output_Cash:
        print("You Cant Withdraw On Your Account is", Cash - Output_Cash, "lari")

print(Bank(100))










