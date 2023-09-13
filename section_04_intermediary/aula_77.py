# Exercício - sistema de perguntas e respostas
perguntas = [
    {
        "Pergunta": "Quanto é 2+2?",
        "Opções": ["1", "3", "4", "5"],
        "Resposta": "4",
    },
    {
        "Pergunta": "Quanto é 5*5?",
        "Opções": ["25", "55", "10", "51"],
        "Resposta": "25",
    },
    {
        "Pergunta": "Quanto é 10/2?",
        "Opções": ["4", "5", "2", "1"],
        "Resposta": "5",
    },
]

running = True
number_of_questions = len(perguntas)
current_question = 0
acertos = 0
erros = 0


def display_question():
    global acertos, erros, current_question
    print(f'\n{perguntas[current_question]["Pergunta"]}')
    for i, option in enumerate(perguntas[current_question]["Opções"]):
        print(f"{i}: {option}")
    choice = int(input("Escolha sua opção: "))
    if (
        perguntas[current_question]["Resposta"]
        == perguntas[current_question]["Opções"][choice]
    ):
        acertos += 1
        print("\n\tParabéns, você acertou!")
    else:
        erros += 1
        print("\n\tVocê errou...")

    current_question += 1


while running:
    while current_question < number_of_questions:
        display_question()

    print(f"\nVocê acertou {acertos} questões e errou {erros}...")

    running = False
