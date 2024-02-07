from typing import Callable
from enum import Enum
import click


def get_less_than_twenty(val: int) -> str:
    """
    Function processing the values less than 20
    """
    less_than_sixteen_mapping = {
        0: "zéro",
        1: "un",
        2: "deux",
        3: "trois",
        4: "quatre",
        5: "cinq",
        6: "six",
        7: "sept",
        8: "huit",
        9: "neuf",
        10: "dix",
        11: "onze",
        12: "douze",
        13: "treize",
        14: "quatorze",
        15: "quinze",
        16: "seize",
    }

    if val < 17:
        return less_than_sixteen_mapping[val]
    units = val % 10
    return less_than_sixteen_mapping[10] + "-" + less_than_sixteen_mapping[units]


def get_tens(val: int, from_france: bool, add_plural: bool = True) -> str:
    """
    Function processing the value less than 100
    """
    if val >= 100 | val < 0:
        return None

    if val <= 16:
        return get_less_than_twenty(val)

    tens = val // 10
    units = val % 10

    tens_mapping = {
        1: "dix",
        2: "vingt",
        3: "trente",
        4: "quarante",
        5: "cinquante",
        6: "soixante",
        7: "septante",
        8: "huitante",
        9: "nonante",
    }

    # Treating the exceptions
    if from_france:
        if val == 71:
            return "soixante-et-onze"
        if val == 81:
            return "quatre-vingt-un"

    if units == 0:
        if (not from_france) | (from_france & (tens in [1, 2, 3, 4, 5, 6])):
            return tens_mapping[tens]
        if tens == 7:
            return tens_mapping[6] + "-" + get_less_than_twenty(10)
        if tens == 8:
            return "quatre-vingts"
        return "quatre-vingt-" + get_less_than_twenty(10)

    if units == 1 and (
        (not from_france) | (from_france & (tens in [1, 2, 3, 4, 5, 6]))
    ):
        return tens_mapping[tens] + "-et-un"
    if units > 1 and ((not from_france) | (from_france & (tens in [1, 2, 3, 4, 5, 6]))):
        return tens_mapping[tens] + "-" + get_less_than_twenty(units)
    if tens == 7:
        return tens_mapping[6] + "-" + get_less_than_twenty(10 + units)
    if tens == 8:
        return "quatre-vingt-" + get_less_than_twenty(units)
    return "quatre-vingt-" + get_less_than_twenty(10 + units)


class UnitType(Enum):
    """
    Define a type for units
    """

    CENT = "cent"
    MILLE = "mille"


def get_senior_units(
    val: int,
    unit: UnitType,
    low_unit_fnc: Callable[[int, bool, bool], str],
    from_france: bool = True,
    add_plural: bool = True,
):
    """
    Generalized function to treat hundreds and thousands
    """
    if unit == "cent":
        divider = 100
    else:
        divider = 1000
    units = val // divider
    if units == 0:
        return low_unit_fnc(val, from_france)
    low_units = val % divider
    if units == 1:
        if low_units == 0:
            return unit
        return unit + "-" + low_unit_fnc(low_units, from_france)
    if low_units == 0:
        return (
            low_unit_fnc(units, from_france, add_plural=False)
            + f'-{unit}{"s" if add_plural else ""}'
        )
    return (
        low_unit_fnc(units, from_france, add_plural=False)
        + f"-{unit}-"
        + low_unit_fnc(low_units, from_france)
    )


def get_hundreds(val: int, from_france: bool = True, add_plural: bool = True) -> str:
    """
    Function treating hundreds
    """
    return get_senior_units(val, "cent", get_tens, from_france, add_plural)


def get_thousand(val: int, from_france: bool = True, add_plural: bool = True) -> str:
    """
    Function treating thousands
    """
    return get_senior_units(val, "mille", get_hundreds, from_france, add_plural)


@click.command()
@click.option("--from_france", is_flag=True, help="Enable from France mode")
def main(from_france):
    """
    The main function of the program that prints the string values for French numbers
    """
    input = [
        -10,
        0,
        1,
        5,
        10,
        11,
        15,
        20,
        21,
        30,
        35,
        50,
        51,
        68,
        70,
        75,
        99,
        100,
        101,
        105,
        111,
        123,
        168,
        171,
        175,
        199,
        200,
        201,
        555,
        999,
        1000,
        1001,
        1111,
        1199,
        1234,
        1999,
        2000,
        2001,
        2020,
        2021,
        2345,
        9999,
        10000,
        11111,
        12345,
        123456,
        654321,
        999999,
        9999990,
    ]
    for val in input:
        if val > 999999:
            click.echo(f"{val} -> The value must be less than 999999")
            continue
        if val < 0:
            click.echo(f"{val} -> The value must be positive")
            continue
        click.echo(f"{val} -> {get_thousand(val, from_france=from_france)}")


if __name__ == "__main__":
    main()
