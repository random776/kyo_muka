# kyo_muka
pythonとLine notify apiを用いて、東京大学教養学部の教務課のお知らせを10分に1回定点観測するツールです。
## 仕様
### 各ファイルの紹介
main.py 東京大学教養学部の教務課ホームページ https://www.c.u-tokyo.ac.jp/zenki/index.htmlの「お知らせ」欄の変化を感知し、Line notify経由で伝達します。
sub.py main.pyの機能を、timeやscheduleモジュールを用いて、継続的に実行するための装置です。
old_elem.xlsx 本ツールのデータベース部分です。このデータを鋳型として main.pyによって取得されたデータと比較し、変化を読み取ります。

### 使用方法：これから編集します。

## なぜこんなものが必要なのか
東京大学教養学部の教務課は、基本的に連絡事項をホームページで確認し忘れても自己責任だとする姿勢です。これに対処するため、ホームページを定点観測できるようにして、
チェックし忘れを防ぐことができます。