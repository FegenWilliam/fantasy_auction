#!/usr/bin/env python3
"""
Fantasy Auction Battle Game
A menu-based game where you compete against 3 NPCs in daily auctions.
"""
import random
import time
from generators import (
    generate_npc_name, generate_item_name, generate_auction_flavor,
    get_npc_reaction
)


# 25 Unique Relics - one-of-a-kind items that you keep forever
UNIQUE_RELICS = [
    {
        "name": "Crown of Ancient Kings",
        "description": "A crown that glows with ethereal light, its gemstones pulsing with timeless power.",
        "worth": 8000,
        "hint_words": ["ancient", "timeless", "ethereal"]
    },
    {
        "name": "Dragon's Heartstone",
        "description": "A pulsing red gem radiating warmth, said to contain the essence of a legendary dragon.",
        "worth": 9500,
        "hint_words": ["legendary", "essence", "radiating"]
    },
    {
        "name": "Staff of the Cosmos",
        "description": "A staff with stars swirling within its core, holding the mysteries of the universe.",
        "worth": 7500,
        "hint_words": ["mysteries", "universe", "swirling"]
    },
    {
        "name": "Blade of Eternal Frost",
        "description": "A sword perpetually frozen, its edge sharper than any mortal blade could be.",
        "worth": 8200,
        "hint_words": ["eternal", "perpetually", "mortal"]
    },
    {
        "name": "Amulet of Time",
        "description": "A pendant that ticks like a cosmic clock, its hands moving in impossible directions.",
        "worth": 9000,
        "hint_words": ["cosmic", "impossible", "ticks"]
    },
    {
        "name": "Phoenix Feather Quill",
        "description": "A quill that writes in flames, yet never burns the parchment it touches.",
        "worth": 6800,
        "hint_words": ["flames", "never burns", "phoenix"]
    },
    {
        "name": "Mirror of Truth",
        "description": "A mirror showing more than mere reflections, revealing what lies beneath.",
        "worth": 7800,
        "hint_words": ["revealing", "beneath", "more than"]
    },
    {
        "name": "Ring of Whispers",
        "description": "A ring that murmurs ancient secrets to those who wear it.",
        "worth": 6500,
        "hint_words": ["ancient", "secrets", "murmurs"]
    },
    {
        "name": "Orb of Storms",
        "description": "A sphere crackling with miniature lightning, holding the fury of a thousand tempests.",
        "worth": 8800,
        "hint_words": ["fury", "tempests", "crackling"]
    },
    {
        "name": "Boots of the Windwalker",
        "description": "Boots that seem weightless, as if crafted from clouds and morning mist.",
        "worth": 7200,
        "hint_words": ["weightless", "clouds", "crafted"]
    },
    {
        "name": "Chalice of Stars",
        "description": "A cup eternally filled with liquid starlight that never spills.",
        "worth": 8500,
        "hint_words": ["eternally", "starlight", "never spills"]
    },
    {
        "name": "Tome of Forgotten Lore",
        "description": "An ancient book whose pages change with each reading, holding infinite knowledge.",
        "worth": 9200,
        "hint_words": ["ancient", "infinite", "change"]
    },
    {
        "name": "Gauntlets of the Titan",
        "description": "Gauntlets radiating raw power, forged in an age long past.",
        "worth": 8400,
        "hint_words": ["radiating", "forged", "age long past"]
    },
    {
        "name": "Cloak of Shadows",
        "description": "A cloak that absorbs light itself, woven from the fabric of night.",
        "worth": 7600,
        "hint_words": ["absorbs", "woven", "fabric of night"]
    },
    {
        "name": "Harp of the Sirens",
        "description": "An instrument that plays haunting melodies on its own, enchanting all who hear.",
        "worth": 7000,
        "hint_words": ["haunting", "enchanting", "on its own"]
    },
    {
        "name": "Compass of Destiny",
        "description": "A compass pointing not to north, but to one's true path in life.",
        "worth": 6900,
        "hint_words": ["true path", "destiny", "not to north"]
    },
    {
        "name": "Lantern of Souls",
        "description": "A lantern with a flame that never dies, illuminating more than just darkness.",
        "worth": 7400,
        "hint_words": ["never dies", "illuminating", "more than"]
    },
    {
        "name": "Mask of Many Faces",
        "description": "A mask whose expression shifts and changes, reflecting infinite possibilities.",
        "worth": 7100,
        "hint_words": ["shifts", "infinite", "possibilities"]
    },
    {
        "name": "Scepter of Command",
        "description": "A scepter humming with unquestionable authority, obeyed by reality itself.",
        "worth": 9800,
        "hint_words": ["unquestionable", "authority", "reality itself"]
    },
    {
        "name": "Hourglass of Eternity",
        "description": "An hourglass where sand flows upward, defying the very laws of nature.",
        "worth": 8600,
        "hint_words": ["eternity", "defying", "upward"]
    },
    {
        "name": "Locket of Memories",
        "description": "A locket showing scenes from forgotten times, preserving moments lost to history.",
        "worth": 6700,
        "hint_words": ["forgotten", "preserving", "lost to history"]
    },
    {
        "name": "Bracers of the Guardian",
        "description": "Bracers inscribed with protective runes that glow with everlasting vigor.",
        "worth": 7300,
        "hint_words": ["everlasting", "protective", "runes"]
    },
    {
        "name": "Pendant of the Moon",
        "description": "A pendant glowing with pure lunar light, waxing and waning with celestial rhythm.",
        "worth": 7700,
        "hint_words": ["lunar", "celestial", "waxing and waning"]
    },
    {
        "name": "Horn of Legends",
        "description": "A horn that echoes with the calls of heroes from ages immemorial.",
        "worth": 8100,
        "hint_words": ["echoes", "heroes", "immemorial"]
    },
    {
        "name": "Crystal of Pure Magic",
        "description": "A crystal pulsing with raw arcane energy, untainted by mortal hands.",
        "worth": 10000,
        "hint_words": ["pulsing", "arcane", "untainted"]
    }
]


