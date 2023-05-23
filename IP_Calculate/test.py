test_list = ["kim", "kim", "kim", "kim", "park", "lee", "ryu", "yang", "jeon"]
result_list = []

for i in test_list:
    temp = i.replace("kim", "ha")
    result_list.append(temp)
    
print(result_list)