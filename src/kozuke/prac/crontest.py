import datetime
from pathlib import Path

print('exec from cron')
now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

with open(Path(__file__).parent / f'{now}.txt', 'w') as f:
    f.write('test')

print('end')
