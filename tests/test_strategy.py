
from src.design_patterns.strategy import BubbleSortStrategy, QuickSortStrategy, Context
import random

def test_sort_strategy():
    rand_list = [random.randint(0, 100) for _ in range(10)]

    context = Context(BubbleSortStrategy())
    assert context.execute([3, 2, 1]) == [1, 2, 3]
    assert context.execute(rand_list) == sorted(rand_list)

    context.set_strategy(QuickSortStrategy())

    assert context.execute([3, 2, 1]) == [1, 2, 3]
    assert context.execute(rand_list) == sorted(rand_list)