# En desarrollo
def test(program: function, *args, expected: any) -> bool:
    res: bool = program(args) == expected
    return res
