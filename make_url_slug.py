title = input()

# TODO: keep only letters, digits and spaces, lowercase them,
# and join the words with single hyphens.

slug = ""

for ch in title:
    if ch.isalnum() or ch.isspace():
       slug += ch.lower()
slug = "-".join(slug.split())
print(slug)
