# --- ENHANCED DASHBOARD ---
if not data.empty:
    # 1. Calculate Distance & Efficiency
    data['Distance'] = data['Odometer'].diff()
    data['Kmpl'] = data['Distance'] / data['Litres']
    
    # 2. Calculate Cost per KM
    data['Cost_per_km'] = data['Cost'] / data['Distance']

    # 3. Display Key Metrics
    col1, col2, col3 = st.columns(3)
    
    # Latest Efficiency
    latest_kmpl = data['Kmpl'].iloc[-1]
    col1.metric("Fuel Economy", f"{latest_kmpl:.2f} km/L")
    
    # Latest Cost per KM
    latest_cpk = data['Cost_per_km'].iloc[-1]
    col2.metric("Running Cost", f"${latest_cpk:.2f}/km")
    
    # Total Monthly Spend
    monthly_spend = data['Cost'].sum()
    col3.metric("Total Spend", f"${monthly_spend:.2f}")

    # --- VISUALS ---
    st.subheader("Cost vs. Efficiency")
    # A dual-axis chart or comparison
    st.line_chart(data.set_index('Date')[['Kmpl', 'Cost_per_km']])
  
