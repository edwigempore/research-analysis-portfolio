"""Execute existing notebook code cells in IPython, without a notebook server.

Run from any directory: python scripts/verify_analysis.py instacart|telco-churn
Requires the exact private CSVs documented in the project data READMEs.
Local logs can contain source-row previews; never commit .verification/.
"""
import json
import os
from pathlib import Path
import re
import sys

from IPython.core.interactiveshell import InteractiveShell
from IPython.utils.capture import capture_output

ROOT = Path(__file__).resolve().parents[1]


def check_results(slug, records):
    text = '\n'.join(r['stdout'] + '\n' + '\n'.join(r['display']) for r in records)
    if slug == 'telco-churn':
        expected = [r'Test AUC: 0\.831', r'\[\[904\s+129\]\s*\[169\s+205\]\]',
                    r'Churned\s+0\.61\s+0\.55\s+0\.58\s+374']
    else:
        expected = [r'Selected lambda: 0\.25',
                    r'0\.25\s+0\.2719\s+0\.3530\s+0\.2645\s+0\.4070\s+0\.3464',
                    r'0\.00\s+0\.2594\s+0\.3359\s+0\.2518\s+0\.3889',
                    r'Global popularity\s+0\.0668\s+0\.0685\s+0\.0602',
                    r'NDCG@10: 0\.0918',
                    r'Item-item minus recency-frequency NDCG: -0\.3375',
                    r'95% interval: -0\.3455 to -0\.3296']
    for pattern in expected:
        if not re.search(pattern, text):
            raise AssertionError(f'Result differs from published precision: {pattern}')


def main(slug):
    if slug not in ('instacart', 'telco-churn'):
        raise SystemExit('Choose instacart or telco-churn')
    filenames = (['Telco-Customer-Churn.csv'] if slug == 'telco-churn' else
                 ['aisles.csv', 'departments.csv', 'order_products.csv', 'orders.csv', 'products.csv'])
    for filename in filenames:
        path = ROOT / 'projects' / slug / 'data' / filename
        if not path.exists():
            raise FileNotFoundError(f'Provide the exact source CSV: {path}')
    project = ROOT / 'projects' / slug
    os.chdir(project)
    notebook = json.loads((project / 'analysis.ipynb').read_text())
    shell = InteractiveShell.instance()
    records = []
    output = ROOT / '.verification'
    output.mkdir(exist_ok=True)
    for i, cell in enumerate(notebook['cells']):
        if cell['cell_type'] != 'code':
            continue
        with capture_output() as cap:
            result = shell.run_cell(''.join(cell['source']), store_history=False)
        records.append({'cell': i, 'stdout': cap.stdout, 'stderr': cap.stderr,
                        'display': [o.data.get('text/plain', '') for o in cap.outputs]})
        (output / f'{slug}.json').write_text(json.dumps(records, indent=2))
        if result.error_before_exec or result.error_in_exec:
            raise RuntimeError(f'Cell {i} failed; inspect local .verification/{slug}.json')
        print(f'{slug}: cell {i} passed', flush=True)
    check_results(slug, records)
    print(f'{slug}: all code cells passed; selected results match published precision.')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python scripts/verify_analysis.py instacart|telco-churn')
    main(sys.argv[1])
