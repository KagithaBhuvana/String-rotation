def is_same_str(str1,str2):
    flag=0
    for i in range(len(str1)):
        if str1==str2:
            flag=1
            rotation_n=i
            break
        else:
            str2=str2[1:]+str2[0]
    if flag==1:
        print(rotation_n)
    else:
        print("No Match")
    

str1=input()
str2=input()
is_same_str(str1,str2)
