# Battle Simulator ⚔️

A turn-based battle system featuring anime characters with unique abilities. Watch Rimuru and Veldora fight it out with special ultimate moves!

## Features

- 🎮 **Turn-Based Combat**: Both characters attack each other simultaneously
- ⚡ **Ultimate Abilities**: Each character has a unique special move with a chance to activate
- 💚 **Dynamic HP System**: HP cannot go below 0, preventing overkill
- 🎯 **Customizable Stats**: Override default values with command-line arguments
- 🎨 **Colored Output**: Enhanced terminal formatting for better readability
- ⏱️ **Game Speed Control**: Adjust battle pacing from 1-20 for your preferred tempo

## Characters

### Rimuru
- **Attack Damage**: 1 (default)
- **Health Points**: 30 (default)
- **Ultimate Ability**: Regeneration
  - 35% chance per turn to restore 3 HP
  - Great for prolonged battles

### Veldora
- **Attack Damage**: 1 (default)
- **Health Points**: 100 (default)
- **Ultimate Ability**: Super Saiyan Boost
  - 5% chance per turn to gain +9999999 attack damage (instant win!)
  - Rare but devastating when triggered

## Requirements

- Python 3.6+
- No external dependencies

## Installation

```bash
git clone https://github.com/yourusername/battle-simulator.git
cd battle-simulator
```

## How to Run

### Default Values
```bash
python Main.py
```

Starts a battle with default stats:
- Rimuru: 5 AD, 30 HP
- Veldora: 1 AD, 50 HP

You'll be prompted to enter a game speed (1-20 recommended, 10 is standard)

### Custom Values
```bash
python Main.py [rimuru_ad] [rimuru_hp] [veldora_ad] [veldora_hp]
```

**Example:**
```bash
python Main.py 10 50 5 100
```

Starts a battle with:
- Rimuru: 10 AD, 50 HP
- Veldora: 5 AD, 100 HP

You'll still be prompted for game speed.

### Game Speed
After entering arguments (or using defaults), you'll see:
```
Enter game speed (recommended 10): 
```

- **Higher speed** (15-20) = Faster battles, less dramatic pauses
- **Lower speed** (1-5) = Slower, more dramatic battles with longer waits
- **10** = Recommended for best pacing

### Error Handling
Invalid arguments will display:
```
Invalid number of arguments!
Read the documentation on github for further instructions.
```

The program will exit immediately without asking for speed.

## File Structure

```
battle-simulator/
├── Main.py          # Entry point & battle logic
├── Enemy.py         # Base enemy class
├── Rimuru.py        # Rimuru character class
├── Veldora.py       # Veldora character class
├── README.md        # This file
└── .gitignore       # Git ignore file
```

## Sample Output

```
Enter game speed (recommended 10): 10

Fight me!!
Haha! Come brother, I shall entertain you.

------Round 1------
-------Fight!------
Rimuru has no ultimate.
Veldora has no ultimate.
Rimuru deals 5 damage.
Veldora deals 1 damage.
Rimuru: 29 hp
Veldora: 45 hp

------Round 2------
-------Fight!------
Rimuru regenerated 3 hp!
Veldora has no ultimate.
Rimuru deals 5 damage.
Veldora deals 1 damage.
Rimuru: 31 hp
Veldora: 40 hp

------Round 3------
-------Fight!------
Rimuru has no ultimate.
Veldora has no ultimate.
Rimuru deals 5 damage.
Veldora deals 1 damage.
Rimuru: 30 hp
Veldora: 35 hp

...

### ⭐ Rimuru Wins ⭐ ###
** rimuru smirks
```

*Note: HP displays in green, winner name in yellow, and the game includes strategic pauses based on your speed setting.*

## Game Mechanics

1. Both characters greet each other
2. Each round:
   - Check if either ultimate activates (random chance)
   - Both characters attack simultaneously
   - Damage is dealt to both
   - HP is displayed (cannot go below 0)
3. Battle ends when one or both characters reach 0 HP
4. Winner is announced

## Future Enhancements

- [ ] More characters with unique abilities
- [ ] Difficulty levels
- [ ] Save/replay battles
- [ ] GUI interface
- [ ] Item system (potions, weapons, etc.)

## License

This project is open source and available under the MIT License.

## Author

Created for learning Python OOP and game development concepts.

---

**Have fun battling!** ⚡