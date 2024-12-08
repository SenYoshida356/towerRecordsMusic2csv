# towerRecordsMusic2csv

[Tower Records Music](https://music.tower.jp/home)のプレイリストを、[Soundiiz](https://soundiiz.com/)でインポート可能なCSV形式に変換するPythonスクリプト

## 使い方

- PCのブラウザでTower Records Musicにログインし、変換したいプレイリストを表示。「名前を付けて保存」でHTMLファイルを保存。
- python towerRecordsMusic2csv.py [HTMLファイル名]
- 生成されたCSVをSoundiizでインポートし、任意の音楽サービス向けに変換。
