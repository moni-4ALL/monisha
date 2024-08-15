att=int(input("enter the percent:"))
cgpa=float(input("enter the cgpa:"))
bl=int(input("enter the bl:"))
hoa=int(input("enter the hoa:"))
if (80 <= att <= 100 ) and (cgpa>=7.5) and (bl<=2):
    if (hoa<5):
          
        if(cgpa>6.5):
          print("you are eligible")
    else:
       print("you are not eligible")
    
elif (att>=70 and hoa==0 and bl<2):
  print("you are eligible")
else:
    print("you are not  eligible")