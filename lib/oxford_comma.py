def oxford_comma(items):
    if len(items) > 2:
        items[-1] = 'and ' + items[-1]
        x = ', '.join(items)
        return x
    elif len(items) == 2:
        items[-1] = 'and ' + items[-1]
        x = ' '.join(items)
        return x
    else:
        return ' '.join(items)

oxford_comma(["a", "b", "c"])