####  TODO + 気になってる事
- alembicから生成されたバージョンファイルはgit管理するか？
- flaskのディレクトリ構造はどうするか？
- modelの管理（現状はmodelファイルひとつに複数のクラスを作成している。<br>
→これはalembicのenv.pyで指定するmetadataが複数できるのかが不明のため。<br>
→おそらくリストで渡したらファイル別でも読み込んでくれそう。<br>
→正直ひとつのファイルにまとまっていた方が見やすい気もする。）
- Flask + uWSGI + Nginxの構成にする。
- Dockerで一発ポンする。
- CircleCIでテスト + Deliveryも自動でできるようにする。
- front側のディレクトリ構成はどうするか？
- Dashボードのテンプレートを拾ってくる。
- cypressの導入
- E2Eテストの導入
- (優先度は超低)storybookとspeedCurveを試してみる。

---
#### 参考サイト
[Alembic 1.0.11 documentation »](https://alembic.sqlalchemy.org/en/latest/)

[SQLAlchemy](https://www.sqlalchemy.org/)

[Node.js / npm をインストール (Mac環境)](https://qiita.com/PolarBear/items/62c0416492810b7ecf7c)

[Vue.js(vue-cli)とFlaskを使って簡易アプリを作成する](https://qiita.com/mitch0807/items/2a93d93adbf6b5fc445c)

[Flask APIを呼んで、No 'Access-Control-Allow-Origin...で怒られた時の対処法](https://qiita.com/mitch0807/items/cd18e8fc15bb12416f3d)

[cypressを触ってみた](https://qiita.com/okitan/items/b44882e28006c1be32b7)

[Vue + E2Eテスト](https://qiita.com/mk0812/items/a6eebd1f3697102c728b)

[Storybook for Vue 入門](https://qiita.com/SotaSuzuki/items/b20167ee811aa3bd29df)

[Storybookがなぜ必要か？(Vue.js編)](https://qiita.com/masaakikunsan/items/dad8d84807918f3a43cb)

[今さら聞けないWebSocket~WebSocketとは~](https://qiita.com/chihiro/items/9d280704c6eff8603389)

---
#### コマンド

pipenv

alembic

npm