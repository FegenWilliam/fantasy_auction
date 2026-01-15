# Fantasy Auction Battle

A menu-based game where you compete against 3 NPCs in daily fantasy auctions!

## How to Play

Run the game:
```bash
python3 fantasy_auction.py
```

## Game Overview

**Objective**: Build your fortune by buying low and selling high at fantasy auctions. Outlast your rivals and accumulate the most gold!

**Starting Conditions**:
- Everyone starts with 10,000 gold
- Compete against 3 NPCs with different personalities
- Game lasts up to 30 days or until winners/losers are determined

## Daily Cycle

### 1. Prep Session
- View current standings (gold, items won, total profit)
- Check who's been eliminated
- See who's in the lead

### 2. Auction Selection
- Each day has 3 auctions
- Choose 1 auction to participate in
- NPCs independently choose their auctions
- Preview: item name, starting bid, and flavor text

### 3. Auction Session
- Take turns bidding against NPCs
- Options: **[B]id**, **[P]ass**, or **[I]nfo** for details
- Bid in increments (minimum 50g or 10% of current bid)
- Auction ends when everyone passes or you force close it

### 4. Results
- Winner pays their final bid
- Item's **true worth** is revealed
- Item is automatically sold for its true worth
- Profit/loss is calculated and added to your total

## Item Quality Tiers

Items range from worthless junk to priceless relics:

| Tier | Worth Range | Drop Rate | Risk/Reward |
|------|-------------|-----------|-------------|
| **Garbage** | 50-400g | 25% | Often **overvalued** - buyer beware! |
| **Common** | 300-1,200g | 35% | Mixed - could go either way |
| **Uncommon** | 800-2,500g | 25% | Mixed - some good deals here |
| **Rare** | 2,000-5,000g | 12% | Usually solid value |
| **Relic** | 4,000-10,000g | 3% | Often **undervalued** - great deals! |

**Key Strategy**: The starting bid can be deceiving! High starting bids don't always mean high value - garbage items are often overpriced, while relics might have surprisingly low starting bids. Pay attention to the flavor text and trust your instincts!

## NPC Personalities

Your 3 rivals have different bidding strategies:

- **Aggressive**: Bids often and high, willing to overpay
- **Cautious**: Conservative bidder, rarely overpays
- **Balanced**: Standard approach, reasonable bids
- **Random**: Unpredictable wildcard

Each NPC also has a random risk tolerance affecting how much they're willing to spend.

## Winning & Losing

**Elimination**: Players with less than 50 gold are eliminated

**Victory Conditions**:
- Have the most gold after 30 days
- Be the last one standing if everyone else is eliminated
- Eliminate all NPCs before day 30

**Strategy Tips**:
- Don't overbid! Profit comes from buying below true worth
- Watch your gold reserves - going broke means elimination
- Relics are rare but often underpriced - great opportunities!
- Garbage items are common traps with inflated starting bids
- NPCs don't know true values - use this to your advantage
- Sometimes passing is the best move

## Files

- `fantasy_auction.py` - Main game with all mechanics
- `generators.py` - Random name and flavor text generators

Enjoy the auction battles!
