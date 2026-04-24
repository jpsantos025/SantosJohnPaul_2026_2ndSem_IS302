class Product:
    def __init__(self, jps_product_name, jps_product_price, jps_stock_count):
        self.__jps_product_name = jps_product_name
        self.__jps_product_price = jps_product_price
        self.__jps_stock_count = jps_stock_count

    def get_product_info(self):
        print("Product:", self.__jps_product_name)
        print("Price:", self.__jps_product_price)
        print("Quantity:", self.__jps_stock_count)

    def update_quantity(self, jps_new_stock):
        if jps_new_stock >= 0:
            self.__jps_stock_count = jps_new_stock

    def update_price(self, jps_new_price):
        if jps_new_price > 0:
            self.__jps_product_price = jps_new_price


# example usage
jps_item1 = Product("Laptop", 45000, 10)

jps_item1.get_product_info()

#JohnPaulSantos