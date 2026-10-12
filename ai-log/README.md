# ai-log

Exporty konverzací s AI, chronologicky.

| Soubor | Nástroj | Co obsahuje |
|---|---|---|
| [`00-claude-app-plan-build-orchestrace.md`](00-claude-app-plan-build-orchestrace.md) | aplikace Claude (agentní režim, propojená s mým Macem) | výběr zadání, rešerše a plán, schéma, pokyny pro agenty, instalace Claude Code, kód a testy, tři scouti, první (neúspěšný) pokus o triáž, runbook |
| `01-…` | Claude Code | první krok kódu (`config.py`, `validate.py`); export se nedochoval, práce je v commitech `7fff7cb` a `3cf6879` |
| `02-…` | Claude Code | běh pilotu podle runbooku R0–R8 (doplní se po dokončení příkazem `/export`) |

Volání nástrojů jsou v logu 00 zkrácená na jeden řádek, protože zapsané soubory jsou celé v git historii. Pokyny pro agenty jsou v logu celé.
