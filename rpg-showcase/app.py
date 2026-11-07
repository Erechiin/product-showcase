from flask import Flask, render_template

from models.product import DigitalProduct, PhysicalProduct

app = Flask(__name__)

# CUSTOMIZE HERE: choose a theme and introduce your showcase.
SHOWCASE_NAME = "MineShop — Village Market"
SHOWCASE_DESCRIPTION = "Explore the Overworld and Nether trade routes! Visit each Villager's workshop and barter with Emeralds and Gold Ingots."
AUTHOR_NAME = "Master Villager"

VILLAGERS = {
    "armorer": {
        "id": "armorer",
        "name": "Blacksmith Gorak",
        "role": "Master Armorer & Toolsmith",
        "level": "Level 5 · Master (Emerald)",
        "workstation": "Anvil & Blast Furnace",
        "dimension": "overworld",
        "dimension_name": "Overworld",
        "currency_name": "Emeralds",
        "currency_short": "Em.",
        "currency_icon": "/static/images/Emerald_JE3_BE3.png",
        "icon": "⚒️",
        "avatar": "/static/images/ferreiro.png",
        "flip_avatar": True,
        "theme": "theme-armeiro",
        "quote": "I have forged blades, axes, and pickaxes since the first mine opened beneath the village. Whether you need to break Obsidian or survive the night hordes, you came to the right forge!",
        "specialty": "Melee weapons, mining pickaxes, and heavy armor",
    },
    "cleric": {
        "id": "cleric",
        "name": "Cleric Eldrin",
        "role": "Master Alchemist & Enchanter",
        "level": "Level 5 · Master (Emerald)",
        "workstation": "Brewing Stand & Enchanting Table",
        "dimension": "overworld",
        "dimension_name": "Overworld",
        "currency_name": "Emeralds",
        "currency_short": "Em.",
        "currency_icon": "/static/images/Emerald_JE3_BE3.png",
        "icon": "🧪",
        "avatar": "/static/images/Savanna_Cleric.png",
        "flip_avatar": True,
        "theme": "theme-alquimista",
        "quote": "High atop the village tower, I brew rare potions and prepare enchanted golden fruits to grant speed, regeneration, and arcane power to travelers.",
        "specialty": "Alchemical potions, golden apples, and mystic artifacts",
    },
    "nether_trader": {
        "id": "nether_trader",
        "name": "Trader Ignis (Piglin)",
        "role": "Bastion Bartering Master (Piglin)",
        "level": "Level 5 · Gold Master (Piglin)",
        "workstation": "Bastion Chest & Respawn Anchor",
        "dimension": "nether",
        "dimension_name": "Nether",
        "currency_name": "Gold Ingots",
        "currency_short": "Gold",
        "currency_icon": "/static/images/Gold_Ingot_JE4_BE2.png",
        "icon": "🔥",
        "avatar": "/static/images/piglincard.png",
        "flip_avatar": True,
        "theme": "theme-ignis",
        "quote": "Emeralds have no value here in the Nether! Bring your shiny Gold Ingots and I will barter them for Ender Pearls, Crying Obsidian, and pure Netherite!",
        "specialty": "Gold Ingot Bartering: Ender Pearls, Crying Obsidian, and Netherite",
    },
}

