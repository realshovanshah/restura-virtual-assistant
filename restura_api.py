class ResturaApi:

    all_data = {
                'drinks': ['Mocha', 'Beer', 'Coke'],
                'breakfast': ['Toast', 'Oats', 'Omelette', 'Pancake'],
                'cake': ['Black Forest', 'Fudge Cake', 'Cheesecake'],
                'food':['Pizza', 'Choupsey', 'Sphagetti','Burger', 'Parmesan']
            }

    items= [item for items in all_data.values() for item in items]
    categories = list(all_data.keys())
    orders = []
    
    # @classmethod
    # def get_items(cls):
    #     return cls.items

    # @staticmethod
    # def get_categories(cls):
    #     return cls.categories

    @staticmethod
    def add_order(items):
        global orders
        orders.add(items)

    @staticmethod
    def get_orders():
        return orders
