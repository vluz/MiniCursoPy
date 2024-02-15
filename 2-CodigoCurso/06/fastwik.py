import wikipedia


wikipedia.set_lang("pt")
result = wikipedia.page(title="Barreiro")
print(result.content)