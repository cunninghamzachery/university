# https://www.w3schools.com/python/ref_string_find.asp

# locate None
# locate who called it
# None now calls the index of that instead
# then that becomes the new target
# locate who called it...etc.
# repeat until? i guess until target is the head, because nobody called the head, so then that one
# that should be None

storage = [(11, 1), (32, 3), (56, None), (39, 2)]
head_index = 0

def reverse_linked_list(head_index, storage):
    reversed = [] 
    target = None
    while target != storage[head_index][1]:
        for key, value in storage:
            if value is target:
                reversed.append((key, (len(reversed) + 1)))
                target = storage.index((key, value))
    reversed.append((storage[head_index][0], None))
    return 0, reversed

print(reverse_linked_list(head_index, storage))

