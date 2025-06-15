
selected_columns = ['檢傷級數', '年齡', '性別', '心跳', '呼吸次數', '血壓(SBP)', '血壓(DBP)', '血氧濃度(%)', 'pH', 'Y']
df_selected = df[selected_columns]

df_selected['Y'] = df_selected['Y'].fillna(df_selected['Y'].mode()[0])