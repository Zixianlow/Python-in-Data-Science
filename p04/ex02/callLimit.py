def callLimit(limit: int):
    """callLimit function with a function return"""
    count = 0

    def callLimiter(function):
        """callLimiter function called when def func()"""
        def limit_function(*args, **kwds):
            """limit_function prints out the func() content when less
            than limit count"""
            nonlocal count
            count += 1
            if count <= limit:
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter
