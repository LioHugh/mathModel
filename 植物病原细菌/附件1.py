import pandas as pd
import matplotlib.pyplot as plt
#在图标中间显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']    # Set the font to SimHei for Chinese characters.
plt.rcParams['axes.unicode_minus'] = False      # Ensure that minus signs are displayed correctly.

# Read the Excel file
df1 = pd.read_excel('附件1.xlsx', sheet_name='Sheet1',header=1,usecols='B:D')

# Preprocess the DataFrame
time_series = df1['时间']
temp_series = df1['温度(℃)']
humidity_series = df1['相对湿度RH（%）']

time_obj = pd.to_datetime(time_series, format='   %H:%M:%S').dt
time_hours = time_obj.hour + time_obj.minute / 60 + time_obj.second / 3600

# 3. 准备建模用的数据
x_data = time_hours.values    # 转换为Numpy数组
y_temp_data = temp_series.values     # 转换为Numpy数组
y_humidity_data = humidity_series.values # 转换为Numpy数组

# --- 创建图表和第一个Y轴 (温度) ---
fig, ax1 = plt.subplots(figsize=(12, 6))

# 绘制温度曲线
color = 'tab:red'
ax1.set_xlabel('时间 (小时)')
ax1.set_ylabel('温度 (℃)', color=color)
line1 = ax1.plot(x_data, y_temp_data, color=color, label='温度')
ax1.tick_params(axis='y', labelcolor=color)

# --- 创建第二个Y轴 (相对湿度) ---
ax2 = ax1.twinx()  # 创建一个共享X轴的第二个Y轴
color = 'tab:blue'
ax2.set_ylabel('相对湿度RH (%)', color=color)
line2 = ax2.plot(x_data, y_humidity_data, color=color, label='相对湿度')
ax2.tick_params(axis='y', labelcolor=color)

# --- 美化图表 ---
plt.title('温度与相对湿度随时间变化图')
# 为了在一个图例中同时显示两条线，我们需要手动合并它们
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left')

plt.grid(True)  # 添加网格线
fig.tight_layout()  # 自动调整布局以避免标签重叠

plt.show()  # 显示图形