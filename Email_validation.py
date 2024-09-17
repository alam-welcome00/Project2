input_mail = input("Enter your Email =")
k,j,d = 0,0,0

if len(input_mail) >= 6:
    if ("@" in input_mail) and (input_mail.count("@") == 1):
        if (input_mail[-4] == ".") ^ (input_mail[-3] == "."):
            if input_mail[0].isalpha():
                for i in input_mail:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i.isupper():
                         j = 1
                    elif i.isdigit():
                        continue
                    elif i == "@" or i == "." or i == "_":
                        continue
                    else:
                        d = 1
                if (k == 1) or (j == 1) or (d == 1):
                    print("Your Email contain some space or any upper case")
                else:
                    print("Valid")
            else:
                print("First letter should be an lower case alphabet")
        else:
            print("Position of . is not correct")
    else:
        print("Your email is not contain or contain more @")
else:
    print("Your Email is too short")
    
