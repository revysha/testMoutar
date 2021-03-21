def palindromeNumbers(list_a):  
  
    c = 0
      # loop till list is not empty  
    for i in list_a:              
          # Find reverse of current number  
        t = i  
        rev = 0
        while t > 0:  
            rev = rev * 10 + t % 10
            t = t // 10
        # compare rev with the current number  
        if rev == i:
            print (i)  
            c = c + 1
    print("There is",c,"integer")
    print("Total palindrome: ", c ) 
    print();

# Driver code  
def main():  
    
    print("list_a")
    list_a = [808,809,102,212]  
    palindromeNumbers(list_a)  
    
    print("list_b")
    list_b = [908,809,122,102]  
    palindromeNumbers(list_b)                      
  
if __name__=="__main__":  
    main()             # main function call