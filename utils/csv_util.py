# def get_dictionary_from_csv(filename: str) -> {int: []}:
#     filepath = PATH_TO_RES + filename
#     all_dictionaries = create_blank_dictionaries()
#
#     with open(filepath, 'r', newline='') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             entry = row.pop().split(';')
#             push_entry_into_dictionary(all_dictionaries, entry)
#
#     return all_dictionaries
#
#
# def create_blank_dictionaries() -> {}:
#     dictionaries = {}
#     for i in range(WORD_LENGTH_MIN, WORD_LENGTH_MAX + 1):
#         dictionaries[i] = []
#     return dictionaries
#
#
# def push_entry_into_dictionary(dictionaries: {int: []}, entry: []):
#     dictionaries[int(entry.pop(1))].append(entry.pop(0))