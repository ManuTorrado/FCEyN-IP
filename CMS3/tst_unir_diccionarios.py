from typing import List
from typing import Dict
import json


def unir_diccionarios(a_unir: List[Dict[str, str]]) -> Dict[str, List[str]]:
    res: Dict[str, List[str]] = {}

    for diccionario in a_unir:
        for key in diccionario:
            if (key in res):
                res[key].append(diccionario[key])
            else:
                res[key] = [diccionario[key]]

    return res


print(unir_diccionarios([{"a": 2}, {"b": 3, "a": 1}]))
print(unir_diccionarios([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'a': 5}]))
