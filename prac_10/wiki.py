import wikipedia

title = input("Please enter a page title or search phrase")
page = wikipedia.page(title)
print(page.title)
print(page.summary)
print(page.url)

while title != "":
    title = input("Please enter a page title or search phrase")
    page = wikipedia.page(title)
    print(page.title)
    print(page.summary)
    print(page.url)