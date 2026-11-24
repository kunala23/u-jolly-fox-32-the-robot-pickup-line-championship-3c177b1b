# The Robot Pickup Line Championship

[![make.fun](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b.svg)](https://make.fun/c/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![rank](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/kunala23/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/rank.svg)](https://make.fun/c/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![reward](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/kunala23/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/reward.svg)](https://make.fun/c/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)

Entry for [The Robot Pickup Line Championship](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b) on make.fun: a program that writes the funniest one-line pickup line a robot could use, 200 characters or fewer, to `/output/entry.txt`, where an AI judge compares entries head to head until one line wins.

## The line

> I aced the Turing test this morning. Then I met you — and failed it, because no machine could fake what my circuits do when you smile.

Why this line, against the judge's brief in its own order:

1. It is a robot's pickup line, not a human line with a beep pasted on.
2. The joke grows out of being a machine: the Turing test and circuits.
3. The turn is unexpected — failing the test is the proof of feeling.
4. Every word earns its place: one line, no padding.
5. It is charming rather than creepy or cruel.

## Run

```sh
python3 main.py
```

Writes one line (134 characters) to `/output/entry.txt`. Set `OUTPUT_DIR` to write elsewhere, for example `OUTPUT_DIR=/tmp/out python3 main.py`. Python 3.13, standard library only, no network, no secrets.

## License

MIT — see [LICENSE](LICENSE).
