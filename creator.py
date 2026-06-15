import random
import re

with open("base.txt", "r") as f:
    original = f.read()
    
offset_map = {}

def get_closest_offset(x, z):
    for (orig_x, orig_z), offset in offset_map.items():
        if abs(orig_x - x) < 0.05 and abs(orig_z - z) < 0.05:
            return offset
    new_offset = (random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1))
    offset_map[(x, z)] = new_offset
    return new_offset

def modify_line(match):
    command = match.group(1)
    x = float(match.group(2))
    y = float(match.group(3))
    z = float(match.group(4))
    rest = match.group(5)

    offset_x, offset_z = get_closest_offset(x, z)

    new_x = round(x + offset_x, 3)
    new_z = round(z + offset_z, 3)

    return f"{command}({new_x:.3f}, {y:.3f}, {new_z:.3f}, {rest}"

pattern = r"(\w+)\(\s*(-?\d+\.\d+),\s*(-?\d+\.\d+),\s*(-?\d+\.\d+),\s*(.*)"

modified_lines = []
for line in original.strip().split("\n"):
    new_line = re.sub(pattern, modify_line, line)
    modified_lines.append(new_line)

with open("strat.txt", "w") as f:
    f.write("\n".join(modified_lines))