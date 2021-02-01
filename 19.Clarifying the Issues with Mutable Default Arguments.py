# Best Practices:
# 🧠 def func(arg, list=None):

def add_employee(emp, emp_list=[]):
    emp_list.append(emp)
    print(emp_list)

# Set the default list to None if no data input

# NOTE: this is NOT an "if-else" statement, it is ONLY a pre-requisite
# if只是作为进行后序步骤的先决条件，而不是所谓的if else 二选一的判断结果！
# 🧭 重点在于提供选择权，通过每次设置为None，可以选择每次重建新的list，或是在既有list上增加！


def add_employee_fixed(emp, emp_list=None):
    # If there is NO input -> set every time to a new empty list
    if emp_list is None:
        emp_list = []

    emp_list.append(emp)
    print(emp_list)


emps = ['John', 'Jane']


add_employee('Corey')
add_employee('Jason')
add_employee('James')
print()

add_employee_fixed('Corey')
add_employee_fixed('Jason')
add_employee_fixed('James')
print()

add_employee_fixed('Corey', emps)
add_employee_fixed('Jason', emps)
add_employee_fixed('James', emps)
print()
