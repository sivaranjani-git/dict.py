my_tuple_1=(7,8,0,3,45,3,2,22,4)

print ("The tuple is : ")
print(my_tuple_1)

my_dict ={"Hey": 11,"there": 31,"jane":23}

print("The dictionary is :")
print(my_dict)

my_tuple_1 =list(my_tuple_1)
my_tuple_1 . append(my_dict)
my_tuple_1 =tuple(my_tuple_1)
print("The tuple after adding the dictionary elements is :")
print (my_tuple_1)
