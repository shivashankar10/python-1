def balaji():
    return "This is my bank balance"
test_dict = {"fname":balaji,"age":50,"address":"sales"}
print(" the original dictionary is :"+str(test_dict))
res = test_dict['fname']()
print("the required call result:"+str(res))