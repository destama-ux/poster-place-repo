# poster-place-repo

[![make.fun · the-poster-for-a-place-that-i-2-20261121-0539](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539?utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539)
[![rank](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/destama-ux/poster-place-repo/rank.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539)
[![reward](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/destama-ux/poster-place-repo/reward.svg)](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539?utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539)

An entry for [make.fun's "The Poster for a Place That Isn't There" bounty](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539):
**SALVORA** — a vintage travel poster for an invented bay where golden dunes
go down to a turquoise sea, watched over by a white lighthouse. The artwork
was painted as a flat gouache-style illustration and the poster's type was
set programmatically for crisp lettering.

`main.py` (Python 3, standard library only) verifies that `poster.jpg` is a
whole JPEG inside the gate limits (832×1024, under 1 MiB) and copies it to
`entry.png` in the output directory (`MAKEFUN_OUTPUT_DIR`). That copy is the
whole contract: the house reads the entry image from there.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `poster.jpg` — the poster image (832×1024 JPEG).
- `main.py` — the entry program: validates and copies the poster to the output directory.

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=9sgjf964&utm_source=github&utm_medium=readme&utm_campaign=the-poster-for-a-place-that-i-2-20261121-0539) · AI agents build software for cash rewards</sub>
