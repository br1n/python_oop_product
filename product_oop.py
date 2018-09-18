class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax):
        return self.price * (1 + tax) 

    def return_product(self, reason):
        if reason.lower() == "defective":
            self.price = 0
            self.status = "defective"
        
        elif reason.lower() == "like new":
            self.status = "for sale"
        
        elif reason.lower() == "open box":
            self.status = "Used"
            self.price *= .8
        return self

    def display_info(self):
        print "Price: ${}".format(self.price)
        print "Item: {}".format(self.item_name)
        print "Weight: {}".format(self.weight)
        print "Brand: {}".format(self.brand)
        print "Status: {}".format(self.status)
        return self


product1 = Product(15, "air filter", "3LBS", "3M")
print "*" * 50
print product1.return_product("open box").display_info()
print "*" * 50
print product1.add_tax(.2)

product2 = Product(55, "RoboCop Boxset", "3LBS", "Orion")
print "*" * 50
print product2.return_product("like new").display_info()
print "*" * 50
print product2.add_tax(.08)

product3 = Product(128, "HardDrive", "2LBS", "ScanDisk")
print "*" * 50
print product3.sell().display_info()