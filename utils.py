import json


def load_candidates_from_json():
    """
    Возвращает список всех кандидатов
    """
    with open("candidates.json", "r", encoding="utf-8") as file:
        return json.load(file)


def get_candidates_all():
    return load_candidates_from_json()


def get_candidate_by_pk(pk):
    """
    Возвращает одного кандидата по его id
    """
    for candidate in load_candidates_from_json():
        if candidate['pk'] == pk:
            return candidate
    return None


def get_candidates_by_name(name):
    """
    Возвращает кандидатов по имени
    """
    result = []
    for candidate in load_candidates_from_json():
        if name in candidate['name']:
            result.append(candidate)
    return result


def get_candidates_by_skill(skill):
    """
    Возвращает кандидатов по навыку
    """
    result = []
    for candidate in load_candidates_from_json():
        if skill in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result


# # candidate_pk = 1
# # candidate_name = 'Burt Stein'
# skill_name = 'python'
# # print(get_candidate(candidate_pk))
# # print(get_candidates_by_name(candidate_name))
# print(get_candidates_by_skill(skill_name))
