# ------------------------------------------------
# 1 / (1 - x)
# ------------------------------------------------

def generate_one_over_one_minus_x_order(n: int) -> str:
    res = "1"
    for k in range(1, n):
        res += f"+x^{k}"
    res += f"+o(x^{n})"
    return res


def generate_one_over_one_minus_x() -> str:
    return "1+x+x^2+x^3+\\dots+o(x^n)"


# ------------------------------------------------
# 1 / (1 + x)
# ------------------------------------------------

def generate_one_over_one_plus_x_order(n: int) -> str:
    res = "1"
    for k in range(1, n):
        if k % 2 == 1:
            res += f"-x^{k}"
        else:
            res += f"+x^{k}"
    res += f"+o(x^{n})"
    return res


def generate_one_over_one_plus_x() -> str:
    return "1-x+x^2-x^3+\\dots+o(x^n)"


# ------------------------------------------------
# exp(x)
# ------------------------------------------------

def generate_exp_order(n: int) -> str:
    res = "1+x"
    for k in range(2, n):
        res += f"+\\frac{{x^{k}}}{{{k}!}}"
    res += f"+o(x^{n})"
    return res


def generate_exp() -> str:
    return "1+x+\\frac{x^2}{2!}+\\frac{x^3}{3!}+\\dots+o(x^n)"


# ------------------------------------------------
# sin(x)
# ------------------------------------------------

def generate_sin_order(n: int) -> str:
    res = "x"
    sign = -1
    for k in range(3, n, 2):
        if sign == -1:
            res += f"-\\frac{{x^{k}}}{{{k}!}}"
        else:
            res += f"+\\frac{{x^{k}}}{{{k}!}}"
        sign *= -1
    res += f"+o(x^{n})"
    return res


def generate_sin() -> str:
    return "x-\\frac{x^3}{3!}+\\frac{x^5}{5!}-\\dots+o(x^n)"


# ------------------------------------------------
# cos(x)
# ------------------------------------------------

def generate_cos_order(n: int) -> str:
    res = "1"
    sign = -1
    for k in range(2, n, 2):
        if sign == -1:
            res += f"-\\frac{{x^{k}}}{{{k}!}}"
        else:
            res += f"+\\frac{{x^{k}}}{{{k}!}}"
        sign *= -1
    res += f"+o(x^{n})"
    return res


def generate_cos() -> str:
    return "1-\\frac{x^2}{2!}+\\frac{x^4}{4!}-\\dots+o(x^n)"


# ------------------------------------------------
# ln(1+x)
# ------------------------------------------------

def generate_ln_one_plus_x_order(n: int) -> str:
    res = "x"
    sign = -1
    for k in range(2, n):
        if sign == -1:
            res += f"-\\frac{{x^{k}}}{{{k}}}"
        else:
            res += f"+\\frac{{x^{k}}}{{{k}}}"
        sign *= -1
    res += f"+o(x^{n})"
    return res


def generate_ln_one_plus_x() -> str:
    return "x-\\frac{x^2}{2}+\\frac{x^3}{3}-\\dots+o(x^n)"


# ------------------------------------------------
# arctan(x)
# ------------------------------------------------

def generate_arctan_order(n: int) -> str:
    res = "x"
    sign = -1
    for k in range(3, n, 2):
        if sign == -1:
            res += f"-\\frac{{x^{k}}}{{{k}}}"
        else:
            res += f"+\\frac{{x^{k}}}{{{k}}}"
        sign *= -1
    res += f"+o(x^{n})"
    return res


def generate_arctan() -> str:
    return "x-\\frac{x^3}{3}+\\frac{x^5}{5}-\\dots+o(x^n)"


# ------------------------------------------------
# (1 + x)^alpha
# ------------------------------------------------

def generate_one_plus_x_alpha() -> str:
    return (
        "1+\\alpha x"
        "+\\frac{\\alpha(\\alpha-1)}{2!}x^2"
        "+\\frac{\\alpha(\\alpha-1)(\\alpha-2)}{3!}x^3"
        "+\\dots+o(x^n)"
    )


# =================================================
# TABLE DES FORMULES
# =================================================

FORMULAS = [
    {
        "name": "\\frac{1}{1-x}",
        "formula": generate_one_over_one_minus_x(),
        "formula_order": generate_one_over_one_minus_x_order
    },
    {
        "name": "\\frac{1}{1+x}",
        "formula": generate_one_over_one_plus_x(),
        "formula_order": generate_one_over_one_plus_x_order
    },
    {
        "name": "e^x",
        "formula": generate_exp(),
        "formula_order": generate_exp_order
    },
    {
        "name": "\\sin(x)",
        "formula": generate_sin(),
        "formula_order": generate_sin_order
    },
    {
        "name": "\\cos(x)",
        "formula": generate_cos(),
        "formula_order": generate_cos_order
    },
    {
        "name": "\\ln(1+x)",
        "formula": generate_ln_one_plus_x(),
        "formula_order": generate_ln_one_plus_x_order
    },
    {
        "name": "\\arctan(x)",
        "formula": generate_arctan(),
        "formula_order": generate_arctan_order
    },
    {
        "name": "(1+x)^\\alpha",
        "formula": generate_one_plus_x_alpha(),
        "formula_order": None
    }
]