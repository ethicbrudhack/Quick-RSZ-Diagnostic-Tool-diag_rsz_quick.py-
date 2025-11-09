# ⚡ Quick RSZ Diagnostic Tool — `diag_rsz_quick.py`

> 🧠 **Ultra-fast diagnostic utility** for instant analysis of multiple  
> Bitcoin ECDSA signature parameter sets (`r`, `s`, `z`).  
>  
> Designed for **forensic crypto analysis**, **signature correlation**,  
> and **entropy testing** between suspected reused ECDSA values.

---

## 🚀 Overview

This standalone tool analyzes and compares up to **4 sets of ECDSA parameters (`r`, `s`, `z`)**  
used in Bitcoin or other SECP256k1-based cryptosystems.

It prints immediate diagnostic results, including:
- Duplicate detection (`r`, `s`, `z`)
- Bit lengths, ratios, and relative differences
- Hamming distances between parameters
- Approximate byte entropy
- Clear visual comparison between all pairs

The script executes **instantly** — no dependencies beyond standard Python libraries.

---

## ✨ Features

| Feature | Description |
|----------|-------------|
| ⚙️ **Pairwise Comparison** | Checks every combination of entries (4→6 pairs) |
| 🔍 **Duplicate Detection** | Flags identical `r`, `s`, or `z` values |
| 🧮 **Bit-level Analysis** | Computes bit length, Hamming distance, and ratio |
| 📊 **Entropy Estimation** | Approximates byte-level entropy per `r` |
| 🔢 **Relative Difference (mod n)** | Measures fractional difference over the SECP256k1 curve order |
| ⚡ **Instant Output** | Prints all diagnostics directly to console — no files |
| 🧠 **Forensic Precision** | Ideal for identifying reused nonces or weak signatures |

---

## 📂 File

| File | Description |
|------|-------------|
| `diag_rsz_quick.py` | Quick diagnostic script |
| `README.md` | Documentation (this file) |

---

## ⚙️ Usage

1. Open the script and replace the `ENTRIES` section with your own `(label, r, s, z)` tuples:

```python
ENTRIES = [
    ("TX1", "0x...", "0x...", "0x..."),
    ("TX2", "0x...", "0x...", "0x..."),
    ...
]
Run it directly from terminal:

python3 diag_rsz_quick.py


View instant structured output in your console.

🧩 Example Output
========================================================================
Szybka diagnostyka RSZ — liczba wpisów: 4
========================================================================
Duplikaty r: True
Duplikaty s: True
Duplikaty z: True
Rząd krzywej n bitlen: 256
========================================================================
PARA: A1 <> A2
  r1: 0x53133471acd440676d6694e40ff4563596734725860b2359a041083ed6023053
  r2: 0x5443d5d7ed0a62d75c2a170b9334340baec3a8f8cbb13ad7f47ad1ba9f8638e1
  bits r1: 255  bits r2: 255
  ratio r2/r1: 1.007993
  abs diff r: 726942733...
  rel diff (b-a)/n: 2.833e-06
  Hamming distance (r): 117
  r_equal: False  s_equal: False  z_equal: False
  Hamming(s): 131
  Entropy est r1: 1904.0  r2: 1904.0
------------------------------------------------------------------------
...
Koniec diagnostyki.

🧠 Technical Summary
ECDSA Context

In the Bitcoin ECDSA signature scheme, each signature is defined by:

r = (k·G).x mod n

s = k⁻¹(z + r·d) mod n

Where:

k → per-signature random nonce

z → message hash (double SHA256 of transaction data)

d → private key

G → generator point

n → curve order

Reusing or correlating r values between signatures leaks information about k and d,
and this tool helps detect such dangerous overlaps.

🧮 Core Functions
Function	Description
parse_hex()	Converts hex string to integer (handles 0x prefix)
bitlen(x)	Returns number of bits used by integer
hamming(a, b)	Counts bit differences between two integers
ratio(a, b)	Computes ratio b / a (or ∞ if a=0)
rel_diff(a, b)	Relative difference modulo curve order
byte_entropy(x)	Shannon entropy estimate per byte sequence
combinations()	Iterates through all pair comparisons
⚡ Performance

Pure Python — zero external dependencies

Runs in under 0.1s on standard systems

Memory footprint negligible (<10KB)

Ideal for offline analysis of captured signatures

🔒 Ethical Use Notice

This script serves as an educational and diagnostic tool
for analyzing ECDSA parameters. It performs no key recovery
and should never be used for unauthorized cryptographic analysis.

You may:

Validate signature randomness and uniqueness.

Compare or audit digital signatures for research.

You must not:

Use it for key recovery, data theft, or any unethical activity.

⚖️ Respect privacy and legal boundaries.

🪪 License

MIT License
© 2025 — Author: [Ethicbrudhack]

💡 Summary

This is a micro-diagnostic framework for cryptographic researchers —
instantly analyzing relationships between ECDSA parameters.

“Entropy doesn’t lie — it only reveals.”
— [Ethicbrudhack]
