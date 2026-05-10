# Smart Life Toolbox - 3322 理財分配器 (進取實踐版)
def calculate_3322_pro():
    print("================================")
    print("   💰 3322 理財自動分配工具   ")
    print("================================")
    # 加入專業宣告，提升專案層次
    print("💡 產品哲學：這是一個針對『資產累積期』設計的進取型分配工具，")
    print("   適合低生活開銷、追求複利極大化的實踐者。")
    print("-" * 32)
    
    try:
        # 1. 輸入總額
        income = float(input("👉 請輸入本月預計存入總額 (元): "))
        
        # 2. 進行 3322 計算
        invest_steady = income * 0.3    # 穩健型資產 (例如：市值型 ETF)
        invest_growth = income * 0.3    # 成長型資產 (例如：全球/科技類)
        emergency_fund = income * 0.2   # 緊急預備金 (儲蓄)
        daily_expense = income * 0.2    # 生活雜支 (彈性支用)
        
        # 3. 顯示結果
        print("\n[ 📊 本月分配建議 ]")
        print(f"🔹 穩健型投資 (30%): {invest_steady:,.0f} 元")
        print(f"🔹 成長型投資 (30%): {invest_growth:,.0f} 元")
        print(f"🔹 緊急預備金 (20%): {emergency_fund:,.0f} 元")
        print(f"🔹 生活消費金 (20%): {daily_expense:,.0f} 元")
        print("-" * 32)
        
        # 4. 結餘試算功能
        print(f"💡 提示：本月生活預算為 {daily_expense:,.0f} 元")
        spent = float(input("👉 請輸入目前已花費金額 (若無請輸入 0): "))
        remains = daily_expense - spent
        
        if remains >= 0:
            print(f"✅ 剩餘額度: {remains:,.0f} 元，請繼續保持！")
        else:
            print(f"⚠️ 注意：已超支 {abs(remains):,.0f} 元，建議調整下月支出。")
            
        print("\n================================")
        print("    持續執行，就是致富的捷徑！   ")
        print("================================")

    except ValueError:
        print("❌ 錯誤：請輸入正確的數字格式。")

if __name__ == "__main__":
    calculate_3322_pro()
