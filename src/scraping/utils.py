dict = {
    u'а': u'а',
    u'б': u'b',
    u'в': u'v',
    u'г': u'g',
    u'д': u'd',
    u'е': u'e',
    u'ё': u'o',
    u'ж': u'h',
    u'з': u'z',
    u'и': u'e',
    u'й': u'y',
    u'к': u'k',
    u'л': u'l',
    u'м': u'm',
    u'н': u'n',
    u'о': u'o',
    u'п': u'p',
    u'р': u'r',
    u'с': u's',
    u'т': u't',
    u'у': u'u',
    u'ф': u'f',
    u'х': u'h',
    u'ц': u'ts',
    u'ч': u'ch',
    u'ш': u'sh',
    u'щ': u'sh',
    u'ъ': u'0',
    u'ы': u'i',
    u'ь': u'0',
    u'э': u'e',
    u'ю': u'yu',
    u'я': u'ya'
}

def from_ru_to_en(text:str):
    text = text.replace(' ', '_').lower()
    tmp = ''
    for key in text:
        tmp += dict.get(key,key)
    return tmp