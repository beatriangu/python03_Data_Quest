#!/usr/bin/env python3


def show_inventory(player_name: str, inventory: dict) -> tuple:
    print(f"=== {player_name}'s Inventory ===")

    total_value = 0
    item_count = 0
    categories = {}

    for item_name, item_data in inventory.items():
        category = item_data["category"]
        rarity = item_data["rarity"]
        quantity = item_data["quantity"]
        value = item_data["value"]

        item_total = quantity * value
        total_value += item_total
        item_count += quantity

        categories[category] = categories.get(category, 0) + quantity

        print(
            f"{item_name} ({category}, {rarity}): {quantity}x "
            f"@ {value} gold each = {item_total} gold"
        )

    print()
    print(f"Inventory value: {total_value} gold")
    print(f"Item count: {item_count} items")

    print(
        "Categories: "
        f"weapon({categories.get('weapon', 0)}), "
        f"consumable({categories.get('consumable', 0)}), "
        f"armor({categories.get('armor', 0)})"
    )
    print()

    return total_value, item_count


def transfer_potions(alice: dict, bob: dict, amount: int) -> None:
    print("=== Transaction: Alice gives Bob 2 potions ===")
    alice_potions = alice.get("potion", {}).get("quantity", 0)

    if alice_potions < amount:
        print("Transaction failed!")
        print()
        return

    alice["potion"]["quantity"] = alice_potions - amount

    bob_potions = bob.get("potion", {}).get("quantity", 0)
    if "potion" not in bob:
        bob["potion"] = {
            "category": "consumable",
            "rarity": "common",
            "quantity": 0,
            "value": 50,
        }
    bob["potion"]["quantity"] = bob_potions + amount

    print("Transaction successful!\n")

    print("=== Updated Inventories ===")
    print(f"Alice potions: {alice['potion']['quantity']}")
    print(f"Bob potions: {bob['potion']['quantity']}")
    print()


def inventory_value(inventory: dict) -> int:
    total = 0
    for item_data in inventory.values():
        total += item_data["quantity"] * item_data["value"]
    return total


def inventory_item_count(inventory: dict) -> int:
    count = 0
    for item_data in inventory.values():
        count += item_data["quantity"]
    return count


def rarest_items(players: dict) -> str:
    rare_items = []
    for inv in players.values():
        for item_name, item_data in inv.items():
            if item_data["rarity"] == "rare" and item_name not in rare_items:
                rare_items.append(item_name)
    return ", ".join(rare_items)


def main() -> None:
    print("=== Player Inventory System ===\n")

    alice = {
        "sword": {
            "category": "weapon",
            "rarity": "rare",
            "quantity": 1,
            "value": 500,
        },
        "potion": {
            "category": "consumable",
            "rarity": "common",
            "quantity": 5,
            "value": 50,
        },
        "shield": {
            "category": "armor",
            "rarity": "uncommon",
            "quantity": 1,
            "value": 200,
        },
    }

    bob = {
        "magic_ring": {
            "category": "accessory",
            "rarity": "rare",
            "quantity": 1,
            "value": 300,
        }
    }

    show_inventory("Alice", alice)

    transfer_potions(alice, bob, 2)

    print("=== Inventory Analytics ===")
    players = {"Alice": alice, "Bob": bob}

    alice_value = inventory_value(alice)
    bob_value = inventory_value(bob)

    if alice_value >= bob_value:
        print(f"Most valuable player: Alice ({alice_value} gold)")
    else:
        print(f"Most valuable player: Bob ({bob_value} gold)")

    alice_items = inventory_item_count(alice)
    bob_items = inventory_item_count(bob)

    if alice_items >= bob_items:
        print(f"Most items: Alice ({alice_items} items)")
    else:
        print(f"Most items: Bob ({bob_items} items)")

    print(f"Rarest items: {rarest_items(players)}")


if __name__ == "__main__":
    main()
