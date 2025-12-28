#!/usr/bin/env python3
"""
Hearthstone Battlegrounds Shorthand Code Generator

Creates compact text codes for Battlegrounds cards in format:
  T{tier}{tribes}{atk}/{hp}[keywords]

Examples:
  T2B3/2        - Tier 2 Beast, 3/2
  T6D9/5        - Tier 6 Demon, 9/5
  T4RD5/5T+     - Tier 4 Dragon+Demon, 5/5 with Taunt and Divine Shield
"""

import json
import sys
from pathlib import Path

# Tribe mapping (single character codes)
TRIBE_CODES = {
    'BEAST': 'B',
    'DEMON': 'D',
    'DRAGON': 'R',      # R for dRagon (D taken)
    'ELEMENTAL': 'E',
    'MECHANICAL': 'M',
    'MURLOC': 'U',      # U for mUrloc (M taken)
    'NAGA': 'A',        # A for nAga
    'PIRATE': 'P',
    'QUILBOAR': 'Q',
    'UNDEAD': 'Z',      # Z for undead
    'ALL': '*',         # All tribes
    'TOTEM': 'O'        # tOtem
}

# Keyword mapping (single character codes)
KEYWORD_CODES = {
    'TAUNT': 'T',
    'DIVINE_SHIELD': '+',
    'WINDFURY': 'W',
    'REBORN': 'R',
    'POISONOUS': 'P',
    'DEATHRATTLE': 'D',
    'BATTLECRY': 'B',
    'STEALTH': 'S',
    'CHARGE': 'C',
    'INSPIRE': 'I',
    'MAGNETIC': 'G',
    'RUSH': 'H',
    'IMMUNE': 'M',
    'LIFESTEAL': 'L',
    'VENOMOUS': 'V',
    'FRENZY': 'F'
}

def create_shorthand(card, include_keywords=True):
    """
    Create shorthand code for a card.
    
    Args:
        card: Card dictionary from JSON
        include_keywords: Whether to append keyword codes
        
    Returns:
        String shorthand code
    """
    # Tier
    tier = card.get('techLevel', '?')
    
    # Tribes
    tribes = card.get('races', [])
    if not tribes:
        tribe_code = 'N'  # Neutral/No tribe
    else:
        tribe_code = ''.join([TRIBE_CODES.get(t, t[0]) for t in tribes])
    
    # Stats
    attack = card.get('attack', 0)
    health = card.get('health', 0)
    
    # Base code
    code = f"T{tier}{tribe_code}{attack}/{health}"
    
    # Keywords (optional)
    if include_keywords:
        keywords = card.get('referencedTags', [])
        keyword_codes = []
        for kw in keywords:
            if kw in KEYWORD_CODES:
                keyword_codes.append(KEYWORD_CODES[kw])
        
        if keyword_codes:
            code += ''.join(sorted(set(keyword_codes)))  # Unique, sorted
    
    return code

def create_extended_shorthand(card):
    """
    Create extended shorthand with name abbreviation.
    
    Format: [T{tier}{tribes}{atk}/{hp}] Name
    """
    code = create_shorthand(card, include_keywords=True)
    name = card.get('name', 'Unknown')
    return f"[{code}] {name}"

def visualize_board(minion_codes, player_name="Player"):
    """
    Visualize a Battlegrounds board with shorthand codes.
    
    Args:
        minion_codes: List of up to 7 shorthand codes
        player_name: Name to display for player
    """
    print(f"\n{'=' * 60}")
    print(f"{player_name}'s Board")
    print('=' * 60)
    
    if not minion_codes:
        print("  [Empty Board]")
    else:
        for i, code in enumerate(minion_codes[:7], 1):
            print(f"  {i}. {code}")
    
    print('=' * 60)

def search_minion(minions, search_term):
    """Search for minions by name."""
    search_lower = search_term.lower()
    results = []
    
    for minion in minions:
        name = minion.get('name', '').lower()
        if search_lower in name:
            results.append(minion)
    
    return results

def main():
    # Load minions
    data_path = Path(__file__).parent / 'bg_minions.json'
    
    if not data_path.exists():
        print(f"Error: {data_path} not found")
        print("Run this script from the hearthstone-bg-data directory")
        sys.exit(1)
    
    with open(data_path) as f:
        minions = json.load(f)
    
    # Interactive mode
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == 'search' and len(sys.argv) > 2:
            # Search for a minion
            search_term = ' '.join(sys.argv[2:])
            results = search_minion(minions, search_term)
            
            if not results:
                print(f"No minions found matching '{search_term}'")
            else:
                print(f"\nFound {len(results)} minion(s):\n")
                for minion in results:
                    print(create_extended_shorthand(minion))
        
        elif command == 'tier' and len(sys.argv) > 2:
            # List all minions in a tier
            tier = int(sys.argv[2])
            tier_minions = [m for m in minions if m.get('techLevel') == tier]
            
            print(f"\nTier {tier} Minions ({len(tier_minions)}):\n")
            for minion in sorted(tier_minions, key=lambda m: m.get('name', '')):
                print(create_extended_shorthand(minion))
        
        elif command == 'board':
            # Example board visualization
            example_board = [
                "T3B4/3DT",     # Tier 3 Beast 4/3 with Deathrattle and Taunt
                "T5M10/8+W",    # Tier 5 Mech 10/8 with Divine Shield and Windfury
                "T4D7/7",       # Tier 4 Demon 7/7
                "T6R12/12T",    # Tier 6 Dragon 12/12 with Taunt
                "T2U3/3P",      # Tier 2 Murloc 3/3 with Poisonous
                "T5Q8/8D",      # Tier 5 Quilboar 8/8 with Deathrattle
                "T7*20/20+"     # Tier 7 All-tribes 20/20 with Divine Shield
            ]
            visualize_board(example_board, "Example Player")
        
        else:
            print(f"Unknown command: {command}")
            print("Usage:")
            print("  python shorthand.py search <name>")
            print("  python shorthand.py tier <number>")
            print("  python shorthand.py board")
    
    else:
        # Generate all shorthand codes
        print("Hearthstone Battlegrounds Shorthand Codes")
        print("=" * 80)
        print(f"Total Minions: {len(minions)}\n")
        
        # Group by tier
        for tier in range(1, 8):
            tier_minions = [m for m in minions if m.get('techLevel') == tier]
            if tier_minions:
                print(f"\n--- TIER {tier} ({len(tier_minions)} minions) ---")
                for minion in sorted(tier_minions, key=lambda m: m.get('name', ''))[:5]:
                    print(create_extended_shorthand(minion))
                if len(tier_minions) > 5:
                    print(f"  ... and {len(tier_minions) - 5} more")

if __name__ == '__main__':
    main()
