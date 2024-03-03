import typing


class Pizza:
    def __init__(self, name, topping1=None, topping2=None, topping3=None) -> None:
        self.name = name
        self.top1 = topping1
        self.top2 = topping2
        self.top3 = topping3
        self.serv_state = "Unserved"
        self.uid = 0

    def __str__(self):
        return f"{self.name}"


class PizzaCollection:
    def __init__(self):
        self.list_of_pizza = []
        PizzaCollection.UIcounter = 0

    def __add__(self, pizza):
        self.list_of_pizza.append(pizza)
        PizzaCollection.UIcounter += 1
        pizza.uid = PizzaCollection.UIcounter

    def remove(self, uid):
        for pizza in self.list_of_pizza:
            if pizza.uid == uid:
                self.list_of_pizza.remove(pizza)

    def update_serving_state(self, uid):
        for pizza in self.list_of_pizza:
            if pizza.uid == uid:
                pizza.serv_state = "Served"

    def remove_served(self):
        for pizza in self.list_of_pizza:
            if pizza.serv_state == "Served":
                self.list_of_pizza.remove(pizza)

    def __str__(self):
        str_to_return = ""
        for pizza in self.list_of_pizza:
            str_to_return += f"{pizza.name}\n"
        return str_to_return


"""Of mörg toppings
State sem er annað en served og unserved
Leitar af pizzu sem er ekki til
Serve pizzu sem er núþegar served.
Eyða pizzu sem er ekki til
"""

pizza = Pizza("Hawaii", "Skinka", "Ostur")
assert pizza.serv_state == "Served" or pizza.serv_state == "Unserved"
# print(pizza.uid)
pizza2 = Pizza("Margarita", "Skinka", "Sveppir")
print(pizza2)
pizza3 = Pizza("Eih", "Ostur", "Skinka", "Pepperoni")
collection = PizzaCollection()
collection.__add__(pizza)
collection.__add__(pizza2)
collection.__add__(pizza3)
print(pizza2.uid)
collection.update_serving_state(2)
print(pizza2.serv_state)
collection.remove_served()
print(collection)

# x.uid

# assert pizza.serv_state == "Unserved"
assert pizza.uid == 1
assert pizza2.uid == 2
assert pizza3.uid == 3
assert pizza.serv_state == "Unserved"



# Gæti slegið inn ógild götuheiti og heiti á hverfum
# Gæti leitað eftir götu og hún er ekki skráð.


class LogEntries:
    def __init__(self):
        pass

    # def __add__(self, )
