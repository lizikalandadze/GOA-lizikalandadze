# 5) შექმენით user_password ცვლადი და მასში შეინახეთ input. სანამ user_password ტოლი არ იქნება "12345678"-ის, მაქამდე შეეკითხეთ მომხმარებელს თავიდან პაროლი და შეინახეთ user_password ცვლადში
user_password = ""
while user_password != "12345678":
    user_password= input("Enter your passworld:")

print("password is correct")