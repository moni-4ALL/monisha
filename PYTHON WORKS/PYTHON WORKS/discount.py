def calculate_discount(member, coupon, purchase):

    is_member = membership.lower() == 'yes'
    has_coupon = coupon.lower() == 'yes'

 

    if has_coupon and purchase  > 10000:
       if 10000 < purchase <= 25000 and is_member :
           print("the discount is 5%")
           
    else:
        print("no discount")
        
    if is_member  and 1000 >= purchase <= 25000:
        if 25000 >= purchase  <=50000:
           print("the discount is 7%")
         
    else:
        print("no discount")
        
    if is_member  and  25000 >= purchase  <=100000:
        if 50000>= purchase  <=100000 and coupon:
            print("the discount is 10%")
           
    else:
        print("no discount")
        


membership=input("enter the membership  :type yes or no")
coupon=input("enter the coupon :type yes or no")
purchase=input("enter the purchase:")
        
calculate_discount(membership,coupon,purchase)