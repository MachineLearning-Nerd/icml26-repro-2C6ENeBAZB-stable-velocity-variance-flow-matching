"""Record why literal anchored Claim 3 cannot be run under the local-only policy."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'outputs/claim3_cpu_infeasibility'
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    source=ROOT/'evidence/source/arxiv-2602.05435-source.tar.gz'
    report={
      'claim':3,
      'verdict':'inconclusive',
      'scope':'Literal SiT-XL/2 Table-2 FID reproduction is CPU-infeasible under the local CPU/local GTX-1050-only policy; no surrogate is run.',
      'source_facts':{'model':'SiT-XL/2 (675M)','training_iterations':[100000,400000],'reported_repa_fid':[18.59,8.13],'reported_stablevm_fid':[17.12,7.58]},
      'local_resources':{'allowed':'local CPU/local GTX 1050 only','prohibited':['HF cpu-upgrade','HF Jobs','paid compute','remote compute']},
      'decision':'Do not attempt model training, 50k-sample FID, or represent a toy as Table-2 evidence.',
      'source_sha256':digest(source),
      'source_excerpt':'evidence/claim3_attempt1/source_locations.txt'
    }
    (OUT/'assessment.json').write_text(json.dumps(report,indent=2)+'\n')
    (OUT/'SHA256SUMS').write_text(hashlib.sha256((OUT/'assessment.json').read_bytes()).hexdigest()+'  assessment.json\n')
if __name__=='__main__':main()
