def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate BMI for each person height and weight.

    params:
        height: list of heights in centimeters.
        weight: list of weights in kilograms.

    return:
        list of BMIs for each person.
    """
    try:
        if not type(height) is list or not type(weight) is list:
            raise ValueError("Both height and weight must be lists.")
        if len(height) != len(weight):
            raise ValueError("Both lists must have the same length.")

        for h, w in zip(height, weight):
            if not type(h) in (int, float) or not type(w) in (int, float):
                raise ValueError("Values must be only ints or floats.")
            if h <= 0 or w <= 0:
                raise ValueError("Values must be positive.")

        bmi = []
        for h, w in zip(height, weight):
            b = w / (h ** 2)
            bmi.append(b)

        return bmi
    except Exception as e:
        print("Error:", e)
        return None


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Calculate if each BMI is above the limit.

    params:
        bmi: list of BMIs.
        limit: the BMI limit to compare against.

    return:
        list of booleans.
    """
    try:
        if not type(bmi) is list:
            raise ValueError("BMI must be a list.")
        if not type(limit) in (int, float):
            raise ValueError("Limit must be an int or float.")

        for b in bmi:
            if not type(b) in (int, float):
                raise ValueError("BMI values must be only ints or floats.")
            if b <= 0:
                raise ValueError("BMI values must be positive.")

        result = []
        for b in bmi:
            result.append(b > limit)

        return result
    except Exception as e:
        print("Error:", e)
        return None
