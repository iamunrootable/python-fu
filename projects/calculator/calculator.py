from replit import clear
import art
import operator

def calculator():
  print(art.logo)
  ops = {
      "+": operator.add, 
      "-": operator.sub,
      "*": operator.mul,
      "/": operator.truediv,
      "%": operator.mod,
      "^": operator.pow
    }
  
  def calc_input(num1, num2, operation):
    '''
    Takes a number and mathematical operation and returns the result.
    ''' 
    answer = (ops[op](num1,num2))
    return answer
  
  
  num1 = float(input("What's the first number?: "))
  
  for symbol in ops:
    print(symbol)
  should_continue = True
  
  while should_continue:
    op = input("Pick an operation: ")
    next_num = float(input("What's the next number?: "))
    result = calc_input(num1, next_num, op)
    print(f"{num1} {op} {next_num} = {result}")
    continue_calc = input(f"Type 'y' to continue calculating with {str(result)}, or type 'n' to start a new calculation: ").lower()
    if continue_calc == "y":
      num1 = result
    else:
      should_continue = False
      clear()
      calculator()

calculator()
    


  