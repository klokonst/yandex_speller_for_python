import requests


def speller(text: str) -> str:
    frase_for_speller = text.replace(' ', '+')
    url = f'https://speller.yandex.net/services/spellservice.json/checkText?text={frase_for_speller}'
    request = requests.get(
        url=url
    )
    data = request.json()
    if len(data) == 0:
        return text
    word_list = []
    for word in data:
        word_list.append(word.get('s')[0])

    final_frase = ' '.join(word_list)
    return final_frase
