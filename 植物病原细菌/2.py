import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import matplotlib.font_manager as fm
#在图标中间显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']    # Set the font to SimHei for Chinese characters.
plt.rcParams['axes.unicode_minus'] = False      # Ensure that minus signs are displayed correctly.

# Read the Excel file
df2 = pd.read_excel('附件2.xlsx', sheet_name='Sheet1', header=1, nrows=5)




# === 步骤 1: 读取并清洗数据 ===
# 使用我们之前确定的最佳方法
df2 = pd.read_excel(
    '附件2.xlsx',
    skiprows=1,   # 跳过总标题
    nrows=5,      # 读取表头+4行数据
    index_col=0   # 温度列作为索引
)

# 清洗列名 (时间)
df2.columns = df2.columns.str.replace('h', '').astype(int)
# 清洗索引 (温度)
df2.index = df2.index.str.replace('°C', '')

print("原始数据 (行:温度, 列:时间):")
print(df2)


# === 步骤 2: 转置数据以便于绘图 ===
# .T 是转置操作
df2_transposed = df2.T
print("\n转置后的数据 (行:时间, 列:温度):")
print(df2_transposed)


# === 步骤 3: 循环绘制曲线 ===
plt.figure(figsize=(12, 8)) # 创建一个大一点的画布

# 遍历转置后DataFrame的每一列（每一列代表一个温度）
for temp_col in df2_transposed.columns:
    plt.plot(
        df2_transposed.index,              # X轴：时间 (转置后的索引)
        df2_transposed[temp_col],          # Y轴：细菌数量 (当前列的数据)
        marker='o',                        # 在每个数据点上加个圆圈标记
        linestyle='-',                     # 用实线连接数据点
        label=f'{temp_col}°C'              # 图例标签，例如 "20°C"
    )

# === 步骤 4: 美化图表 ===
plt.title('不同温度下病原细菌生长曲线', fontsize=16)
plt.xlabel('时间 (小时)', fontsize=12)
plt.ylabel('细菌数量 (个)', fontsize=12)

# 使用对数坐标轴，因为细菌数量级差别太大
# 这样可以更清楚地看到初期的增长情况
plt.yscale('log')
plt.ylabel('细菌数量 (个) - 对数坐标', fontsize=12) # 更新Y轴标签

plt.grid(True, which="both", ls="--", alpha=0.5) # 显示网格线，'both'对主次刻度都有效
plt.legend(title='培养温度') # 显示图例
plt.show() # 显示图像

