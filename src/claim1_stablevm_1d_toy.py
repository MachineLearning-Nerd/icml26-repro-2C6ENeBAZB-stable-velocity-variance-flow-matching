"""Reduced CPU check of the StableVM self-normalized target (paper Eq. stablevm_target_def)."""
import csv, json, math, random
from pathlib import Path

OUT=Path(__file__).parents[1]/'outputs/claim1_stablevm_1d_toy'
def density(x, x0, t):
    s=t
    z=(x-(1-t)*x0)/s
    return math.exp(-.5*z*z)/s
def velocity(x,x0,t):
    # x_t=(1-t)x0+t eps, so d x_t/dt=eps-x0
    return (x-(1-t)*x0)/t-x0
def target(x, refs, t):
    ws=[density(x,r,t) for r in refs]
    return sum(w*velocity(x,r,t) for w,r in zip(ws,refs))/sum(ws)
def run(seed=20260803, trials=4000, t=.65):
    rng=random.Random(seed); rows=[]
    for n in (1,2,4,8,16,32):
        values=[]
        for _ in range(trials):
            refs=[rng.gauss(0,1) for _ in range(n)]
            j=rng.randrange(n); x=(1-t)*refs[j]+t*rng.gauss(0,1)
            values.append(target(x,refs,t))
        mean=sum(values)/trials; var=sum((v-mean)**2 for v in values)/(trials-1)
        rows.append({'n':n,'mean':mean,'sample_variance':var})
    OUT.mkdir(parents=True,exist_ok=True)
    config={'seed':seed,'trials':trials,'t':t,'path':'x_t=(1-t)x0+t epsilon','metric':'Monte-Carlo target variance; reduced diagnostic only'}
    (OUT/'config.json').write_text(json.dumps(config,indent=2)+'\n')
    with (OUT/'results.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    summary={'verdict':'toy','scope':'One-dimensional Gaussian CPU implementation of the paper self-normalized multi-reference target; it is not a proof of unbiasedness/O(1/n), nor ImageNet training.', 'rows':rows, 'variance_n1':rows[0]['sample_variance'],'variance_n32':rows[-1]['sample_variance'],'decreases_n1_to_n32':rows[-1]['sample_variance']<rows[0]['sample_variance']}
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
if __name__=='__main__': run()
