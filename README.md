# dataviztoolkit

A simple data visualization toolkit for beginners.

## Installation
```bash
pip install dataviztoolkit
```

## Usage
```python
from dataviztoolkit import DataVisualizer

dv = DataVisualizer("data.csv")

dv.summary()
dv.histogram("Age")
dv.scatter("Age", "Fare")
dv.bar_chart("Embarked")
dv.heatmap()
```

## Features

* **`summary()`** — Quick dataset overview
* **`histogram(column)`** — Distribution of a numeric column
* **`scatter(x, y)`** — Relationship between two numeric columns
* **`bar_chart(column)`** — Value counts for a categorical column
* **`heatmap()`** — Correlation heatmap for all numeric columns
