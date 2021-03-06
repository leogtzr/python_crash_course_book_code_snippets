favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"name: {name}, lang: {language}")

print("#### Looping thru values:")
for lang in favorite_languages:
    print(lang)

print("#### Looping thru keys:")
for name in favorite_languages.keys():
    print(name)

# Starting from python 3.7, looping through a dictionary returns the items in the same order they were inserted.

names_upper = [name.upper() for name in favorite_languages.keys()]
print(names_upper)
