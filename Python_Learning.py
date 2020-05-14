class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self, name):
        self.name = name


#Dog オブジェクト作成時に犬の飼い主としてPersonオブジェクトを渡す
mick = Person("Mick Jagger")
stan = Dog("Stanly", "Bulldog", mick)
print(stan.owner.name)