import pandas as pd
import math

def entropy(data):
    """Calcula la entropía de un conjunto de datos"""
    count = {}
    for item in data:
        if item not in count:
            count[item] = 0
        count[item] += 1
    entropy = 0
    for c in count.values():
        p = c / len(data)
        entropy -= p * math.log2(p)
    return entropy

def information_gain(data, attribute):
    """Calcula la ganancia de información de un atributo"""
    values = set(data[attribute])
    entropy_sum = 0
    for value in values:
        subset = data[data[attribute] == value]
        p = len(subset) / len(data)
        entropy_sum += p * entropy(subset["Class"])
    return entropy(data["Class"]) - entropy_sum

def id3(data, target_attribute):
    """Implementación del algoritmo ID3"""
    # Si todos los ejemplos son de la misma clase, devolver el nodo hoja correspondiente
    if len(set(data[target_attribute])) == 1:
        return data[target_attribute].iloc[0]
    # Si no hay más atributos para dividir, devolver la clase mayoritaria
    if len(data.columns) == 1:
        return data[target_attribute].value_counts().idxmax()
    # Seleccionar el atributo con la mayor ganancia de información
    information_gains = [(attribute, information_gain(data, attribute)) for attribute in data.columns if attribute != target_attribute]
    best_attribute, _ = max(information_gains, key=lambda x: x[1])
    # Crear el nodo con el atributo seleccionado
    node = {best_attribute: {}}
    # Dividir los ejemplos en subconjuntos según el valor del atributo seleccionado
    for value in set(data[best_attribute]):
        subset = data[data[best_attribute] == value].drop(best_attribute, axis=1)
        # Si no hay ejemplos en el subconjunto, devolver la clase mayoritaria del conjunto original
        if len(subset) == 0:
            node[best_attribute][value] = data[target_attribute].value_counts().idxmax()
        # De lo contrario, agregar el subárbol correspondiente al nodo actual
        else:
            node[best_attribute][value] = id3(subset, target_attribute)
    return node

data = pd.read_csv("datos.csv")
tree = id3(data, "Class")
print(tree)