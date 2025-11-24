import pandas as pd

data = {
    "color": ["red", "blue", "green"],
    "size": ["small", "medium", "large"],
    "price": [100, 200, 300],
    "weight": [1, 2, 3],
    "shape": ["circle", "square", "triangle"],
    "material": ["wood", "metal", "plastic"],
    "style": ["modern", "classic", "art deco"],
    "condition": ["new", "used", "vintage"],
}

df = pd.DataFrame(data)
one_hot_encoded_df = pd.get_dummies(
    df,
    columns=["color", "size", "material", "style", "condition"],
    dtype=int,
)
print(one_hot_encoded_df)