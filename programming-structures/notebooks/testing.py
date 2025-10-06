
# test (this is being way too picky with the errors)
# i get it now, we move based on where the node tells us to, not just iterating linearly
# additional test

storage = [(11, 1), (32, 3), (56, None), (39, 2)]
head_index = 0


result = []
index = head_index

while index is not None:
    value, next_index = storage[index]
    result.append(value)
    index = next_index

print(result)

new_storage = []
while result:
    new_storage.append(result.pop())


for i in range(0, (len(new_storage))):
    if i < (len(new_storage) - 1):
        new_storage[i] = (new_storage[i], (i + 1))
    else:
        new_storage[i] = (new_storage[i], None)

print(new_storage)




