from gb2260 import gb2260

loc2code = {}
for code, loc in gb2260.items():
    loc2code[loc] = code


def validation_code(id17):
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    validate = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    check_sum = 0
    for i in range(0, len(id17)):
        check_sum += int(id17[i]) * weight[i]
    return validate[check_sum % 11]


def generate(location: str, birthday: str, male: bool = None) -> list:
    loc_code = loc2code.get(location)
    if not loc_code:
        raise Exception("location not found")
    id14 = loc_code + birthday
    if len(id14) != 14:
        raise Exception("invalid birthday")
    result = []
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if male is not None:
                    if (k % 2 == 1) == male:
                        id17 = f"{id14}{i}{j}{k}"
                        sfz = id17 + validation_code(id17)
                        result.append(sfz)
    return result


if __name__ == "__main__":
    ids = generate(location="潼南县", birthday="19950916", male=True)
    print(ids)
