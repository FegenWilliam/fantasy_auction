"""
Random generators for names, descriptions, and flavor text.
"""
import random


# NPC Name Generation
FIRST_NAMES = [
    "Aldric", "Beatrix", "Cornelius", "Delphine", "Edmund", "Fiona",
    "Gareth", "Helena", "Ignatius", "Jasmine", "Kristoff", "Lavinia",
    "Magnus", "Nora", "Octavius", "Penelope", "Quintus", "Rosalind",
    "Sebastian", "Thaddeus", "Ulrich", "Vivienne", "Wendell", "Xandra",
    "Yorick", "Zephyr", "Balthazar", "Celestia", "Darius", "Evangeline"
]

LAST_NAMES = [
    "Blackwood", "Silverstone", "Goldweaver", "Ironheart", "Stormwind",
    "Moonwhisper", "Shadowcrest", "Brightforge", "Darkwater", "Starfall",
    "Thornvale", "Ashenmoor", "Crimsonblade", "Frostwyn", "Emberlight",
    "Nightshade", "Sunhaven", "Ravenclaw", "Willowmere", "Stonehammer",
    "Mistwalker", "Firebrook", "Iceborn", "Tidecaller", "Windrunner"
]


def generate_npc_name():
    """Generate a random NPC name."""
    return f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"


# Item Name Generation
ITEM_PREFIXES = [
    "Ancient", "Cursed", "Blessed", "Forgotten", "Mysterious", "Ornate",
    "Rusty", "Golden", "Silver", "Bronze", "Crystal", "Enchanted",
    "Worn", "Pristine", "Tarnished", "Gleaming", "Dusty", "Radiant",
    "Dark", "Luminous", "Ethereal", "Mundane", "Exotic", "Common"
]

ITEM_TYPES = [
    "Amulet", "Ring", "Crown", "Chalice", "Scroll", "Tome", "Orb",
    "Staff", "Dagger", "Shield", "Helm", "Gauntlets", "Boots",
    "Cloak", "Mirror", "Hourglass", "Compass", "Locket", "Sword",
    "Bow", "Pendant", "Bracelet", "Scepter", "Idol", "Relic",
    "Coin", "Gemstone", "Mask", "Tapestry", "Vase", "Statue",
    "Lamp", "Box", "Key", "Map", "Journal", "Quill", "Tankard"
]

ITEM_SUFFIXES = [
    "of Power", "of Wisdom", "of Fortune", "of Misery", "of the Ancients",
    "of Eternal Night", "of Dawn", "of the Depths", "of the Peaks",
    "of Lost Kings", "of Forgotten Heroes", "of the Void", "of Light",
    "of Shadows", "of Time", "of Space", "of Dreams", "of Nightmares",
    "of Victory", "of Defeat", "of Glory", "of Shame", "of Wonder"
]


def generate_item_name(quality_tier):
    """Generate an item name based on quality tier."""
    if quality_tier == "garbage":
        # Garbage items tend to be mundane or worn
        prefix = random.choice(["Rusty", "Worn", "Broken", "Cracked", "Dusty", "Tarnished", "Old", "Mundane"])
        item_type = random.choice(ITEM_TYPES)
        if random.random() < 0.3:  # 30% chance of no suffix
            return f"{prefix} {item_type}"
        suffix = random.choice(["of Dubious Origin", "of Questionable Value", "of No Import", ""])
        return f"{prefix} {item_type} {suffix}".strip()

    elif quality_tier in ["common", "uncommon"]:
        # Common items have basic prefixes
        prefix = random.choice(ITEM_PREFIXES[:15])
        item_type = random.choice(ITEM_TYPES)
        if random.random() < 0.5 and quality_tier == "uncommon":
            suffix = random.choice(ITEM_SUFFIXES)
            return f"{prefix} {item_type} {suffix}"
        return f"{prefix} {item_type}"

    else:  # rare or relic
        # High quality items get the best prefixes and always have suffixes
        prefix = random.choice(["Ancient", "Legendary", "Mythical", "Divine", "Enchanted",
                               "Radiant", "Ethereal", "Celestial", "Pristine"])
        item_type = random.choice(ITEM_TYPES)
        suffix = random.choice(ITEM_SUFFIXES)
        return f"{prefix} {item_type} {suffix}"


