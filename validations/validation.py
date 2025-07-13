from functools import wraps


def validation(algo_name, expected, comparator=lambda x, y: x == y):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs) -> None:
            observed = func(*args, **kwargs)
            if comparator(expected, observed):
                print(f"✅ Validation Passed on {algo_name}")
            else:
                print(f"❌ Validation Failed on {algo_name}")
                print(f"Expected: {expected}")
                print(f"Observed: {observed}")

        return wrapper

    return decorator
