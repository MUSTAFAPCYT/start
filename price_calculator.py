def calculate_price():
    print("=== حاسبة أسعار آركيد ستور (Arcade Store) ===")
    
    # إدخال بيانات المنتج
    product_name = input("أدخل اسم المنتج (مثلاً: شحن ببجي، عجلة قيادة G29، إلخ): ")
    cost_price = float(input("أدخل سعر التكلفة الأساسي: "))
    profit_margin = float(input("أدخل نسبة الربح المطلوبة (%): "))
    extra_fees = float(input("أدخل أي رسوم إضافية (بوابات دفع، تكاليف شحن، إلخ) إن وجدت: ") or 0)

    # العمليات الحسابية
    profit_amount = cost_price * (profit_margin / 100)
    final_price = cost_price + profit_amount + extra_fees

    # عرض النتيجة النهائية
    print("\n" + "="*45)
    print(f"المنتج:            {product_name}")
    print(f"تكلفة المنتج:      {cost_price:.2f}")
    print(f"مقدار الربح:       {profit_amount:.2f}")
    print(f"الرسوم الإضافية:   {extra_fees:.2f}")
    print("-" * 45)
    print(f"سعر البيع النهائي: {final_price:.2f}")
    print("=" * 45)

if __name__ == "__main__":
    calculate_price()