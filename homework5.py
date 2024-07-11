immutable_var= 1, 3 ,5 ,7,'title', 2.0
print(immutable_var)
#immutable_var[1]=1
#print(immutable_var)            # кортеж при создании неизменияем нельзя изменить добавить удалить элемент после создания кортежа
mutable_list=[3,5,1.2,'still']
print(mutable_list[2])
mutable_list[2]='cake'
print(mutable_list)
print(mutable_list[3])
print(mutable_list)
mutable_list[3]=9
print(mutable_list)

