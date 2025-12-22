import pandas as pd
from sqlalchemy import create_engine
from sklearn.linear_model import LinearRegression
import numpy as np

# 127.0.0.1  pass123
db_string = 'postgresql://postgres:pass123@127.0.0.1:5432/postgres'
db_conn = create_engine(db_string)

print("🚀 Connecting to Database...")

try:
   
    query = 'SELECT "Order Date", "sales" FROM "sales_data"'
    df = pd.read_sql(query, db_conn)
    print(f"✅ Raw Data Loaded! Records: {len(df)}")

   
    df = df.rename(columns={"sales": "Sales"})

  
    df['Order Date'] = pd.to_datetime(df['Order Date'].astype(str), format='%Y-%m-%d', errors='coerce')

    
    df = df.dropna(subset=['Order Date'])
    print(f"✅ Cleaned Data! Valid Records: {len(df)}")

    if len(df) > 0:
        # Monthly Aggregation
        monthly_sales = df.set_index('Order Date').resample('ME')['Sales'].sum().reset_index()
        monthly_sales['Time_Index'] = np.arange(len(monthly_sales))

        # --- 3. Train AI Model ---
        X = monthly_sales[['Time_Index']]
        y = monthly_sales['Sales']

        model = LinearRegression()
        model.fit(X, y)
        print("🤖 AI Model Trained Successfully!")

        # --- 4. Forecast ---
        next_month_index = monthly_sales['Time_Index'].max() + 1
        predicted_sales = model.predict([[next_month_index]])

        print("\n" + "="*40)
        print(f"🔮 Forecast for Next Month: ${predicted_sales[0]:,.2f}")
        print("="*40 + "\n")
    else:
        print("\n❌ Error: Still getting 0 records. Something is wrong with Date Parsing.")

except Exception as e:
    print("\n❌ Error Occurred:")
    print(e)