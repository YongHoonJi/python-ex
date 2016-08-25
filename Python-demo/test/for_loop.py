#for loop

shopping_list = ['nice shoe', 'apple', 'bear', 'soju']

for item in shopping_list:
    print(item)

#nested loop
todo_list = [
    ['cleaning room', 'polishing floor'],
    ['shopping', 'errand'],
    ['watchging movie', 'meeting my parent']
    ]

count = 1
for sublist in todo_list:
    if(count == 2):
        print('#sublist below')
        for todo in sublist:
            print(todo)
    count = count+1
        
