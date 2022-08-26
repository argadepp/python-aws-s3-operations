

# with open('temp.txt' , mode='w') as  f :
#     f.write('Temp File Created')
# myName = 'Pratik'
# if myName != 'Pratik':
#     print('Hello Pratik')
# else:
#         print('Pratik is not there !! ')


# from traceback import print_last


# myList = [(1,2),(3,4),(4,5)]

# for (i,j) in myList:
#     print(i,j)


# num_List = [10,20,1,11,13,432]

# print(min(num_List))


# from random import randint
# inp = input('what is last')
# inp = int(inp)
# print(randint(1, inp))

# myLb = 'kljhhfuiiuo'
# if 'k' in myLb:
#     print(myLb)
# y= 'X' in [1213,543]
# print( y ) 


# d = {'m1':423434 , 'm3':1}

# print ( 1 in d.values())


# myList = [ x for x in range(0, 17) if x%2 == 0 ]
# print(myList)

# for i in myList:
#     print(2**i )

# def pypart(n):
     
#     # outer loop to handle number of rows
#     # n in this case
#     for i in range(0, n):
     
#         # inner loop to handle number of columns
#         # values changing acc. to outer loop
#         for j in range(0, i+1):
         
#             # printing stars
#             print("* ",end="")
      
#         # ending line after each row
#         print("\r")
 
# # Driver Code
# n = 5
# pypart(n)

from posixpath import split


# st = 'Print that char which is havinf s in the string suraj ssss'
# for s in st.split():
#    # print(s)
#     if (s[0] == 's'):
#         print(s)
# l= []
# ## Print odd number between 1 to 100
# for i in range(1,100):
#     if i%2 == 0:
        
#         print(i)
#         l.append(i)

# print('Total even numbers are =')
# print(l.sort())

# def addition(a):
    
#     return a%2 == 0

# for i in range(1,100):
#     if addition(i) == True:
#         print(i)


# names = ['Pratik' , 'Vishal' , 'Ashutosh']

# # print(list(map(lambda x : x[::-1],names)))

# numbers = [2,3,4,5,6]

# def squre(num):
#     return num**2

# for itm in map(squre  ,numbers):
#     print(itm)

####################################################################

# choice = 'WRONG'
# acceptable_range = range(1,10)
# within_range = False


# while choice.isdigit() == False or within_range==False :

#  choice = input('Enter the number between 1 to 10:')

#  if choice.isdigit() == False:
#    print('Sorry this is not digit')
#  if choice.isdigit() == True:
#      if int(choice) in acceptable_range:
#          within_range = True
#      else:
#          within_range = False
#          print('Sorry Boss input is not in range')


################# OOPS ################

# class Dog():
#   species = 'mamels'
#   def __init__(self , name , bread ):
#     self.name = name 
#     self.bread = bread

# myDog = Dog(bread='Bread' , name='Dog')

# print(myDog.species)
      

