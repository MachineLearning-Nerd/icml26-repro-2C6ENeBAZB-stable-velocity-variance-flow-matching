import hashlib,json
from pathlib import Path
ROOT=Path(__file__).parents[1]
p=ROOT/'outputs/claim2_cpu_infeasibility/assessment.json'
d=json.loads(p.read_text())
assert d['claim']==2 and d['verdict']=='inconclusive'
assert d['literal_requirements']['evaluation'].startswith('FID and IS over 50000')
for line in (ROOT/'outputs/claim2_cpu_infeasibility/SHA256SUMS').read_text().splitlines():
 h,name=line.split(maxsplit=1); assert hashlib.sha256((ROOT/'outputs/claim2_cpu_infeasibility'/name.strip()).read_bytes()).hexdigest()==h
