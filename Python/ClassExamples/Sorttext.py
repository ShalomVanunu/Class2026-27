
list_words = ['the', 'division', 'has', 'created', 'a', 'two-speed', 'path', 'out', 'of', 'the']
list_numers  = [ 45,66,1,100,55,23,77,96,23]

# Sort that dont change the original values
print(sorted(list_words))
print(list_words)
print(sorted(list_numers))
print(list_numers)


# Sort that  change the original values
print(list_words)
list_words.sort(reverse=True)
print(list_words)
print(list_numers)
list_numers.sort()
print(list_numers[::])
for even in list_numers:
    if even %2 == 0:
        print(f"number {even} is eevn")
