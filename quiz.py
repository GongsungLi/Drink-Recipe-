import random

# Full recipes dictionary from your sheet
recipes = {
    # TEA BASIC
    "Cold Tea Basic": ["200 Tea", "+S/ Syrup", "+100 HW"],
    "Hot Tea Basic": ["200 Tea", "+S/ Syrup", "+200 HW"],

    # MILK TEA BASIC
    "Cold Milk Tea Basic": ["S", "3 creamer", "HW up to 100", "+250 Tea"],
    "Hot Milk Tea Basic": ["S", "3 creamer", "+250 Tea"],

    # TEA (C)
    "Mango Tea": ["Mango 40", "Passion 40", "+25% S"],
    "Mad Hatter GT": ["Peppermint 20", "Lemon 20", "+25% S"],
    "Lemon Honey GT": ["40 Honey", "4 slices Lemon", "+25% S", "100 HW"],
    "HK Lemon Tea": ["S", "4 slices lemon", "up to 350 water", "150 HK tea"],

    # MILK TEA (H/C)
    "HK Milk Tea Cold": ["40 Conden", "60 Evapo", "300 Tea", "COLD 60 conden"],
    "HK Milk Tea Hot": ["40 Conden", "60 Evapo", "150 Tea", "150 coffee", "COLD 60 conden"],
    "Thai MT": ["300 T", "100 HH", "Syrup 40", "MT No S"],
    "Taro Milk": ["TARO to 250 HW"],
    "Caramel MT": ["3 creamer", "HW", "Caramel 60 +25% S", "200 BT"],

    # YAKULT 40
    "Yakult Rose Lemon": ["Rose 25", "Lemon 15", "Yakult 40", "CW up to 400"],
    "Yakult Peach": ["Peach 60", "Yakult 40", "CW to 300", "butterfly pea"],

    # SLUSH
    "Slush Basic": ["All syrup 70", "No S", "+50 HW"],
    "Shaved Ice Red Bean": [
        "White Rabbit base", "4 creamer", "50 HW", "80 HH", "blend"
    ],

    # COFFEE
    "Iced Milk Coffee": ["150 Hot Coffee", "inc S", "4 creamer", "250 Cold Coffee"],
    "Iced Black Coffee": ["150 Hot Coffee", "inc S", "250 Cold Coffee"]
}

score = 0
rounds = 5  # number of questions per game

print("=== Drink Recipe Quiz ===")
print("Type the components separated by commas.\n")

for _ in range(rounds):
    drink = random.choice(list(recipes.keys()))
    print(f"Drink: {drink}")
    answer = input("Enter the components: ").strip()
    answer_list = [a.strip() for a in answer.split(",")]

    if set(answer_list) == set(recipes[drink]):
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Wrong.")
        print(f"Correct components: {', '.join(recipes[drink])}\n")

print(f"Game over! Your score: {score}/{rounds}")
