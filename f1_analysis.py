data = [
    {"race": "Bahrain", "driver": "Lewis Hamilton", "position": 1, "points": 25, "fastest_lap": 76.123},
    {"race": "Bahrain", "driver": "Max Verstappen", "position": 2, "points": 18, "fastest_lap": 76.456},
    {"race": "Bahrain", "driver": "Charles Leclerc", "position": 3, "points": 15, "fastest_lap": 77.001},
    {"race": "Bahrain", "driver": "Lando Norris", "position": 4, "points": 12, "fastest_lap": 77.500},
    {"race": "Bahrain", "driver": "Carlos Sainz", "position": 5, "points": 10, "fastest_lap": 77.800},

    {"race": "Saudi Arabia", "driver": "Max Verstappen", "position": 1, "points": 25, "fastest_lap": 73.912},
    {"race": "Saudi Arabia", "driver": "Lewis Hamilton", "position": 2, "points": 18, "fastest_lap": 74.120},
    {"race": "Saudi Arabia", "driver": "Lando Norris", "position": 3, "points": 15, "fastest_lap": 75.001},
    {"race": "Saudi Arabia", "driver": "Charles Leclerc", "position": 4, "points": 12, "fastest_lap": 75.600},
    {"race": "Saudi Arabia", "driver": "Carlos Sainz", "position": 5, "points": 10, "fastest_lap": 76.100},

    {"race": "Australia", "driver": "Max Verstappen", "position": 1, "points": 25, "fastest_lap": 74.500},
    {"race": "Australia", "driver": "Lando Norris", "position": 2, "points": 18, "fastest_lap": 74.900},
    {"race": "Australia", "driver": "Lewis Hamilton", "position": 3, "points": 15, "fastest_lap": 75.300},
    {"race": "Australia", "driver": "Charles Leclerc", "position": 4, "points": 12, "fastest_lap": 75.800},
    {"race": "Australia", "driver": "Carlos Sainz", "position": 5, "points": 10, "fastest_lap": 76.200},
]
def total_points(data):
    totals = {}
    for row in data:
        driver = row["driver"]
        points = row["points"]
        if driver not in totals:
            totals[driver] = 0
        totals[driver] += points
    return totals
def fastest_laps(data):
    fastest = {}
    for row in data:
        driver = row["driver"]
        lap = row["fastest_lap"]
        if driver not in fastest:
            fastest[driver] = lap
        else:
            fastest[driver] = min(fastest[driver], lap)
        return fastest
def average_position(data):
    positions = {}
    counts = {}
    for row in data:
        driver = row["driver"]
        pos = row["position"]
        if driver not in positions:
            positions[driver] = 0
            counts[driver] = 0
        positions[driver] += pos
        counts[driver] += 1
    avg = {}
    for d in positions:
        avg[d] = round(positions[d] / counts[d], 2)
    return avg
def race_comparison(data):
    comparison = {}
    for row in data:
        driver = row["driver"]
        race = row["race"]
        pos = row["position"]
        if driver not in comparison:
            comparison[driver] = {}
        comparison[driver][race] = pos
    return comparison

print("\nTOTAL POINTS PER DRIVER")
totals = total_points(data)
for d, p in totals.items():
    print(f"{d}: {p} points")

print("\nFASTEST LAP PER DRIVER (smaller = faster)")
fastest = fastest_laps(data)
for d, f in fastest.items():
    print(f"{d}: {f} seconds")

print("\nAVERAGE FINISHING POSITION")
avg_pos = average_position(data)
for d, a in avg_pos.items():
    print(f"{d}: {a}")

print("\nRACE-BY-RACE COMPARISON")
comparison = race_comparison(data)
for d, races in comparison.items():
    print(f"\n{d}:")
    for race, pos in races.items():
        print(f"  {race}: P{pos}")