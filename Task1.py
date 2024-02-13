import timeit
import random

def merge_sort(arr):
    # Рекурсивна функція сортування злиттям
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)  # Сортування лівої половини
        merge_sort(R)  # Сортування правої половини

        # Злиття відсортованих підмасивів
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def insertion_sort(arr):
    # Функція сортування вставками
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def tim_sort(arr):
    # Вбудована функція сортування Timsort
    arr.sort()

# Розміри масивів для тестування
sizes = [100, 1000, 10000, 100000]
# Назви алгоритмів сортування
algorithms = ['merge_sort', 'insertion_sort', 'tim_sort']

for size in sizes:
    # Генеруємо випадковий масив заданого розміру
    arr = [random.randint(0, 1000) for _ in range(size)]
    print(f"Розмір масиву: {size}")

    for algorithm in algorithms:
        # Вимірюємо час виконання кожного алгоритму
        setup_code = f"from __main__ import {algorithm}"
        stmt = f"{algorithm}({arr.copy()})"
        time_taken = timeit.timeit(stmt, setup=setup_code, number=1)
        print(f"{algorithm}: {time_taken} секунд")
