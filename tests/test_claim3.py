import json
from pathlib import Path
p=Path(__file__).parents[1]/'outputs/claim3_cpu_infeasibility/assessment.json'
d=json.loads(p.read_text())
assert d['verdict']=='inconclusive'
assert d['source_facts']['model']=='SiT-XL/2 (675M)'
assert d['source_facts']['training_iterations']==[100000,400000]
assert 'remote compute' in d['local_resources']['prohibited']
