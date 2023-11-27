#მომხმარებლის ნიშნებისგან გამოანგარიშება საშვალო არითმეტიკული და თუ ცხრაზე მეტი იქნება
#დაუპრინტეთ გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რისთვისაც შეალიე შენი ცხოვრების წლები
#თუ ეს იქნება 5ზე ნაკლები დაუპრინტე გილოცავ გაექეცი მატრიცას
#თუ იქნება 5 იდან 9 მდე დაუპრინტე YOU ARE MID
#თუ იქნება 10ზე მეტი ან 0ზე ნაკლები დაუპრინტე there is something wrong with you

user_salary1 = float(input("enter salary N1: "))
user_salary2 = float(input("enter salary N2: "))
user_salary3 = float(input("enter salary N3: "))
user_salary4 = float(input("enter salary N4: "))

avg_salary = (user_salary1 + user_salary2 + user_salary3 + user_salary4)

if avg_salary<=1000 and avg_salary>= 0:
    print("გილოცავ, მატრიცელო. შენი ხელფასია: " + str(avg_salary) + " შემოსულიყავი გოაში, მატრიცელო")
elif avg_salary<=10000 and avg_salary >= 1000:
    print("შენი ხელფასია: " + str(avg_salary) + " you mid")
elif avg_salary>=0 and avg_salary >= 10000:
    print("შენი ხელფასია: " + str(avg_salary) + " გოა-ში სწავლობდი?")