def my_sort(data, key):
    def custom_sort(x):
        return x[key]
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if custom_sort(data[j]) > custom_sort(data[j+1]):
                data[j], data[j+1] = data[j+1], data[j]
    return data
