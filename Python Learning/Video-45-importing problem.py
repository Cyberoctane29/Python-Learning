#when we have made a py file with a function welcome(),(refere file welcome) and in the file if the we have called the welcome function.
#so the problem occurs when we import this file into another py file and the welcome() function is immediately called and its content is printed
#which isnt something which is intended to happen

# import welcome as w

#we see the welcome function's content is printed even if we havent called the imported file's function it still considers the call in the
#imported file's content rather than only considering the current file's content

# w.welcome()
#we see its printing it twice

#so to tackle this

# now after including if __name__=="__main__": in welcome file and including the call in the if block

import welcome as w

#the problem is solved
#now no unintended printing of the result of the call in welcome file happening while running the importingProblem file

# w.welcome()

#works as intended

# print(__name__)

# if __name__=="__main__": if true then it means it is being ran from this file thats why we are running welcome()