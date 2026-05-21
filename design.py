from pathlib import Path

# ---------- Farben (verbindlich) ----------
CLASS_COLORS = {
    'Death Knight': '#5E1410',
    'Warlock':      '#8E2416',
    'Rogue':        '#7A3A18',
    'Warrior':      '#5A3E28',
    'Hunter':       '#6F6A2A',
    'Shaman':       '#B85A2B',
    'Druid':        '#C98A5A',
    'Mage':         '#E57A1F',
    'Paladin':      '#F2C10F',
    'Priest':       '#E6D3A3',
}

RACE_COLORS = {
    'Blood Elf': '#E6D3A3',
    'Orc':       '#6F6A2A',
    'Tauren':    '#6B4A2D',
    'Troll':     '#D45A2A',
    'Undead':    '#5E1410',
}

ROLE_MAP = {
    'Warrior': 'Tank',
    'Paladin': 'Tank',
    'Death Knight': 'Tank',

    'Priest': 'Healer',
    'Druid': 'Healer',
    'Shaman': 'Healer',

    'Mage': 'DPS',
    'Warlock': 'DPS',
    'Rogue': 'DPS',
    'Hunter': 'DPS',
}

ROLE_COLORS = {
    'Tank': '#5C6F8A',
    'Healer': '#6E8B6E',
    'DPS': '#8A3F2D',
}

ASSETS = Path('assets')
CLASS_DIR = ASSETS / 'classes'
RACE_DIR = ASSETS / 'races'
HORDE_ICON = ASSETS / 'horde.png'

RACE_ICON_KEY = {
    'Blood Elf': 'bloodelf',
    'Orc': 'orc',
    'Tauren': 'tauren',
    'Troll': 'troll',
    'Undead': 'scourge',
}

def _norm(x: str) -> str:
    return str(x).strip().lower().replace(' ', '').replace('-', '')

def class_icon_path(class_name: str) -> str | None:
    p = CLASS_DIR / f'{_norm(class_name)}.jpg'
    return str(p) if p.exists() else None

def race_icon_path(race_name: str, gender: str) -> str | None:
    key = RACE_ICON_KEY.get(race_name)
    if not key:
        return None
    p = RACE_DIR / f'{key}_{gender}.jpg'
    return str(p) if p.exists() else None
