def deduplicate_lists(lst1, lst2, reverse=False):
    return sorted(set(lst1 + lst2), reverse=reverse)