class Item:
    """Represents an auction item."""

    QUALITY_TIERS = {
        "garbage": {"min_worth": 50, "max_worth": 400, "weight": 25},
        "common": {"min_worth": 300, "max_worth": 1200, "weight": 35},
        "uncommon": {"min_worth": 800, "max_worth": 2500, "weight": 25},
        "rare": {"min_worth": 2000, "max_worth": 5000, "weight": 12},
        "relic": {"min_worth": 4000, "max_worth": 10000, "weight": 3}
    }

    def __init__(self, available_unique_relics=None):
        # Check if this should be a unique relic
        self.is_unique_relic = False
        self.relic_data = None
        self.auction_name = None  # The obscured name shown during auction

        # Small chance to generate a unique relic (if any are available)
        if available_unique_relics and len(available_unique_relics) > 0:
            # 5% chance per item to be a unique relic
            if random.random() < 0.05:
                self.is_unique_relic = True
                self.relic_data = random.choice(available_unique_relics)
                self.quality = "relic"
                self.true_worth = self.relic_data["worth"]

                # Generate obscured name for auction
                self.auction_name = generate_item_name(self.quality)
                self.name = self.relic_data["name"]  # True name revealed after winning

                # Price is significantly undervalued for unique relics
                self.base_price = random.randint(int(self.true_worth * 0.2), int(self.true_worth * 0.6))

                # Generate flavor text with subtle hints
                self.flavor_text = self._generate_relic_flavor()
                self.winner = None
                return

        # Regular item generation
        # Randomly determine quality tier
        tiers = list(self.QUALITY_TIERS.keys())
        weights = [self.QUALITY_TIERS[t]["weight"] for t in tiers]
        self.quality = random.choices(tiers, weights=weights)[0]

        # Generate item properties
        self.name = generate_item_name(self.quality)
        self.auction_name = self.name  # For regular items, auction name = real name
        tier_info = self.QUALITY_TIERS[self.quality]
        self.true_worth = random.randint(tier_info["min_worth"], tier_info["max_worth"])

        # Base price is offset from true worth (creating risk/reward)
        # Can be undervalued or overvalued
        if self.quality == "garbage":
            # Garbage often overvalued
            self.base_price = random.randint(int(self.true_worth * 0.8), int(self.true_worth * 2.5))
        elif self.quality == "relic":
            # Relics often undervalued (great deals!)
            self.base_price = random.randint(int(self.true_worth * 0.3), int(self.true_worth * 0.8))
        else:
            # Others are mixed
            multiplier = random.uniform(0.5, 1.8)
            self.base_price = int(self.true_worth * multiplier)

        self.base_price = max(50, self.base_price)  # Minimum 50 gold
        self.flavor_text = generate_auction_flavor(self.name, self.quality)
        self.winner = None

    def _generate_relic_flavor(self):
        """Generate flavor text for unique relics with subtle hints."""
        hint_words = self.relic_data["hint_words"]

        templates = [
            f"An extraordinary artifact, the auctioneer speaks of its {hint_words[0]} origins with reverence.",
            f"The item seems to possess a {hint_words[1]} quality that defies explanation.",
            f"Whispers among collectors suggest this piece is {hint_words[2]} in nature.",
            f"The seller's hands tremble slightly - this {hint_words[0]} piece clearly means something special.",
            f"Documents accompanying the item mention {hint_words[1]} properties, though details are scarce.",
            f"A {hint_words[2]} aura surrounds this piece, making it stand out from common wares.",
        ]

        return random.choice(templates)

    def get_display_name(self):
        """Get the name to display during auction (obscured for unique relics)."""
        return self.auction_name

    def get_profit(self, purchase_price):
        """Calculate profit if sold after winning."""
        return self.true_worth - purchase_price


