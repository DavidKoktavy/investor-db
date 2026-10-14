# ai-log

Exporty konverzací s AI, chronologicky.

| Soubor | Nástroj | Co obsahuje |
|---|---|---|
| [`00-claude-app-plan-build-orchestrace.md`](00-claude-app-plan-build-orchestrace.md) | aplikace Claude (agentní režim, propojená s mým Macem) | výběr zadání, rešerše a plán, schéma, pokyny pro agenty, instalace Claude Code, kód a testy, tři scouti, první (neúspěšný) pokus o triáž, runbook |
| — | Claude Code | první krok kódu (`config.py`, `validate.py`); export se nedochoval, práce je v commitech `7fff7cb` a `3cf6879` |
| [`01-pilot-r0-r8.md`](01-pilot-r0-r8.md) | Claude Code (`/export`) | běh pilotu: triáž, extrakce, kontrola citací, ověření, rozhodnutí, opravný průchod (R0–R8 a repair_01; zápis výsledků ruční kontroly a R9 proběhly až po exportu) |

Volání nástrojů jsou v logu 00 zkrácená na jeden řádek, protože zapsané soubory jsou celé v git historii. Pokyny pro agenty jsou v logu celé.
