from src.domain.coder import Coder
from src.domain.recruiter import Recruiter
from src.main import (
    create_list_of_matches,
    create_list_of_combinations,
    filter_by_location,
    filter_by_skill,
    filter_by_languages,
)


# def setup():

#     ainara = Coder("ainara", ["Bilbao", "Barcelona"], ["python", "vue"])
#     ainhoa = Coder("ainhoa", ["Bilbao"], ["python", "vue"], ["ingles"])
#     jeff = Coder("jeff", ["Bilbao"], ["python", "vue"], ["frances"])

#     perla = Recruiter("perla", ["Bilbao"], ["python", "angular"], ["ingles"])
#     laura = Recruiter("laura", ["Barcelona"], ["python", "vue"])
#     joseph = Recruiter("joseph", ["Bilbao"], ["php", "angular"])

#     coder_list = [ainara, ainhoa, jeff]
#     recruiter_list = [perla, laura, joseph]

#     number_of_meetings = 5
#     return create_list_of_matches(coder_list, recruiter_list, number_of_meetings)


def test_main_should_create_a_list_of_matches():
    ainara = Coder("ainara")
    perla = Recruiter("perla")
    laura = Recruiter("laura")
    coder_list = [ainara]
    recruiter_list = [perla, laura]
    number_of_meetings = 2

    list_of_matches = create_list_of_matches(
        coder_list, recruiter_list, number_of_meetings
    )
    assert len(list_of_matches) == 8

def test_main_should_create_a_list_of_posible_combinations():
    ainara = Coder("ainara")
    perla = Recruiter("perla")
    laura = Recruiter("laura")
    coder_list = [ainara]
    recruiter_list = [perla, laura]
    number_of_meetings = 2

    list_of_matches = create_list_of_matches(
        coder_list, recruiter_list, number_of_meetings
    )
    slots = len (recruiter_list) * number_of_meetings

    list_of_combinations = create_list_of_combinations (list_of_matches, slots)
    number_of_combinations = 0
    for combination in list_of_combinations:
        number_of_combinations +=1

    assert len(list_of_matches) == 8
    assert number_of_combinations ==  70





# def test_main_should_return_list_of_matches_with_same_locations():

#     list_of_matches = setup()

#     list_filtered_by_location = filter_by_location(list_of_matches)

#     assert len(list_filtered_by_location) == 35


# def test_main_should_return_list_of_matches_with_a_matching_skill():

#     list_of_matches = setup()

#     list_filtered_by_skill = filter_by_skill(list_of_matches)

#     assert len(list_filtered_by_skill) == 30


# def test_main_should_return_list_of_matches_with_same_languages():

#     list_of_matches = setup()

#     list_filtered_by_languages = filter_by_languages(list_of_matches)

#     assert len(list_filtered_by_languages) == 5
