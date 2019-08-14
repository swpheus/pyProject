class Account:
    num_accounts = 0

    def __init__(self, name):
        self.name = name
        Account.num_accounts += 1

    def __del__(self):
        Account.num_accounts -= 1


woo = Account("woo")
lee = Account("lee")
woo.__del__()

print(woo.num_accounts)
# class BusinessCard:
#
#     def __init__(self, name, email, addr):
#         self.name = name
#         self.email = email
#         self.addr = addr
#
#     def print_info(self):
#         print("-------------------")
#         print("Name", self.name)
#         print("Email", self.email)
#         print("Adress", self.addr)
#         print("-------------------")
#         return ""
#
#
# card1 = BusinessCard("우성우", "swpheus1@gmail.com", '서울시')
# print(card1.print_info)
# apart = [[101, 102, 103, 104], [201, 202, 203, 204], [301, 302, 303, 304], [401, 402, 403, 404]]
# for floor in apart:
#     for room in floor:
#         print(room, "우유배달을 하였습니다.")
