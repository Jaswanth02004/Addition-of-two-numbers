# Addition of two numbers.
def addition(First_num,Second_num):
  return f"Addition of given Two Number's is: {First_num + Second_num}"
First_num,Second_num = map(int,input("Enter two numbers to add").split())
print(addition(First_num,Second_num))