class Participant:
    """Base class for player and NPCs."""

    def __init__(self, name, is_player=False):
        self.name = name
        self.gold = 10000
        self.items_won = []
        self.relics_collected = []  # Unique relics are kept, not sold
        self.is_player = is_player
        self.active = True
        self.total_profit = 0

    def can_bid(self, amount):
        """Check if participant can afford to bid."""
        return self.gold >= amount and self.active

    def place_bid(self, amount):
        """Place a bid (doesn't deduct gold yet)."""
        return amount

    def win_item(self, item, price):
        """Win an item and pay for it."""
        self.gold -= price
        self.items_won.append(item)
        item.winner = self

        # Check if this is a unique relic
        if item.is_unique_relic:
            # Keep the relic! Don't sell it.
            self.relics_collected.append(item)
            # No profit/loss calculation - it's priceless!
        else:
            # Automatically sell regular item
            profit = item.get_profit(price)
            self.gold += item.true_worth
            self.total_profit += profit

    def is_eliminated(self):
        """Check if participant is out of the game."""
        return self.gold < 50 or not self.active


class NPC(Participant):
    """NPC with bidding AI."""

    PERSONALITIES = ["aggressive", "cautious", "balanced", "random"]

    def __init__(self):
        name = generate_npc_name()
        super().__init__(name, is_player=False)
        self.personality = random.choice(self.PERSONALITIES)
        self.risk_tolerance = random.uniform(0.3, 1.5)

    def decide_bid(self, current_bid, item, min_increment):
        """Decide whether to bid and how much."""
        if not self.can_bid(current_bid + min_increment):
            return None

        # Estimate value (NPCs have imperfect knowledge)
        estimated_value = self._estimate_value(item)
        max_willing = int(estimated_value * self.risk_tolerance)

        # Personality affects bidding
        if self.personality == "aggressive":
            # Bid more often, higher amounts
            if current_bid < max_willing * 0.9:
                increment = random.randint(min_increment, min_increment * 3)
                return current_bid + increment

        elif self.personality == "cautious":
            # Bid conservatively
            if current_bid < max_willing * 0.6:
                return current_bid + min_increment

        elif self.personality == "balanced":
            # Standard bidding
            if current_bid < max_willing * 0.75:
                increment = random.randint(min_increment, min_increment * 2)
                return current_bid + increment

        else:  # random
            # Unpredictable
            if random.random() < 0.4 and current_bid < max_willing:
                increment = random.randint(min_increment, min_increment * 5)
                return current_bid + increment

        return None

    def _estimate_value(self, item):
        """Estimate item value (with some error)."""
        # NPCs don't know true worth exactly
        error_margin = random.uniform(0.6, 1.4)
        estimated = int(item.true_worth * error_margin)

        # Sometimes NPCs are influenced by base price
        if random.random() < 0.3:
            estimated = int((estimated + item.base_price) / 2)

        return estimated


