################### Scope ####################

enemies = 1
def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")



# Global scope
player_health = 10
def game():
    def drink_portion():
        # Local scope
        portion_strength = 2
        print(player_health)
    drink_portion()
print(player_health)

game()

# There is no block scope
game_level = 3
def create_enemy():
    enemies = ["Skelton", "Zombie", "Alien"]

    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)
create_enemy()