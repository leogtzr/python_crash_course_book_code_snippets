for n in range(1, 11):
    if n % 2 == 0:
        print(n)

print("sep...............")
even_nums = list(filter(lambda x: x % 2 == 0, list(range(1, 11))))
print(even_nums)

# Using list comprehension:
even_nums2 = [n for n in list(range(1, 11)) if n % 2 == 0]
print(even_nums2)