class Auction:
    """Manages a single auction event."""

    def __init__(self, auction_id, available_relics=None):
        self.id = auction_id
        self.item = Item(available_relics)
        self.participants = []
        self.winner = None
        self.final_price = 0

    def add_participant(self, participant):
        """Add a participant to this auction."""
        self.participants.append(participant)

    def run(self, game):
        """Execute the auction."""
        print("\n" + "="*70)
        print(f"AUCTION #{self.id}")
        print("="*70)
        print(f"\n{self.item.flavor_text}\n")
        print(f"ITEM: {self.item.get_display_name()}")
        print(f"STARTING BID: {self.item.base_price} gold")
        print(f"\nParticipants: {', '.join([p.name for p in self.participants])}")
        print("\n" + "-"*70)

        input("\n[Press Enter to begin bidding]")

        current_bid = self.item.base_price
        current_winner = None
        min_increment = max(50, int(self.item.base_price * 0.1))

        bidding_active = True
        consecutive_passes = 0

        while bidding_active:
            print(f"\nCurrent bid: {current_bid} gold")
            if current_winner:
                print(f"Current winner: {current_winner.name}")
            print()

            # Shuffle participants for fairness
            bid_order = self.participants.copy()
            random.shuffle(bid_order)

            round_had_bid = False

            for participant in bid_order:
                if not participant.can_bid(current_bid + min_increment):
                    continue

                if participant.is_player:
                    # Player's turn
                    print(f"\n>>> YOUR TURN <<<")
                    print(f"Your gold: {participant.gold}")
                    print(f"Current bid: {current_bid} gold")
                    print(f"Minimum bid: {current_bid + min_increment} gold")

                    choice = input("\n[B]id, [P]ass, or [I]nfo? ").strip().upper()

                    if choice == 'I':
                        self._show_item_info()
                        choice = input("\n[B]id or [P]ass? ").strip().upper()

                    if choice == 'B':
                        while True:
                            try:
                                bid_amount = input(f"Enter bid amount (min {current_bid + min_increment}): ").strip()
                                bid_amount = int(bid_amount)

                                if bid_amount < current_bid + min_increment:
                                    print(f"Bid must be at least {current_bid + min_increment} gold!")
                                elif bid_amount > participant.gold:
                                    print(f"You only have {participant.gold} gold!")
                                else:
                                    current_bid = bid_amount
                                    current_winner = participant
                                    round_had_bid = True
                                    print(f"\nYou bid {current_bid} gold!")
                                    break
                            except ValueError:
                                print("Invalid input! Enter a number.")
                    else:
                        print(f"{participant.name} passes.")

                else:
                    # NPC's turn
                    npc_bid = participant.decide_bid(current_bid, self.item, min_increment)

                    if npc_bid and participant.can_bid(npc_bid):
                        time.sleep(0.5)
                        print(f"{participant.name} {get_npc_reaction('bid')} - bids {npc_bid} gold!")
                        current_bid = npc_bid
                        current_winner = participant
                        round_had_bid = True
                    else:
                        print(f"{participant.name} passes.")

            if not round_had_bid:
                consecutive_passes += 1
                if consecutive_passes >= 2:
                    bidding_active = False
            else:
                consecutive_passes = 0

            if bidding_active:
                continue_bidding = input("\n[Continue to next round? Press Enter or type 'END' to close auction]").strip().upper()
                if continue_bidding == 'END' and current_winner:
                    bidding_active = False

        # Auction ends
        print("\n" + "="*70)
        if current_winner:
            print(f"SOLD to {current_winner.name} for {current_bid} gold!")
            current_winner.win_item(self.item, current_bid)
            self.winner = current_winner
            self.final_price = current_bid

            # Check if this was a unique relic
            if self.item.is_unique_relic:
                print("\n" + "*"*70)
                print("*** UNIQUE RELIC DISCOVERED! ***")
                print("*"*70)
                print(f"\nThe item's true identity is revealed:")
                print(f">>> {self.item.name} <<<")
                print(f"\n{self.item.relic_data['description']}")
                print(f"\nThis legendary artifact is priceless and will be kept in your collection!")
                print(f"Paid: {current_bid} gold")
                print("\n" + "*"*70)

                # Remove this relic from available pool
                if self.item.relic_data in game.available_relics:
                    game.available_relics.remove(self.item.relic_data)
                    print(f"\nUnique relics remaining in the world: {len(game.available_relics)}/25")
            else:
                # Regular item
                profit = self.item.get_profit(current_bid)
                print(f"\nItem's true worth: {self.item.true_worth} gold")
                print(f"Profit/Loss: {'+' if profit > 0 else ''}{profit} gold")

                if profit > 0:
                    print(f"\n{current_winner.name} {get_npc_reaction('win')} - What a deal!")
                else:
                    print(f"\n{current_winner.name} {get_npc_reaction('lose')} - Overpaid!")

            if not current_winner.is_player:
                print(f"{current_winner.name}'s gold: {current_winner.gold}")
        else:
            print("No sale - item withdrawn!")

        print("="*70)
        input("\n[Press Enter to continue]")

    def _show_item_info(self):
        """Show detailed item information."""
        print("\n" + "-"*70)
        print("ITEM DETAILS")
        print("-"*70)
        print(f"Name: {self.item.get_display_name()}")
        print(f"Starting Price: {self.item.base_price} gold")
        print(f"\n{self.item.flavor_text}")
        print("\nNote: True worth unknown until after purchase!")
        if self.item.is_unique_relic:
            print("\n[Something feels different about this item...]")
        print("-"*70)


