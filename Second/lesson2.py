import numpy as np
#1
# rng = np.random.default_rng(1)
# s = rng.random(50)

# print(s)
# print(sum(s))
# print(np.sum(s))

# a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print(np.sum(a))
# print(np.sum(a, axis=0))
# print(np.sum(a, axis=1))

# print(np.min(a))
# print(np.min(a, axis=0))
# print(np.min(a, axis=1))

# print(a.min())
# print(a.min(0))
# print(a.min(1))

# print(np.nanmin(a))
# print(np.nanmin(a, axis=0))
# print(np.nanmin(a, axis=1))


#2
# a = np.array([0, 1, 2])
# b = np.array([5, 5, 5])

# print(a + b)
# print(a + 5)

# a = np.array([[0, 1, 2], [3, 4, 5]])
# print(a + 5)

# a = np.array([0, 1, 2])
# b = np.array([[0], [1], [2]])
# print(a + b)

# a = np.array([[0, 1, 2], [3, 4, 5]])
# b = np.array([5])

# print(a.ndim, a.shape)
# print(b.ndim, b.shape)

# a = np.ones((2, 3))
# b = np.arange(3)

# print(a)
# print(b)

# print(a.ndim, a.shape)
# print(b.ndim, b.shape)

# c = a + b
# print(c, c.shape)

# a = np.arange(3).reshape((3, 1))
# b = np.arange(3)

# print(a)
# print(b)

# print(a.ndim, a.shape)
# print(b.ndim, b.shape)

# c = a + b

# print(c, c.shape)

# a = np.ones((3, 2))
# b = np.arange(3)

# #c = a + b ошибка измерений

# X = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
#              [9, 8, 7, 6, 5, 4, 3, 2, 1]])

# Xmean0 = X.mean(0)
# print(Xmean0)

# Xcenter0 = X - Xmean0
# print(Xcenter0)

# Xmean1 = X.mean(1)
# print(Xmean1)

# #Xcenter1 = X - Xmean1 ошибка

# Xmean1 = Xmean1[:, np.newaxis]
# Xcenter1 = X - Xmean1

# print(Xcenter1)

# x = np.linspace(0, 5, 50)
# y = np.linspace(0, 5, 50)[:, np.newaxis]
# z = np.sin(x) ** 3 + np.cos(20 + y * x) * np.sin(y)

# print(z.shape)

# import matplotlib.pyplot as plt

# plt.imshow(z)
# plt.colorbar()


#3
# x = np.array([1, 2, 3, 4, 5])

# print(x < 3)
# print(np.less(x, 3))#одинаковые

# print(np.sum(x < 3))#количество

# y = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print(np.sum(y < 4, axis=0))
# print(np.sum(y < 4, axis=1))

# x = np.array([1, 2, 3, 4, 5])
# y = x < 3

# print(x[y])#работает как маска

# x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# index = [1, 5, 7]

# print(x[index])#индекс в виде вектора

# index = [[1, 5, 7], [2, 4, 8]]
# print(x[index])

# x = np.arange(12).reshape((3, 4))

# print(x) #форма массив индексов, а не исходная
# print(x[2])
# print(x[2, [2, 0, 1]])
# print(x[1:, [2, 0, 1]])

# x = np.arange(10)
# i = np.array([2, 1, 8, 4])

# print(x)

# x[i] = 999
# print(x)

# x = [3, 2, 3, 5, 2, 6, 7, 3, 6, 3, 2]

# print(sorted(x))
# print(np.sort(x))

#4

data = np.zeros(4, dtype={
    'names': (
        'name', 'age'
    ),
    'formats': (
        'U10', 'i4'
    )
})

print(data.dtype)

name = ['name1', 'name2', 'name3', 'name4']
age = [10, 20, 30, 40]

data['name'] = name
data['age'] = age

print(data)
print(data['age'] > 20)
print(data[data['age'] > 20]['name'])

data_rec = data.view(np.recarray)

print(data_rec)
print(data_rec[0])
print(data_rec[-1].name)