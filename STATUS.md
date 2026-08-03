# Status
- OpenReview ID: `2C6ENeBAZB`; 6 anchored claims / 12 maximum points.
- Source pinned: arXiv 2602.05435 PDF/source archive under `evidence/source/`.
- Compute: local CPU/local GTX 1050 only; no HF cpu-upgrade, Jobs, paid, or remote compute.
- Claim 1: **toy**. A source-mapped 1-D Gaussian StableVM self-normalized target fixture uses n=1..32 reference samples and retains its finite Monte-Carlo variance diagnostic. It is not a theorem proof or ImageNet reproduction.
- Next: independent Claim-1 review before Claim 2 CPU-feasibility/source audit. Publication blocked.
- Claim 2: **inconclusive / CPU-infeasible**. Literal Table-1 requires ImageNet training, SiT-XL, 80 epochs, and FID/IS over 50K generated samples. This is not feasible on local CPU/GTX 1050; no remote/HF/paid compute or misleading surrogate was used. Evidence: `evidence/claim2_attempt1/source_locations.md`, `outputs/claim2_cpu_infeasibility/assessment.json`.
- Claim 3: **inconclusive / CPU-infeasible**. Literal Table-2 requires SiT-XL/2 (675M) training through 100k/400k iterations and FID evaluation. This is unavailable under local CPU/GTX-1050-only policy; no remote compute or misleading toy substitute was run. Evidence: `evidence/claim3_attempt1/source_locations.txt`, `outputs/claim3_cpu_infeasibility/assessment.json`.
