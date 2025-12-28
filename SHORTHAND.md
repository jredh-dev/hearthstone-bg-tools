# Hearthstone Battlegrounds Shorthand Code System

A compact text-based notation system for representing Battlegrounds minions, designed for quick board visualization and note-taking.

---

## Format

```
T{tier}{tribes}{attack}/{health}[keywords]
```

### Components

1. **Tier** (`T{1-7}`) - Tavern tier (1 through 7)
2. **Tribes** (1+ letter codes) - Minion type(s)
3. **Stats** (`{attack}/{health}`) - Current attack and health
4. **Keywords** (optional letter codes) - Mechanics like Taunt, Divine Shield

---

## Tribe Codes

| Code | Tribe | Reason |
|------|-------|--------|
| **B** | Beast | **B**east |
| **D** | Demon | **D**emon |
| **R** | Dragon | d**R**agon (D taken) |
| **E** | Elemental | **E**lemental |
| **M** | Mechanical (Mech) | **M**echanical |
| **U** | Murloc | m**U**rloc (M taken) |
| **A** | Naga | n**A**ga (N taken) |
| **P** | Pirate | **P**irate |
| **Q** | Quilboar | **Q**uilboar |
| **Z** | Undead | undead (last letter, U taken) |
| ***** | All | All tribes |
| **N** | None/Neutral | **N**eutral (no tribe) |

**Multi-Tribe Minions**: Combine letters (e.g., `RD` = Dragon+Demon)

---

## Keyword Codes

| Code | Keyword | Example |
|------|---------|---------|
| **T** | Taunt | `T3B5/7T` = 5/7 Beast with Taunt |
| **+** | Divine Shield | `T6R12/12+` = 12/12 Dragon with Shield |
| **W** | Windfury | `T5M8/8W` = 8/8 Mech with Windfury |
| **R** | Reborn | `T4U4/4R` = 4/4 Murloc with Reborn |
| **P** | Poisonous | `T2U2/2P` = 2/2 Murloc with Poison |
| **D** | Deathrattle | `T3B4/3D` = 4/3 Beast with Deathrattle |
| **B** | Battlecry | `T5N2/4B` = Brann (2/4 with Battlecry) |
| **S** | Stealth | `T2N3/2S` = 3/2 with Stealth |
| **C** | Charge | `T1B2/1C` = 2/1 Beast with Charge |
| **G** | Magnetic | `T3M3/3G` = 3/3 Mech with Magnetic |
| **H** | Rush | `T4P5/5H` = 5/5 Pirate with Rush |
| **L** | Lifesteal | `T5D6/6L` = 6/6 Demon with Lifesteal |

**Multiple Keywords**: Combine letters (e.g., `T6R12/12+T` = Shield + Taunt)

---

## Examples

### Basic Minions

```
T1B2/1     = Tier 1 Beast, 2/1 (e.g., Alleycat)
T2U3/2     = Tier 2 Murloc, 3/2
T3Q4/5     = Tier 3 Quilboar, 4/5
T6R10/10   = Tier 6 Dragon, 10/10
T7*20/20   = Tier 7 All-tribes, 20/20
```

### With Keywords

```
T3B4/3DT   = Tier 3 Beast 4/3 with Deathrattle and Taunt
T5M10/8+W  = Tier 5 Mech 10/8 with Divine Shield and Windfury
T2U3/3P    = Tier 2 Murloc 3/3 with Poisonous
T6R12/12+  = Tier 6 Dragon 12/12 with Divine Shield
```

### Multi-Tribe

```
T4RD5/5    = Tier 4 Dragon+Demon, 5/5
T6*6/6+    = Tier 6 All-tribes, 6/6 with Divine Shield
```

---

## Board Visualization

Represent a full board (up to 7 minions) with shorthand:

```
============================================================
Player's Board
============================================================
  1. T3B4/3DT
  2. T5M10/8+W
  3. T4D7/7
  4. T6R12/12T
  5. T2U3/3P
  6. T5Q8/8D
  7. T7*20/20+
============================================================
```

**Benefits**:
- Compact: Fits in terminal or notes
- Quick to read: See stats and keywords at a glance
- Easy to share: Text-based, works everywhere

---

## Usage with `shorthand.py`

The included Python script generates shorthand codes from the JSON data.

### Search for a Minion

```bash
python3 shorthand.py search "Brann"
```

Output:
```
[T5N2/4B] Brann Bronzebeard
```

