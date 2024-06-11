import data
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import tree


# 데이터 가져오기
x_1 = list(zip(data.zero_types, data.moistures, data.salty_taste, data.ingredients, [99] * len(data.zero_types), [99] * len(data.zero_types)))
x_2 = list(zip(data.one_types, data.moistures, [99] * len(data.one_types), [99] * len(data.one_types), data.amount_of_cream, data.sugar_content))
x = x_1 + x_2

y_1 = data.zero_preferences
y_2 = data.one_preferences
y = y_1 + y_2

# 훈련 데이터와 테스트 데이터로 분할
x_input, y_test, x_target, y_target = train_test_split(x, y, test_size=0.2, random_state=30)


# 의사결정나무 적합 및 학습데이터 예측
clf = tree.DecisionTreeClassifier()
clf.fit(x_input, x_target)

print("훈련 점수 : ", clf.score(x_input, x_target))
# print("테스트 점수 : ", clf.score(y_test, y_target))


# 분류할 데이터
new_data = [(0, 3, 1, 0, 99 * len(data.zero_types), 99 * len(data.zero_types)), (1, 4, 99 * len(data.zero_types), 99 * len(data.zero_types), 4, 4)]
predictions = clf.predict(new_data)
#print("분류 결과(0 : NO 1 : YES) : ", predictions)

columns = ["types", "moistures", "salty_taste", "ingredients", "amount_of_cream", "sugar_content"]

# # 트리 표현(시각화)個分割基準特性
plt.figure(figsize=(10, 10))
tree.plot_tree(clf, 
               feature_names=columns, 
               class_names=['Ture', 'False'],
               rounded=True,
               filled=True)
plt.show()


class_names = ['Ture', 'False']
# 샘플을 가지고 산점도 그래프 그리기("types", "moistures", "salty_taste")根埔里変色ん
plt.figure(figsize=(15, 10))
for i in range(2):
    for feature, feature_name in enumerate(columns[:3]):
        plt.subplot(2, 3, i * 3 + feature + 1)
        plt.scatter([data[feature] for data in x_input if data[0] == i], [x_target[j] for j in range(len(x_target)) if x_input[j][0] == i], 
                    c=[x_target[j] for j in range(len(x_target)) if x_input[j][0] == i], cmap='coolwarm', label='Class: {}'.format(class_names[i]))
        plt.scatter(new_data[i][feature], clf.predict([new_data[i]])[0], c='black', marker='x', s=100, label='New Data')
        plt.xlabel(feature_name)
        plt.ylabel('preferences')
        plt.title('Scatter Plot (Feature: {})'.format(feature_name))
plt.tight_layout()
plt.show()


# 샘플을 가지고 산점도 그래프 그리기("ingredients", "amount_of_cream", "sugar_content")
plt.figure(figsize=(15, 10))
for i in range(2):
    for feature, feature_name in enumerate(columns[3:]):
        plt.subplot(2, 3, i * 3 + feature + 1)
        plt.scatter([data[feature+3] for data in x_input if data[0] == i], [x_target[j] for j in range(len(x_target)) if x_input[j][0] == i], 
                    c=[x_target[j] for j in range(len(x_target)) if x_input[j][0] == i], cmap='coolwarm', label='Class: {}'.format(class_names[i]))
        plt.scatter(new_data[i][feature+3], clf.predict([new_data[i]])[0], c='black', marker='x', s=100, label='New Data')
        plt.xlabel(feature_name)
        plt.ylabel('preferences')
        plt.title('Scatter Plot (Feature: {})'.format(feature_name))
plt.tight_layout()
plt.show()