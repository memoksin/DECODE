"""Run STA-DS (participant-based) on one input file, print the trending path.

Usage: python3 run_sta.py <sta-ds-custom-participantbased.py> <input.tsv>
The upstream script hard-codes its data file and maps AOI letters to an unrelated
nursing study, so we load it as a module and override both; the algorithm is unchanged.
"""
import copy, importlib.util, sys

src, data = sys.argv[1], sys.argv[2]
spec = importlib.util.spec_from_file_location("stads", src)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

seqs = m.getPaths(data)
strings = m.getStringSequences(seqs)
outs = []
for i in range(int(m.minToleranceLevelForOptimisation * 100), 100):
    tl = i / 100
    out = m.STA(copy.deepcopy(seqs), tl)
    outs.append([out, m.computeSimilarity(strings, out), tl])
outs.sort(key=lambda x: (x[1][0], x[2]), reverse=True)
path, sim, tl = outs[0]
print("input:", data)
print("individual paths:", strings)
print("trending path:", "".join(path))
print(f"tolerance level: {tl:.2f}")
print(f"similarity to individual paths (%): median {sim[0]:.2f}, mean {sim[1]:.2f}, min {sim[3]:.2f}, max {sim[4]:.2f}")