CATEGORIES = [
    {
        "id": "weapons",
        "name": "Weapons & Tools",
        "items": [
            {
                "id": 1,
                "name": "Iron Sword",
                "price": 8,
                "stack": 1,
                "damage": "+6 Attack Damage",
                "image": "Iron_Sword_JE2_BE2.png",
                "description": "Reliable blade forged on the village anvil for close-quarters combat.",
                "lore": "Suggested Enchantment: Sharpness III · Mending",
                "product_type": "physical",
                "delivery": "Blacksmith Gorak's Forge (Armorer)",
                "villager_id": "armorer",
                "dimension": "overworld",
            },
            {
                "id": 2,
                "name": "Diamond Pickaxe",
                "price": 24,
                "stack": 1,
                "durability": "1561 uses",
                "image": "Diamond_Pickaxe_JE3_BE3.png",
                "description": "High-durability mining tool capable of extracting Obsidian and rare ores.",
                "lore": "Suggested Enchantment: Efficiency IV · Fortune III",
                "product_type": "physical",
                "delivery": "Blacksmith Gorak's Forge (Toolsmith)",
                "villager_id": "armorer",
                "dimension": "overworld",
            },
            {
                "id": 7,
                "name": "Diamond Axe",
                "price": 20,
                "stack": 1,
                "damage": "+9 Attack / Fast Chopping",
                "image": "machadodiamante.png",
                "description": "Chops logs in seconds and disables enemy shields with heavy strikes.",
                "lore": "Suggested Enchantment: Efficiency V · Silk Touch",
                "product_type": "physical",
                "delivery": "Blacksmith Gorak's Forge (Weaponsmith)",
                "villager_id": "armorer",
                "dimension": "overworld",
            },
            {
                "id": 8,
                "name": "Iron Chestplate",
                "price": 18,
                "stack": 1,
                "durability": "240 uses (+6 Armor)",
                "image": "peitoralferro.png",
                "description": "Reinforced blast-furnace chest armor built to deflect arrows and blasts.",
                "lore": "Suggested Enchantment: Protection IV · Unbreaking III",
                "product_type": "physical",
                "delivery": "Blacksmith Gorak's Forge (Armorer)",
                "villager_id": "armorer",
                "dimension": "overworld",
            },
        ],
    },
    {
        "id": "blocks",
        "name": "Relics & Resources",
        "items": [
            {
                "id": 12,
                "name": "Ender Pearl",
                "price": 14,
                "stack": 16,
                "type": "Dimensional Teleport",
                "image": "Ender_Pearl_JE3_BE2.png",
                "description": "A favorite item in Piglin bartering! Allows instant teleportation when thrown.",
                "lore": "Essential for crafting Eyes of Ender and locating the End Portal.",
                "product_type": "physical",
                "delivery": "Bartering with Trader Ignis (Piglin)",
                "villager_id": "nether_trader",
                "dimension": "nether",
            },
            {
                "id": 13,
                "name": "Crying Obsidian",
                "price": 10,
                "stack": 64,
                "type": "Rare Bastion Block",
                "image": "Crying_Obsidian_JE1_BE1.png",
                "description": "Ancient obsidian that emits glowing purple particles, exclusive to Piglin trades.",
                "lore": "Used to craft Respawn Anchors in the Nether.",
                "product_type": "physical",
                "delivery": "Trader Ignis's Bastion (Piglin)",
                "villager_id": "nether_trader",
                "dimension": "nether",
            },
            {
                "id": 14,
                "name": "Netherite Ingot",
                "price": 36,
                "stack": 64,
                "type": "Legendary Metal (Lava Proof)",
                "image": "Netherite_Ingot_JE1_BE2.png",
                "description": "Smelted from 4 Netherite Scraps and 4 Gold Ingots inside Bastion treasure vaults.",
                "lore": "Upgrades any Diamond gear at the Smithing Table.",
                "product_type": "physical",
                "delivery": "Trader Ignis's Royal Vault (Piglin)",
                "villager_id": "nether_trader",
                "dimension": "nether",
            },
        ],
    },
    {
        "id": "alchemy",
        "name": "Potions & Consumables",
        "items": [
            {
                "id": 5,
                "name": "Potion of Swiftness II",
                "price": 12,
                "stack": 1,
                "duration": "1:30 min",
                "image": "Potion_of_Swiftness_JE3.png",
                "description": "Increases movement speed by +40% for fast biome exploration.",
                "lore": "Brewed with Nether Wart, Sugar, and Glowstone Dust.",
                "product_type": "digital",
                "delivery": "Cleric Eldrin's Tower (Alchemical Effect)",
                "villager_id": "cleric",
                "dimension": "overworld",
            },
            {
                "id": 6,
                "name": "Golden Apple",
                "price": 16,
                "stack": 64,
                "effect": "Regeneration II",
                "image": "Golden_Apple_JE2_BE2.png",
                "description": "Mystic fruit coated in 8 pure gold ingots that rapidly restores hearts.",
                "lore": "Grants Regeneration II (5s) and Absorption I (2:00 min).",
                "product_type": "digital",
                "delivery": "Cleric Eldrin's Altar (Mystic Blessing)",
                "villager_id": "cleric",
                "dimension": "overworld",
            },
            {
                "id": 11,
                "name": "Bottle o' Enchanting",
                "price": 10,
                "stack": 64,
                "effect": "+Enchanting XP",
                "image": "Bottle_o'_Enchanting_JE1_BE1.png",
                "description": "Shimmering bottle that releases experience orbs when shattered on the ground.",
                "lore": "Perfect for repairing Mending gear or unlocking enchantments.",
                "product_type": "digital",
                "delivery": "Cleric Eldrin's Tower (XP Orbs)",
                "villager_id": "cleric",
                "dimension": "overworld",
            },
        ],
    },
]


def _build_products(categories):
    built_products = []
    for category in categories:
        for item in category["items"]:
            if "damage" in item:
                stat_label, stat_value = "Damage", item["damage"]
            elif "durability" in item:
                stat_label, stat_value = "Durability", item["durability"]
            elif "type" in item:
                stat_label, stat_value = "Type", item["type"]
            elif "duration" in item:
                stat_label, stat_value = "Duration", item["duration"]
            else:
                stat_label, stat_value = "Effect", item.get("effect", "Special")

            v_id = item.get("villager_id", "armorer")
            villager_info = VILLAGERS.get(v_id, VILLAGERS["armorer"])

            common_kwargs = dict(
                item_id=item["id"],
                name=item["name"],
                description=item["description"],
                price=float(item["price"]),
                image=item["image"],
                category_id=category["id"],
                category_name=category["name"],
                stack=item["stack"],
                stat_label=stat_label,
                stat_value=stat_value,
                lore=item["lore"],
                villager_id=v_id,
                villager_name=villager_info["name"],
                villager_role=villager_info["role"],
                dimension=item.get("dimension", villager_info["dimension"]),
            )

            if item.get("product_type") == "digital":
                built_products.append(
                    DigitalProduct(
                        file_format=item["delivery"],
                        **common_kwargs,
                    )
                )
            else:
                built_products.append(
                    PhysicalProduct(
                        pickup_location=item["delivery"],
                        **common_kwargs,
                    )
                )
    return built_products


products = _build_products(CATEGORIES)


@app.route("/")
def index():
    return render_template(
        "index.html",
        showcase_name=SHOWCASE_NAME,
        showcase_description=SHOWCASE_DESCRIPTION,
        author_name=AUTHOR_NAME,
        products=products,
        categories=CATEGORIES,
        villagers=VILLAGERS,
    )
