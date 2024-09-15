# bmi = 體重 / ((身高/100)**2)
user_weight = float(input("請輸入您的體重(kg): "))
user_height = float(input("請輸入您的身高(m): "))
user_bmi = user_weight / (user_height / 100) ** 2
# print("您的BMI值為: " + str(user_bmi))
# print("您的BMI值為:%.2f" % (user_bmi))
# print("您的BMI值為: {:.2f}".format(user_bmi))
print(f"您的BMI值為: {user_bmi:.2f}")
