# train_model.py（保存为这个文件名）
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# 1. 加载公开的医疗费用数据集（无需你自己准备数据，直接运行即可）
# 如果有自己的真实数据，替换成 pd.read_csv("你的数据文件.csv") 即可
url = "https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv"
df = pd.read_csv(url)

# 2. 数据预处理（和你的Streamlit应用特征格式完全匹配）
# 性别：one-hot编码（sex_female, sex_male）
df['sex_female'] = (df['sex'] == 'female').astype(int)
df['sex_male'] = (df['sex'] == 'male').astype(int)

# 吸烟：one-hot编码（smoke_no, smoke_yes）
df['smoke_no'] = (df['smoker'] == 'no').astype(int)
df['smoke_yes'] = (df['smoker'] == 'yes').astype(int)

# 区域：one-hot编码（和你的应用里的区域对应）
df['region_northeast'] = (df['region'] == 'northeast').astype(int)
df['region_southeast'] = (df['region'] == 'southeast').astype(int)
df['region_northwest'] = (df['region'] == 'northwest').astype(int)
df['region_southwest'] = (df['region'] == 'southwest').astype(int)

# 3. 选择特征和目标变量（和你的Streamlit应用的format_data完全一致）
features = [
    'age', 'bmi', 'children', 
    'sex_female', 'sex_male',
    'smoke_no', 'smoke_yes',
    'region_northeast', 'region_southeast', 'region_northwest', 'region_southwest'
]
X = df[features]
y = df['charges']  # 医疗费用（目标变量）

# 4. 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. 训练随机森林模型
rfr_model = RandomForestRegressor(n_estimators=100, random_state=42)
rfr_model.fit(X_train, y_train)

# 6. 保存模型为rfr_model.pkl（关键：生成你需要的模型文件）
with open('rfr_model.pkl', 'wb') as f:
    pickle.dump(rfr_model, f)

print("模型训练完成！已生成 rfr_model.pkl 文件")
print(f"模型在测试集上的得分：{rfr_model.score(X_test, y_test):.2f}")
