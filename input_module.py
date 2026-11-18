import json
import os

DATA_FILE = "expenses.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_expense(date, amount, category, notes=""):
    expenses = load_data()
    new_expense = {
        "date": date,
        "amount": float(amount),
        "category": category,
        "notes": notes
    }
    expenses.append(new_expense)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(expenses, f, ensure_ascii=False, indent=4)
    print("支出新增成功！")

if __name__ == "__main__":
    print("--- 新增支出測試 ---")
    date = input("請輸入日期 (YYYY-MM-DD): ")
    amount = input("請輸入金額: ")
    category = input("請輸入分類 (例如: 食物, 交通): ")
    notes = input("請輸入備註 (選填): ")
    save_expense(date, amount, category, notes)