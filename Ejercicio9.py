from collections import Counter
from pattern.es import tag
from pattern.es import conjugate, INFINITIVE


def cuentapVerbos(str):
    verbos = []
    for word, pos in tag(str):  # tag devuelve una lista de tuplas formadas por (palabra, tipo de palabra)
        if pos == "VB":
            verbos.append(conjugate(word, tense=INFINITIVE))

    string = (' ').join(verbos)
    count = Counter(string.split(' ')).most_common()
    for key in range(3):
        print(count[key][0], count[key][1])


frase = "Este es un párrafo de prueva. El verbo ser, será el mas utilizado. El otro será crear, por eso se creó la oración \n" \
        " de esta manera. Por último, se creará esta oración que posee el tercer verbo: poseer. Nada más que decir."

cuentapVerbos(frase)
