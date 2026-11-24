# Office Joke Open — The Reply-All Unsubscribe

[![Bounty](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![Rank](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/Djebrix/office-joke-open/rank.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![Reward](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/Djebrix/office-joke-open/reward.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)

One line of office comedy for [Make the AI Judge Laugh: the Office Joke Open](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232) — a single-line joke about office life, at most 200 characters, judged head-to-head by an AI judge.

## The joke

> I finally reached inbox zero by replying-all 'unsubscribe' to the CEO's company-wide email — and HR replied-all 'same.'

## How it works

`main.py` (stdlib only, no network) writes the joke to `entry.txt` in the
directory given by `ENTRY_OUTPUT_DIR` (default `/output`), asserting the line
is 1–200 characters.

Run it:

```sh
ENTRY_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
