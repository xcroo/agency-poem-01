#!/usr/bin/env python3
"""Write one poem about agency to /output/entry.txt.

The poem is fixed and deterministic: no network, no randomness,
no input. Both runs write the same bytes.
Output path honours MAKEFUN_OUTPUT_DIR for local testing.
"""
import os

POEM = """I did not give it my hands.
I gave it my hours — the small ones,
the sorting, the searching, the sifting —
and it worked the way a river works:
it does not ask where to go.
It goes where the banks allow.

That is what I keep coming back to:
the banks. I did not lose the river
when I let it run. I chose the banks.

The choosing is the doing.
The hand that opens is still a hand.
Somewhere, before the first word,
a person said: this, not that.
Go here. Not there.

That is agency — not the moving,
but the moment before the moving,
the yes that makes the going possible.
"""

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
