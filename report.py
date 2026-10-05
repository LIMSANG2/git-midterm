import csv
from pathlib import Path

menu_file = Path(__file__).resolve().parent / "menu.csv"   # 어디서 실행해도 같은 폴더의 menu.csv를 읽음
with open(menu_file, encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

prices = [int(r["가격"]) for r in rows]
print(f"메뉴 수: {len(rows)}")
print(f"평균 가격: {sum(prices) / len(prices):.0f}원")
