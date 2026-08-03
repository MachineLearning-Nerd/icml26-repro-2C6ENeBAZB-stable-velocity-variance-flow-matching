import csv, json, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/'src'))
from claim1_stablevm_1d_toy import run, OUT
run()
rows=list(csv.DictReader((OUT/'results.csv').open()))
assert len(rows)==6
assert json.loads((OUT/'summary.json').read_text())['verdict']=='toy'
assert float(rows[-1]['sample_variance']) < float(rows[0]['sample_variance'])
