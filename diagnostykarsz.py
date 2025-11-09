#!/usr/bin/env python3
# diag_rsz_quick.py
# Szybki, jednoznaczny diagnostyk — natychmiast drukuje wynik dla 4 zestawów.

import math
from collections import Counter
from itertools import combinations
import sys

N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

def parse_hex(s):
    s = s.strip()
    if s.lower().startswith("0x"):
        return int(s, 16)
    return int(s, 16)

def bitlen(x): return x.bit_length()
def hamming(a,b): return (a ^ b).bit_count()
def ratio(a,b): return b / a if a != 0 else float("inf")
def rel_diff(a,b): return (b - a) / N

def byte_entropy(x):
    b = x.to_bytes((x.bit_length()+7)//8 or 1, "big")
    cnt = Counter(b)
    ent = 0.0
    L = len(b)
    for c in cnt.values():
        p = c / L
        ent -= p * math.log2(p)
    return ent * L

# --- YOUR DATA: 4 sets (label, r, s, z) ---
ENTRIES = [
    ("A1",
     "0x53133471acd440676d6694e40ff4563596734725860b2359a041083ed6023053",
     "0x5d3313bb527c38424cfdf0c3a2304ac2731ba136d662b5dabbc4d5ae1e790287",
     "0x64e929eff3671f88626bee3fe2db736d49b372601adb00ded461a262c34c9e41"),
    ("A2",
     "0x5443d5d7ed0a62d75c2a170b9334340baec3a8f8cbb13ad7f47ad1ba9f8638e1",
     "0x5ad8abf5c54985a01fc63731ecee345d950d88b1d9bc9e2a04e12858a3916d02",
     "0x77c027ad88d087b7aeeb234ecf4a2843fe0bfb7a3e101e9d278ac35b2fed2ab8"),
    ("B1",
     "0x53133471acd440676d6694e40ff4563596734725860b2359a041083ed6023053",
     "0x5d3313bb527c38424cfdf0c3a2304ac2731ba136d662b5dabbc4d5ae1e790287",
     "0x64e929eff3671f88626bee3fe2db736d49b372601adb00ded461a262c34c9e41"),
    ("B2",
     "0x5597f68cd265aa37ac3043254cb71ac8cba88c5c6e68acf533484f9f2c66dcf7",
     "0x5c34d09526f77b6c0f559077eefeca879c91e7f9a2ac188f5ae0515f8a1b1301",
     "0xcbced5156e107f898fbcefc32ee49b644987394215c6b08d45fb480c76aacee4"),
]

# parse to ints
items = []
for label, r, s, z in ENTRIES:
    try:
        items.append({
            "label": label,
            "r": parse_hex(r),
            "s": parse_hex(s),
            "z": parse_hex(z)
        })
    except Exception as e:
        print("Błąd parsowania danych:", e)
        sys.exit(1)

print("="*72)
print("Szybka diagnostyka RSZ — liczba wpisów:", len(items))
print("="*72)
# summary
rs = [it["r"] for it in items]
ss = [it["s"] for it in items]
zs = [it["z"] for it in items]
print("Duplikaty r:", len(rs) != len(set(rs)))
print("Duplikaty s:", len(ss) != len(set(ss)))
print("Duplikaty z:", len(zs) != len(set(zs)))
print("Rząd krzywej n bitlen:", N.bit_length())
print("="*72)

# pairwise
for (i,a), (j,b) in combinations(list(enumerate(items)), 2):
    la = a["label"]; lb = b["label"]
    r1 = a["r"]; r2 = b["r"]
    s1 = a["s"]; s2 = b["s"]
    z1 = a["z"]; z2 = b["z"]

    print(f"PARA: {la} <> {lb}")
    print("  r1:", hex(r1))
    print("  r2:", hex(r2))
    print("  bits r1:", bitlen(r1), " bits r2:", bitlen(r2))
    print("  ratio r2/r1: {:.6f}".format(ratio(r1, r2)))
    print("  abs diff r:", abs(r2 - r1))
    print("  rel diff (b-a)/n: {:.6e}".format(rel_diff(r1, r2)))
    print("  Hamming distance (r):", hamming(r1, r2))
    print("  r_equal:", r1 == r2, " s_equal:", s1 == s2, " z_equal:", z1 == z2)
    print("  Hamming(s):", hamming(s1, s2))
    print("  Entropy est r1:", round(byte_entropy(r1),2), " r2:", round(byte_entropy(r2),2))
    print("-"*72)

print("Koniec diagnostyki.")