# Flavor Text Generation
AUCTION_INTROS = [
    "Ladies and gentlemen, behold",
    "Step right up and feast your eyes upon",
    "Gathered from the far reaches, I present",
    "Direct from a mysterious estate, we have",
    "Unearthed from ancient vaults, witness",
    "Found in the collection of a deceased noble",
    "Recovered from a sunken ship, observe",
    "Salvaged from forgotten ruins, see",
    "Acquired through dubious means, I offer",
    "Procured at great expense, marvel at",
    "Fresh from a dragon's hoard, admire",
    "Liberated from a cursed tomb, gaze upon"
]

AUCTION_DESCRIPTIONS = [
    "Its surface gleams with an otherworldly sheen.",
    "Legend speaks of its incredible power.",
    "Scholars debate its true origin to this day.",
    "It radiates an aura of mystery and intrigue.",
    "Many have sought this piece throughout the ages.",
    "Its craftsmanship is truly remarkable... or so they say.",
    "One can feel its energy from across the room.",
    "It bears the marks of a thousand years.",
    "Some claim it brings fortune, others... misfortune.",
    "Its previous owner met a rather... unfortunate end.",
    "Experts are divided on its authenticity.",
    "It hums with barely contained magic.",
    "The weight of history rests upon it.",
    "It appears ordinary, yet feels extraordinary.",
    "Dark rumors surround this peculiar artifact.",
    "It was found clutched in a skeleton's grasp.",
    "Prophecy foretold its rediscovery.",
    "It defies all conventional explanation."
]

AUCTION_CLOSINGS = [
    "Who will claim this treasure?",
    "What secrets does it hold?",
    "Will you be its next owner?",
    "The bidding starts now!",
    "Let the auction begin!",
    "Who dares bid first?",
    "Fortune favors the bold!",
    "Make your fortune today!",
    "Don't let this opportunity pass!",
    "A once-in-a-lifetime chance!",
    "Bid wisely, bid well!",
    "History awaits its new keeper!"
]


def generate_auction_flavor(item_name, quality_tier):
    """Generate flavor text for an auction item."""
    intro = random.choice(AUCTION_INTROS)

    # Select descriptions based on quality
    num_descriptions = 1 if quality_tier in ["garbage", "common"] else random.randint(1, 2)
    descriptions = random.sample(AUCTION_DESCRIPTIONS, num_descriptions)

    closing = random.choice(AUCTION_CLOSINGS)

    flavor = f"{intro} {item_name}! "
    flavor += " ".join(descriptions) + " "
    flavor += closing

    return flavor


# NPC Personality flavor
NPC_REACTIONS_WIN = [
    "smirks confidently",
    "nods with satisfaction",
    "grins triumphantly",
    "chuckles to themselves",
    "adjusts their collar smugly",
    "raises an eyebrow victoriously",
    "allows themselves a small smile"
]

NPC_REACTIONS_LOSE = [
    "frowns deeply",
    "shakes their head in disappointment",
    "mutters under their breath",
    "clenches their fist",
    "narrows their eyes",
    "sighs heavily",
    "looks away in frustration"
]

NPC_REACTIONS_BID = [
    "raises their hand confidently",
    "calls out their bid clearly",
    "makes a subtle gesture",
    "shouts their offer boldly",
    "signals with a knowing smile",
    "speaks up firmly",
    "bids with determination"
]


def get_npc_reaction(situation):
    """Get a random NPC reaction for a situation."""
    if situation == "win":
        return random.choice(NPC_REACTIONS_WIN)
    elif situation == "lose":
        return random.choice(NPC_REACTIONS_LOSE)
    elif situation == "bid":
        return random.choice(NPC_REACTIONS_BID)
    return ""
