"""Write SYNTHETIC STA-DS input files (hand-made AOI sequences, not real data).

AOIs are cells of a 3x3 grid on the code: 0..8 -> A..I (row by row).
STA-DS reads column 0 = participant, 5 = fixation duration (ms), 6 = AOI index,
and filter columns 15-24 (all 0 here = no filtering).
"""
import sys

GROUPS = {
    # novice: line-by-line reading, top to bottom, with re-reading
    "novice": {
        "N1": "ABCDEFGHI",
        "N2": "ABCADEFGHI",
        "N3": "ABDEFEGHI",
        "N4": "ABCDEFGHGI",
    },
    # experienced: signature, then jump to the core logic block and the return
    "experienced": {
        "E1": "AEHEI",
        "E2": "AEHI",
        "E3": "ADEHI",
        "E4": "AEHEHI",
    },
}

def rows(seqs):
    yield "\t".join(f"c{i}" for i in range(25))
    for pid, seq in seqs.items():
        for k, aoi in enumerate(seq):
            f = ["0"] * 25
            f[0], f[5], f[6] = pid, str(200 + 50 * (k % 3)), str(ord(aoi) - ord("A"))
            yield "\t".join(f)

for name, seqs in GROUPS.items():
    with open(f"synthetic_{name}.tsv", "w") as fh:
        fh.write("\n".join(rows(seqs)))  # no trailing newline: STA-DS would read an empty record
    print(f"synthetic_{name}.tsv", len(seqs), "participants")
