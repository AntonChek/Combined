import pandas as pd

classifier = pd.read_csv('Классификатор.csv', delimiter=";")
category = pd.read_csv('Список категорий.csv', delimiter=";")
main_list = pd.read_csv('Основной лист.csv', delimiter=";")

category = category.set_index('id')
classifier = classifier.set_index('id')
main_list = main_list.set_index('category')

combined = pd.merge(main_list, category, left_on='category', right_on='id').set_index('class')
combined = pd.merge(combined, classifier, left_on='class', right_on='id').rename(columns={'name_x': 'category', 'name_y': 'class'})

result = combined.reindex(columns=['id', 'category', 'class', 'value']).set_index('id')

result.to_csv("combined.csv")
print(result)