string_list=input()
digit_list=[]
for i in string_list:
    if i.isdigit():
        digit_list.append(int(i))
print(sum(digit_list))
print(min(digit_list))
print(max(digit_list))

#  Input:       
#  C0d1n8
#  output:
#     9
#     0
#     8
