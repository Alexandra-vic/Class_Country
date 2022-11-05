class Monkey:
    max_age = 12
    loves_bananas = True

    def climb(self):
	    print('I am climbing the tree') 

makaka = Monkey()
martyshka = Monkey()

print(f"My max age: {makaka.max_age} , I love bananas : it's {makaka.loves_bananas}")
makaka.climb()

print(f"My max age: {martyshka.max_age} , I love bananas : it's {martyshka.loves_bananas}")
martyshka.climb()