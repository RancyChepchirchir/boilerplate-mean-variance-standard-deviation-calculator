import numpy as np

def calculate(listed):
    if len(listed) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        arr = np.array(listed).reshape(3, 3)

        output = {
            'mean': [],
            'variance': [],
            'standard deviation': [],
            'max': [],
            'min': [],
            'sum': []
        }

        output['mean'].append(list(arr.mean(axis=0)))
        output['mean'].append(list(arr.mean(axis=1)))
        output['mean'].append(arr.flatten().mean())

        output['variance'].append(list(arr.var(axis=0)))
        output['variance'].append(list(arr.var(axis=1)))
        output['variance'].append(arr.flatten().var())

        output['standard deviation'].append(list(arr.std(axis=0)))
        output['standard deviation'].append(list(arr.std(axis=1)))
        output['standard deviation'].append(arr.flatten().std())

        output['max'].append(list(arr.max(axis=0)))
        output['max'].append(list(arr.max(axis=1)))
        output['max'].append(arr.flatten().max())

        output['min'].append(list(arr.min(axis=0)))
        output['min'].append(list(arr.min(axis=1)))
        output['min'].append(arr.flatten().min())

        output['sum'].append(list(arr.sum(axis=0)))
        output['sum'].append(list(arr.sum(axis=1)))
        output['sum'].append(arr.flatten().sum())

        return output
