#Student ID: 1201201010
#Student Name: Yong Khye Shern

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\t          DATA ENTRY                 ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def get_bonus(u,s):
    if (u > 1000):
        bonus = s*20/100
    elif(u > 500 and u <= 1000):
        bonus = s*10/100
    return bonus
    
def get_nett_salary(b,s):
    nett=b+s
    return nett

def display(id,s,u,b,ns):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\t        SALARY SLIP                       ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Staff ID                : ",id)
    print("Staff salary            :  RM {:.2f}".format (s))
    print("Units sold              : ",units)
    print("Bonus                   :  RM {:.2f}".format (b))
    print("Nett Salary             :  RM {:.2f}".format (ns))


staffid = int(input("Enter staff id          : "))
salary = float(input("Enter staff salary      : RM "))
units = int(input("Enter total units sold  : "))

bonus=get_bonus(units,salary)
nettsalary=get_nett_salary(bonus,salary)
display(staffid,salary,units,bonus,nettsalary)

