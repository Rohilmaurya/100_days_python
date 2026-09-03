import random

# --- CONFIGURATION & GAME DATA ---
PLANETS = ["Zorgon-9", "Xylos Prime", "Nova Terra"]
ITEMS = {"Dark Matter": 150, "Space Spice": 40, "Plasma Cells": 85}

# --- FUNCTIONS ---

def generate_market_fluctuations():
    """Simulates shifting prices on different planets.
    Returns a dictionary of current prices with random modifiers.
    """
    current_market = {}
    for item, base_price in ITEMS.items():
        # Prices can fluctuate up or down by up to 40%
        modifier = random.uniform(0.6, 1.4)
        current_market[item] = round(base_price * modifier, 2)
    return current_market

def travel(current_planet):
    """Handles movement between locations using a robust input loop."""
    print("\nAvailable destinations:")
    destinations = [p for p in PLANETS if p != current_planet]
    
    for index, planet in enumerate(destinations, 1):
        print(f"{index}. {planet}")
        
    while True:
        try:
            choice = int(input("Enter destination number: "))
            if 1 <= choice <= len(destinations):
                new_planet = destinations[choice - 1]
                print(f"\nHyperspace jump successful! Welcome to {new_planet}.")
                return new_planet
            print("Invalid coordinates. Choose a valid destination.")
        except ValueError:
            print("Please enter a numeric choice.")

def trade_item(cargo, credits, market, action):
    """Handles both buying and selling dynamics by mutating inventory data."""
    print("\nCurrent Market Prices:")
    for item, price in market.items():
        print(f"- {item}: {price} credits (You hold: {cargo.get(item, 0)})")
        
    item_choice = input(f"What do you want to {action}? ").title()
    if item_choice not in market:
        print("That commodity does not exist here.")
        return credits

    price = market[item_choice]

    if action == "buy":
        if credits >= price:
            credits -= price
            cargo[item_choice] = cargo.get(item_choice, 0) + 1
            print(f"Bought 1 {item_choice} for {price} credits.")
        else:
            print("Insufficient credits for this transaction.")
            
    elif action == "sell":
        if cargo.get(item_choice, 0) > 0:
            credits += price
            cargo[item_choice] -= 1
            print(f"Sold 1 {item_choice} for {price} credits.")
        else:
            print("You do not have any of this item in your cargo bay.")
            
    return credits

# --- MAIN GAME LOOP ---

def main():
    # Initializing multi-layered state variables
    player_credits = 500.00
    player_cargo = {"Dark Matter": 0, "Space Spice": 0, "Plasma Cells": 0}
    current_location = "Nova Terra"
    local_market = generate_market_fluctuations()
    
    days_left = 10

    print("=== WELCOME TO GALACTIC TRADER ===")
    print("Goal: Maximize profit across the stars in 10 hyperspace jumps.")

    # The conditional while loop handles resource depreciation over time
    while days_left > 0:
        print(f"\n=====================================")
        print(f"LOCATION: {current_location} | JUMPS REMAINING: {days_left}")
        print(f"NET WORTH: {player_credits:.2f} credits")
        print(f"=====================================")
        
        print("1. View Cargo Bay")
        print("2. Buy Commodities")
        print("3. Sell Commodities")
        print("4. Jump to a new planet (Refreshes market prices & costs 1 jump)")
        print("5. Retire early")
        
        action = input("Select an action (1-5): ")

        if action == "1":
            print("\n--- Cargo Inventory ---")
            for item, qty in player_cargo.items():
                print(f"{item}: {qty}")
                
        elif action == "2":
            player_credits = trade_item(player_cargo, player_credits, local_market, "buy")
            
        elif action == "3":
            player_credits = trade_item(player_cargo, player_credits, local_market, "sell")
            
        elif action == "4":
            current_location = travel(current_location)
            local_market = generate_market_fluctuations() # Prices shift dynamically on jump
            days_left -= 1
            
        elif action == "5":
            print("\nEnding your trading career early.")
            break
        else:
            print("Invalid system input. Select a standard command.")

    print(f"\nGAME OVER. Final liquidation value: {player_credits:.2f} credits.")

# Standard entry point execution
if __name__ == "__main__":
    main()
