name = 'Krishna'
full_name = "Krishna Ruparelia"
greeting = "Hello, {}"
with_name = greeting.format(name)
with_name_two = greeting.format(full_name)
print(with_name)
print(with_name_two)

longer_phrase = "Hello , {}. Today is {}"
longer_phrase_with_name = longer_phrase.format(full_name, "Monday")
print(longer_phrase_with_name)