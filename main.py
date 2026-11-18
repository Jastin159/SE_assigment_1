from input_module import save_expense
from viz_module import generate_pie_chart

def main():
    while True:
        print("\n=== 簡易記帳工具 ===")
        print("1. 新增支出")
        print("2. 產生分類圓餅圖")
        print("3. 離開")
        choice = input("請選擇功能 (1-3): ")

        if choice == "1":
            date = input("日期 (YYYY-MM-DD): ")
            amount = input("金額: ")
            category = input("分類: ")
            notes = input("備註 (選填): ")
            save_expense(date, amount, category, notes)
        elif choice == "2":
            generate_pie_chart()
        elif choice == "3":
            print("再見！")
            break
        else:
            print("無效的選擇，請重新輸入。")

if __name__ == "__main__":
    main()