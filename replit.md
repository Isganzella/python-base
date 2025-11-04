# Python Learning Scripts

## Overview
This is a collection of beginner-level Python learning scripts created by Marlos Isganzella. The project contains various educational programs demonstrating basic Python concepts.

## Project Structure
```
.
├── main.py           # Main menu to run all scripts
├── hello.py          # Multi-language Hello World
├── calc_infix.py     # Infix calculator (sum, sub, mul, div)
├── tabuada.py        # Multiplication tables (1-10)
├── ecola.py          # School activities report (complete)
└── escola.py         # School activities example (incomplete)
```

## Scripts Description

### 1. hello.py
Multi-language Hello World that displays messages based on the LANG environment variable.
- Supports: Portuguese (pt_BR), Italian (it_IT), Spanish (es_SP), English (default)

### 2. calc_infix.py
Infix notation calculator supporting basic operations:
- Usage: `python calc_infix.py [operation] [n1] [n2]`
- Operations: sum, sub, mul, div
- Example: `python calc_infix.py sum 5 2` → 7

### 3. tabuada.py
Displays multiplication tables from 1 to 10 in formatted output.

### 4. ecola.py
School management script that groups students by classroom and activities (English, Music, Dance).

### 5. escola.py
Incomplete version of the school management script (learning example).

## Running the Project
The main.py script provides an interactive menu to run all the learning scripts.

## Recent Changes
- **2025-11-04**: Initial import from GitHub
- Fixed syntax errors in escola.py (changed periods to commas in list definitions)
- Fixed potential unbound variable in calc_infix.py
- Added main.py menu for easy script execution
- Configured for Replit environment

## Technology Stack
- Python 3.11
- Standard library only (no external dependencies)

## Language
All scripts and documentation are primarily in Portuguese (Brazilian).
