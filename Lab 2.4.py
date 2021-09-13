#Student ID: 1201201010
#Student Name: Yong Khye Shern

BC=1.5 #constant value, the value doesn't change, name in Capital letters
GC=5.6



print("Invoice for Fruits Purchase")
print("---------------------------------")
bananas=int (input("\nEnter the quantity (comb) of bananas bought: "))
grapes=int (input("Enter the amount (kg) of grapes bought: "))
tbanana=bananas*BC
tgrapes=grapes*GC
total=tbanana+tgrapes
print("\nItem\t\tQty\tPrice\tTotal")
print("Banana (combs)\t",bananas,"\tRM1.50\tRM {:.2f}".format(tbanana))
print("Grapes (kg)\t",grapes,"\tRM5.60\tRM {:.2f}".format(tgrapes))

print("\nTotal: RM {:.2f}".format(total))
