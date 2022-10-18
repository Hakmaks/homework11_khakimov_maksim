import json


def load_candidates_from_json():
    """
    Возвращает список всех кандидатов
    """
    with open("candidates.json", "r", encoding="utf-8") as file:
        candidates = json.load(file)
        return candidates


def get_candidates_all():
    pass


def get_candidate(pk):
    """
    Возвращает одного кандидата по его id
    """
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate['pk'] == pk:
            return candidate


def get_candidates_by_name(name):
    """
    Возвращает кандидатов по имени
    """
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate['name'] == name:
            return candidate


def get_candidates_by_skill(skill):
    """
    Возвращает кандидатов по навыку
    """
    result = []
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result


# # candidate_pk = 1
# # candidate_name = 'Burt Stein'
# skill_name = 'python'
# # print(get_candidate(candidate_pk))
# # print(get_candidates_by_name(candidate_name))
# print(get_candidates_by_skill(skill_name))
