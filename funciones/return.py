def sumnum(a:int, b:int) -> int :
     return a+b if (a > 0 and b > 0) else 0

print(f' result : {sumnum(5,4)}')


#default values
def sumnum(a:int = 1, b:int =1) -> int:
     return a+b if (a > 0 and b > 0) else 0

print(f' result : {sumnum()}')



#var arguments
def listnames(*names) -> any:
     for name in names :
         print(f' name : {name}')

listnames("cecilia", "dickens")


#key-values arguments
def listdictionary(**keyworks) -> any:
     for key,value in keyworks.items() :
         print(f' {key} : {value}')

listdictionary(PK='Primary Key')