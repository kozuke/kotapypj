import zipfile
import os.path
import urllib.request as req
from commonlib import analyze_text

url = 'http://www.aozora.gr.jp/cards/000081/files/456_ruby_145.zip'
local = '456_ruby_145.zip'
if not os.path.exists(local):
    print('ZIPファイルをダウンロード')
    req.urlretrieve(url, local)

zf = zipfile.ZipFile(local, 'r')
fp = zf.open('gingatetsudono_yoru.txt', 'r')
bindata = fp.read()
txt = bindata.decode('shift-jis')

analyze_text.janome_analyze(txt)
