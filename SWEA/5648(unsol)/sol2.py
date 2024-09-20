from collections import defaultdict

def simulate_collisions(atoms):
    atoms = [[x*2, y*2, d, e] for x, y, d, e in atoms]
    total_energy = 0
    max_time = 4000  # Maximum time to simulate

    for _ in range(max_time):
        positions = defaultdict(list)
        for i, (x, y, direction, energy) in enumerate(atoms):
            if direction == 0: y += 1  # Up
            elif direction == 1: y -= 1  # Down
            elif direction == 2: x -= 1  # Left
            elif direction == 3: x += 1  # Right
            positions[(x, y)].append((i, x, y, direction, energy))

        collisions = set()
        for pos, atoms_here in positions.items():
            if len(atoms_here) > 1:
                collisions.update(atom[0] for atom in atoms_here)

        if collisions:
            total_energy += sum(atoms[i][3] for i in collisions)
            atoms = [atom for i, atom in enumerate(atoms) if i not in collisions]
            if not atoms:
                break

        new_atoms = []
        for atoms_at_pos in positions.values():
            if atoms_at_pos:  # Check if the list is not empty
                new_atoms.append(atoms_at_pos[0][1:])  # Take the first atom if multiple at same position
        atoms = new_atoms

        if not atoms:
            break

    return total_energy

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    atoms = [list(map(int, input().split())) for _ in range(N)]
    result = simulate_collisions(atoms)
    print(f'#{tc} {result}')