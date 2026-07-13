# VERIFICATION — <result>

> Stage 5. Independent of the code. Each check needs EVIDENCE (a number or a figure), never just an
> assertion. The result is final only when all five are ticked with evidence.

- [ ] **① Units / dimensions** — <quantity> has units [...]; checked via dimensional-analysis.
      evidence: ...
- [ ] **② Symmetries** — <operator> applied to H numerically; residual ‖·‖ = ...  (domain: which symmetries)
- [ ] **③ Known limit** — reduced to <limit>; got <number> vs published <number> (REFERENCES.md, cite).
- [ ] **④ Convergence** — knob <k>: curve `figures/conv_<k>.png`; measured order = ... (convergence-study)
- [ ] **⑤ Self-consistency** — <quantity A> = <quantity B>: <n> = <n>.

**Verdict:** PASS only if every box is ticked with its evidence. A passing in-code assert does NOT
substitute for a check here.
