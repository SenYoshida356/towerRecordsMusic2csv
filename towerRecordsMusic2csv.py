from bs4 import BeautifulSoup

# 入力ファイル名をコマンドライン引数から取得
import sys
if len(sys.argv) < 2:
    print("Usage: python towerRecordsMusic2csv.py [HTML file]")
    sys.exit()
filename = sys.argv[1]

# HTMLファイルを読み込む
with open(filename, "r", encoding="utf-8") as file:
    content = file.read()

# BeautifulSoupオブジェクトを作成
soup = BeautifulSoup(content, "html.parser")

# 曲名とアーティスト名を抽出
tracks = []
for item in soup.find_all("div", class_="c-grid__item"):
    track = {}
    track_title = item.find("h3", class_="c-media__title")
    artist_name = item.find("h4", class_="c-media__title-sub")
    if track_title and artist_name:
        track["title"] = track_title.get_text(strip=True)
        track["artist"] = artist_name.get_text(strip=True)
        tracks.append(track)

# 結果を200件ずつCSV形式で出力
import csv
for i in range(0, len(tracks), 200):
    outputfile = filename.replace(".html", f"_{i}.csv")
    with open(outputfile, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, ["title", "artist"])
        writer.writeheader()
        writer.writerows(tracks[i:i+200])
    print(f"{outputfile} saved.")