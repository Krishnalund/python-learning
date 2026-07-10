# Write a python function to remove a given word from a list and strip it at the same time.

list1=[" apple "," mango ","pineapple"," guava "]
def modifying_list(list1,word):
    list2=[]
    for item in list1:
        item=item.strip()
        if item!=word:
            list2.append(item)
    return list2

word=input('Enter word from the list: ').lower()
print(modifying_list(list1,word))