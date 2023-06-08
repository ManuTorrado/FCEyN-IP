# En desarrollo
def test(program: function, args: list[any], expected: any) -> bool:
    res: bool = program(args) == expected
    return res
