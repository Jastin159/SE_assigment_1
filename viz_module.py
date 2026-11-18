import json
import os
import matplotlib.pyplot as plt

DATA_FILE = "expenses.json"

def generate_pie_chart():
    # 檢查是否有資料檔案
    if not os.path.exists(DATA_FILE):
        print("找不到資料檔案 (expenses.json)，請先由 Member A 的輸入模組新增幾筆資料！")
        return

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            expenses = json.load(f)
        except json.JSONDecodeError:
            expenses = []

    if not expenses:
        print("目前沒有任何支出紀錄可供視覺化。")
        return

    # 依分類 (category) 加總金額 (amount)
    category_totals = {}
    for item in expenses:
        cat = item.get("category", "其他")
        amt = float(item.get("amount", 0))
        category_totals[cat] = category_totals.get(cat, 0.0) + amt

    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    # 繪製圓餅圖
    plt.figure(figsize=(8, 6))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title("Expense Distribution by Category")
    plt.axis('equal')
    
    # 儲存圖片（作業規定 README 需要一張圓餅圖截圖）
    plt.savefig("expense_pie_chart.png")
    print("圓餅圖已成功產生並儲存為 expense_pie_chart.png")
    
    # 顯示圖表視窗
    plt.show()

if __name__ == "__main__":
    generate_pie_chart()