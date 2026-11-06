"""Render portfolio figures from saved outputs only; never execute notebook cells.

Run from the repository root: python scripts/render_portfolio_figures.py
Requires matplotlib for the Instacart summary chart.
"""
import base64
import json
import re
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]


def read_notebook(project):
    return json.loads((ROOT / 'projects' / project / 'analysis.ipynb').read_text())


def output_text(cell):
    return '\n'.join(
        ''.join(output.get('text', [])) +
        ''.join(output.get('data', {}).get('text/plain', []))
        for output in cell.get('outputs', [])
    )


def instacart_figure():
    notebook = read_notebook('instacart')
    comparison = next(output_text(cell) for cell in notebook['cells']
                      if 'Item-item minus recency-frequency NDCG:' in output_text(cell))
    labels = ['Recency-frequency', 'Repeat frequency', 'Global popularity', 'Item-item CF']
    values = []
    for label in labels:
        match = re.search(r'^' + re.escape(label) + r'\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)', comparison, re.M)
        if match is None:
            raise ValueError(f'Missing saved comparison row: {label}')
        values.append(float(match.group(4)))
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
    fig, ax = plt.subplots(figsize=(9, 4.7))
    bars = ax.barh(labels, values, color=['#0072B2', '#64748B', '#64748B', '#64748B'], height=0.58)
    ax.invert_yaxis()
    ax.set_xlim(0, 0.5)
    ax.set_xlabel('Mean validation NDCG@10 (higher is better)', labelpad=12)
    ax.set_title('Instacart: next-basket validation', loc='left', pad=32, fontweight='bold', fontsize=16)
    ax.text(0, 1.045, '4,994 customers with eligible targets · K = 10', transform=ax.transAxes, fontsize=11, color='#334155')
    ax.bar_label(bars, labels=[f'{v:.4f}' for v in values], padding=7, fontsize=12)
    ax.xaxis.grid(True, color='#E2E8F0')
    ax.set_axisbelow(True)
    ax.tick_params(axis='both', length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    fig.text(0.04, 0.025, 'Recreated from saved summary results; no analysis rerun. Final-test baskets remain unused.', fontsize=10, color='#334155')
    fig.tight_layout(rect=(0.02, 0.07, 0.98, 1))
    target = ROOT / 'projects/instacart/figures/validation-ndcg.png'
    target.parent.mkdir(exist_ok=True)
    fig.savefig(target, dpi=180, facecolor='white')
    plt.close(fig)


def telco_figure():
    notebook = read_notebook('telco-churn')
    evaluation = next(c for c in notebook['cells'] if 'Test AUC:' in output_text(c))
    images = [o['data']['image/png'] for o in evaluation['outputs'] if 'image/png' in o.get('data', {})]
    # Evaluation emits the confusion matrix first, then the ROC curve.
    if len(images) != 2:
        raise ValueError('Expected the saved confusion matrix and ROC images.')
    target = ROOT / 'projects/telco-churn/figures/test-roc.png'
    target.parent.mkdir(exist_ok=True)
    target.write_bytes(base64.b64decode(''.join(images[1])))


if __name__ == '__main__':
    instacart_figure()
    telco_figure()
    print('Created figures from saved outputs only.')
