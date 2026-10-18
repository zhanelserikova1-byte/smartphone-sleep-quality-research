"""Reproducible descriptive pilot benchmark. Synthetic data are not evidence."""
import csv
import json
import math
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parent.parent

def pearson(xs, ys):
    mx, my = mean(xs), mean(ys)
    numerator = sum((x-mx)*(y-my) for x,y in zip(xs,ys))
    denominator = math.sqrt(sum((x-mx)**2 for x in xs)*sum((y-my)**2 for y in ys))
    return numerator/denominator if denominator else None

def main():
    config = json.loads((ROOT/'configs/config.json').read_text(encoding='utf-8'))
    with (ROOT/config['data_path']).open(encoding='utf-8-sig',newline='') as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise ValueError('Dataset is empty')
    required = {'screen_time_hours','psqi_score','disconnection_minutes',
                'sleep_latency_minutes','sleep_efficiency_percent','usage_mode'}
    if not required.issubset(rows[0]):
        raise ValueError('Missing columns: '+str(sorted(required-set(rows[0]))))
    valid=[]
    for row in rows:
        try:
            x=float(row['screen_time_hours'])
            p=float(row['psqi_score'])
            d=float(row['disconnection_minutes'])
            latency=float(row['sleep_latency_minutes'])
            efficiency=float(row['sleep_efficiency_percent'])
            if (not all(map(math.isfinite,[x,p,d,latency,efficiency]))
                or x<0 or not 0<=p<=21 or d<0 or latency<0
                or not 0<=efficiency<=100
                or row['usage_mode'] not in ('active','passive','none')):
                continue
            valid.append((x,p,d,latency,efficiency,row['usage_mode']))
        except (ValueError,TypeError,KeyError):
            continue
    missing_pct=100*(len(rows)-len(valid))/len(rows)
    if len(valid)<config['minimum_sample_size']:
        raise ValueError('Not enough valid rows')
    xs=[r[0] for r in valid]; ys=[r[1] for r in valid]
    disconnected=[r for r in valid if r[2]>=config['disconnection_threshold_minutes']]
    connected=[r for r in valid if r[2]<config['disconnection_threshold_minutes']]
    def summary(group):
        return {'n':len(group),'mean_psqi':round(mean(r[1] for r in group),3) if group else None,
                'good_sleep_rate':round(sum(r[1]<=config['good_sleep_psqi_threshold'] for r in group)/len(group),3) if group else None}
    results={
        'dataset_kind':'synthetic_demo_only',
        'hypothesis_test_status':'not_performed',
        'n_total':len(rows),'n_valid':len(valid),
        'invalid_or_missing_percent':round(missing_pct,2),
        'guardrail_passed':missing_pct<=config['missing_data_threshold_percent'],
        'primary_metric_pearson_r':round(pearson(xs,ys),4) if pearson(xs,ys) is not None else None,
        'mean_screen_time_hours':round(mean(xs),2),
        'mean_psqi':round(mean(ys),2),
        'disconnection_30plus_minutes':summary(disconnected),
        'disconnection_under_30_minutes':summary(connected),
        'note':'No p-values or causal conclusions are computed from synthetic pilot data.'
    }
    dest=ROOT/config['output_path']
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(results,indent=2))
    print('Saved to:',dest)

if __name__=='__main__':
    main()
