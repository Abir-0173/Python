# Method Overriding
class user:

    def __init__(self, user_name, total_purchase):
        self.name = user_name
        self.total_purchase = total_purchase


    def get_shipping_cost(self):
        if self.total_purchase > 1000:
            return 40
        return 60


class premium_user(user):

    def get_shipping_cost(self):
        if self.total_purchase > 2000:
            return 100
        return 20

    def get_shipping_cost(self):
        return 0

premiumUser = premium_user("Abir", 2000)
normal_user = user("test user", 1000)

print(premiumUser.get_shipping_cost())
print(normal_user.get_shipping_cost())