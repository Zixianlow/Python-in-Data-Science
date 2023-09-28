def ft_tqdm(lst: range) -> None:
    """ft_tqdm(lst which is range) --> None

Print out the progress bar based on the iterated progress"""
    total = len(lst)
    progress = 0

    for item in lst:
        yield item
        progress += 1
        percent = progress / total
        fill = int(100 * percent)
        if (fill == 100):
            bar = "=" * 99 + ">"
        else:
            bar = "=" * fill + "-" * (100 - fill)
        print(f"{fill}%|[{bar}]| {progress}/{total}", end="\r")