class Game:
    """Main game manager."""

    def __init__(self):
        self.day = 1
        self.player = None
        self.npcs = []
        self.auctions_per_day = 3
        self.game_over = False
        self.max_days = 30
        # Track available unique relics (copy of the list so we can remove as found)
        self.available_relics = UNIQUE_RELICS.copy()

    def setup(self):
        """Initialize the game."""
        print("\n" + "="*70)
        print("WELCOME TO FANTASY AUCTION BATTLE!")
        print("="*70)
        print("\nYou and 3 rival auctioneers will compete to build your fortune!")
        print("Each day, choose which auction to enter and bid wisely.")
        print("Items have hidden true values - find the relics and avoid the junk!")
        print("\nStarting gold: 10,000")
        print("\n*** NEW: 25 UNIQUE RELICS are hidden in the world! ***")
        print("Find them and keep them in your collection forever!")
        print("Look for subtle hints in item descriptions...")
        print("\nSurvive and profit to win!")
        print("="*70)

        player_name = input("\nEnter your name: ").strip()
        if not player_name:
            player_name = "The Player"

        self.player = Participant(player_name, is_player=True)

        # Create 3 NPCs
        self.npcs = [NPC() for _ in range(3)]

        print(f"\nYour rivals are:")
        for npc in self.npcs:
            print(f"  - {npc.name} ({npc.personality})")

        input("\n[Press Enter to begin Day 1]")

    def run(self):
        """Main game loop."""
        self.setup()

        while not self.game_over and self.day <= self.max_days:
            self.run_day()
            self.check_game_state()
            self.day += 1

        self.end_game()

    def run_day(self):
        """Run a single day of auctions."""
        print("\n" + "="*70)
        print(f"DAY {self.day}")
        print("="*70)

        # Prep session
        self.prep_session()

        # Generate auctions (pass available relics)
        auctions = [Auction(i+1, self.available_relics) for i in range(self.auctions_per_day)]

        # Player chooses auction
        chosen_auction = self.choose_auction(auctions)

        # NPCs choose auctions randomly
        for npc in self.npcs:
            if not npc.is_eliminated():
                auction = random.choice(auctions)
                auction.add_participant(npc)

        # Add player to chosen auction
        if chosen_auction:
            chosen_auction.add_participant(self.player)

        # Run player's auction
        if chosen_auction and not self.player.is_eliminated():
            chosen_auction.run(self)

        # Run other auctions (simulate)
        for auction in auctions:
            if auction != chosen_auction and len(auction.participants) > 0:
                self._simulate_auction(auction)

        # Day end summary
        self.day_summary()

    def prep_session(self):
        """Show prep session information."""
        print("\n--- PREP SESSION ---\n")

        # Show player's relic collection if they have any
        if len(self.player.relics_collected) > 0:
            print("YOUR RELIC COLLECTION:")
            for relic in self.player.relics_collected:
                print(f"  * {relic.name}")
            print(f"\nRelics collected: {len(self.player.relics_collected)}/25")
            print(f"Relics remaining in the world: {len(self.available_relics)}/25")
            print()

        print("Standing:")

        all_participants = [self.player] + self.npcs
        all_participants.sort(key=lambda p: p.gold, reverse=True)

        for i, p in enumerate(all_participants, 1):
            status = "(YOU)" if p.is_player else ""
            eliminated = "(ELIMINATED)" if p.is_eliminated() else ""
            print(f"{i}. {p.name} {status} {eliminated}")
            print(f"   Gold: {p.gold} | Items won: {len(p.items_won)} | Total profit: {p.total_profit}")
            if len(p.relics_collected) > 0:
                print(f"   Relics: {len(p.relics_collected)}")

        print()

    def choose_auction(self, auctions):
        """Let player choose which auction to enter."""
        print("\n--- AUCTION SELECTION ---\n")
        print(f"Today's auctions (choose 1 of {len(auctions)}):\n")

        for auction in auctions:
            print(f"Auction #{auction.id}")
            print(f"  Item: {auction.item.get_display_name()}")
            print(f"  Starting bid: {auction.item.base_price} gold")
            print(f"  Preview: {auction.item.flavor_text[:100]}...")
            print()

        while True:
            try:
                choice = input(f"Choose auction (1-{len(auctions)}): ").strip()
                choice = int(choice)
                if 1 <= choice <= len(auctions):
                    return auctions[choice - 1]
                else:
                    print(f"Please enter a number between 1 and {len(auctions)}.")
            except ValueError:
                print("Invalid input! Enter a number.")

    def _simulate_auction(self, auction):
        """Simulate an auction the player didn't attend."""
        if len(auction.participants) == 0:
            return

        # Simple simulation
        interested = [p for p in auction.participants if not p.is_eliminated()]
        if not interested:
            return

        # Random winner among interested NPCs
        winner = random.choice(interested)

        # Simulate final price
        estimated_value = random.randint(int(auction.item.true_worth * 0.5),
                                        int(auction.item.true_worth * 1.3))
        final_price = random.randint(auction.item.base_price,
                                     min(estimated_value, winner.gold))

        if winner.can_bid(final_price):
            winner.win_item(auction.item, final_price)
            auction.winner = winner
            auction.final_price = final_price

    def day_summary(self):
        """Show end of day summary."""
        print("\n" + "="*70)
        print(f"END OF DAY {self.day}")
        print("="*70)

        print("\nYour status:")
        print(f"Gold: {self.player.gold}")
        print(f"Items won today: {len([i for i in self.player.items_won if i.winner == self.player])}")
        print(f"Total profit: {self.player.total_profit}")
        print(f"Relics collected: {len(self.player.relics_collected)}/25")

        # Check eliminations
        eliminated = [npc for npc in self.npcs if npc.is_eliminated() and npc.active]
        for npc in eliminated:
            npc.active = False
            print(f"\n{npc.name} has been eliminated!")

        input("\n[Press Enter to continue]")

    def check_game_state(self):
        """Check if game should end."""
        # Player eliminated
        if self.player.is_eliminated():
            self.game_over = True
            return

        # All NPCs eliminated
        active_npcs = [npc for npc in self.npcs if not npc.is_eliminated()]
        if len(active_npcs) == 0:
            self.game_over = True
            return

        # Max days reached
        if self.day >= self.max_days:
            self.game_over = True

    def end_game(self):
        """Show game over screen."""
        print("\n" + "="*70)
        print("GAME OVER")
        print("="*70)

        all_participants = [self.player] + self.npcs
        all_participants.sort(key=lambda p: p.gold, reverse=True)

        print("\nFINAL STANDINGS:\n")
        for i, p in enumerate(all_participants, 1):
            status = "(YOU)" if p.is_player else ""
            print(f"{i}. {p.name} {status}")
            print(f"   Final gold: {p.gold}")
            print(f"   Items won: {len(p.items_won)}")
            print(f"   Total profit: {p.total_profit}")
            print(f"   Relics collected: {len(p.relics_collected)}")
            print()

        if all_participants[0].is_player:
            print("VICTORY! You are the greatest auctioneer!")
        else:
            print(f"Defeated! {all_participants[0].name} wins!")

        # Show player's final relic collection
        if len(self.player.relics_collected) > 0:
            print("\n" + "="*70)
            print("YOUR LEGENDARY RELIC COLLECTION:")
            print("="*70)
            for relic in self.player.relics_collected:
                print(f"\n* {relic.name}")
                print(f"  {relic.relic_data['description']}")
            print("\n" + "="*70)
            print(f"Total relics collected: {len(self.player.relics_collected)}/25")

        print("\n" + "="*70)


def main():
    """Entry point."""
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
