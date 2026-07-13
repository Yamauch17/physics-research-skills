# PLAN — <calculation>

> Stage 3. References DERIVATION.md. Plan the verification BEFORE writing the code it tests.

## Modules (each cites DERIVATION.md rows/equations)
1. model builder — eqs (...), conventions C1..C6
2. observables — ...
3. invariants / derived quantities — ...

## Verification plan (Stage 5 gates — write them NOW)
- ① units: ...
- ② symmetries: ...
- ③ known limit: reduce to <benchmark>, expect <number> (REFERENCES.md)
- ④ convergence: scan <knobs>, expect order <n>
- ⑤ self-consistency: <A> == <B>

## Acceptance
Each deliverable notebook ends with an assert cell encoding the gates above
(see jupytext-notebook-workflow); a failed assert blocks the next phase.
