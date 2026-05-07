import json
import sys

with open('outputs/metrics.json') as f:
    m = json.load(f)

acc = m.get('accuracy', 0)
print(f'accuracy = {acc:.4f}')

if acc < 0.50:
    print('Accuracy below threshold (0.50), failing')
    sys.exit(1)

print('OK')
