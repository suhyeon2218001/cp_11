class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate(self, quantity):
        total_price = self.price * quantity
        print("{} {}잔의 총 가격은 {}원 입니다.".format(self.name, quantity, total_price))

# 음료 객체 생성
coffee = Beverage("커피", 3000)
green_tea = Beverage("녹차", 2500)
ice_tea = Beverage("아이스티", 3000)

# 첫 번째 사용자 입력 받기
selected_beverage = input("주문할 음료를 선택하세요 (커피, 녹차, 아이스티): ")

# 선택한 음료에 따라 객체 선택 및 calculate 함수 호출
if selected_beverage == "커피":
    coffee_quantity = int(input("커피의 수량을 입력하세요: "))
    coffee.calculate(coffee_quantity)
elif selected_beverage == "녹차":
    green_tea_quantity = int(input("녹차의 수량을 입력하세요: "))
    green_tea.calculate(green_tea_quantity)
elif selected_beverage == "아이스티":
    ice_tea_quantity = int(input("아이스티의 수량을 입력하세요: "))
    ice_tea.calculate(ice_tea_quantity)
else:
    print("잘못된 음료를 선택하셨습니다.")