### List Tier Minions

```bash
python3 shorthand.py tier 6
```

Output:
```
Tier 6 Minions (36):

[T6E6/6] Acid Rainfall
[T6M6/4G] Apexis Guardian
[T6N10/10] Archaedas
...
```

### Visualize Example Board

```bash
python3 shorthand.py board
```

### Generate All Codes

```bash
python3 shorthand.py
```

Shows all minions grouped by tier with shorthand codes.

---

## Manual Notation

When taking notes or tracking games:

**Before Combat**:
```
Me:       T4B8/8+  T3U5/5P  T5M10/10W  T2Q3/3  T6R12/12T
Opponent: T3D6/6   T4E7/7   T5P8/8D    T6*10/10+  T7N15/15
```

**After Combat** (update stats):
```
Me:       T4B8/8+  -DEAD-   T5M10/10W  T2Q3/3  T6R12/7T   (took damage)
Opponent: -DEAD-   T4E7/7   -DEAD-     T6*10/10+  T7N15/15
```

**Golden Minions** (doubled stats):
```
T6R24/24+T  = Golden tier 6 Dragon (double stats)
```

---

## Common Abbreviations

For even more compact notation:

- **G** = Golden (doubled stats)
- **B** = Buffed (temporary)
- **~** = Approximate stats (varies)

Examples:
```
T5M20/20+W(G)  = Golden Mech with massive stats
T3B8/8(B)      = Buffed Beast (temporary)
T6R~10/~10     = Dragon with variable stats
```

---

## Meta Builds (Text Format)

Using shorthand, you can document popular compositions:

### Beasts (Stats Build)

```
T6B30/30+T   Goldrinn/Leapfrogger scaling
T5B15/15R    Reborn beast
T4B10/10D    Deathrattle triggers
T3B8/8T      Taunt protection
T2B6/6       Early game beast
T1B4/4       Filler
```

### Mechs (Divine Shield)

```
T6M40/40+W   Mega-windfury mech
T5M20/20+    Divine shield wall
T4M15/15G+   Magnetic stack
T3M10/10+    Shield protection
T2M8/8+      Early shield
```

### Murlocs (Poison)

```
T6U10/10P+T  Poison + shield + taunt
T5U8/8P+     Poison wall
T4U6/6P      Poison scalers
T3U5/5PT     Early poison
T2U4/4P      Starter poison
```

---

## Best Practices

1. **Update Stats Live**: Modify codes as minions get buffed during games
2. **Track Golden Status**: Add `(G)` suffix or just double the stats
3. **Note Auras**: Use `^` for aura buffs (e.g., `T4B5/5^ = has Baron buff`)
4. **Positioning Matters**: List left-to-right as they appear on board
5. **Comments**: Add `//` for notes (e.g., `T6R12/12+ // taunt giver`)

---

## Conversion Table

Quick reference for common minions:

| Shorthand | Minion Name | Notes |
|-----------|-------------|-------|
| `T5N2/4B` | Brann Bronzebeard | Double battlecries |
| `T5N1/1D` | Baron Rivendare | Double deathrattles |
| `T6M6/3` | Kangor's Apprentice | Resurrect mechs |
| `T4U4/4R` | Reborn murloc | Common poison carrier |
| `T6R12/12` | Scaled dragon | Late game win condition |

---

## Future Enhancements

Potential additions to the shorthand system:

- **Aura effects**: `^{source}` (e.g., `T4B5/5^BR` = buffed by Baron)
- **Temporary buffs**: `(+2/+2)` (e.g., `T3B6/6(+2/+2)` = base 4/4)
- **Discovered/created**: `*` prefix (e.g., `*T5D6/6` = discovered demon)
- **Hero power targets**: `@` (e.g., `T4B8/8@ = targeted by HP`)

---

## Tips for Learning

1. Start with tier + tribe + stats: `T3B5/5`
2. Add common keywords: `T3B5/5T` (Taunt), `T3B5/5+` (Shield)
3. Practice with your own games: Note boards after each turn
4. Use the search tool: `python3 shorthand.py search <name>`
5. Reference tribe codes until memorized

**Most Important**:
- **T** = Tier number
- **Letter(s)** = Tribe(s)
- **#/#** = Attack/Health
- **Letters after** = Keywords

**Pro Tip**: Focus on memorizing common tribes (B, D, R, M, U, Q) and common keywords (T, +, W, P, D) first!
