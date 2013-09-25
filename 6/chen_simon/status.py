def mycalc():
    ans = 0;
    num1 = 0;
    num2 = 0;
    s1 = raw_input("Input your first number:");
    s2 = raw_input("Input your second number:");
    try:
        num1 = int(s1);
    except ValueError:
        print("Illegal Value");
        return;
    try:
        num2 = int(s2);
    except ValueError:
        print("Illegal Value");
        return;
    sign = raw_input("Input your oprend:");
    if num2 == 0:
        print "Can't divide by zero"
        return;
    if sign == "+":
        ans = num1 + num2;
    elif sign == "-":
        ans = num1 - num2;
    elif sign == "x":
        ans = num1 * num2;
    elif sign == "/":
        ans = nume1 / num2;
    else:
        print("Illegal Value.");
    print(ans);
    
mycalc();
