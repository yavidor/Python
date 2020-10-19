import sys

__author__ = "yavidor"


def calc(question, deli):  # Actually finding the answer
    part1 = question[0:question.find(deli) - 1]
    part2 = question[question.find(deli) + 2:]
    if question[question.find(deli) + 1] != " ":
        part2 = question[question.find(deli) + 1:]
    if (question[question.find(deli) - 1]) != " ":
        part1 = question[0:question.find(deli)]
    if deli == '/':
        try:
            ans = float(part1) / float(part2)
        except ZeroDivisionError:
            return "Division by zero is impossible"
    elif deli == '-':
        ans = float(part1) - float(part2)
    elif deli == '+':
        ans = float(part1) + float(part2)
    elif deli == '*':
        ans = float(part1) * float(part2)
    else:
        return "error"
    return f"{question}= {ans}".replace('\n', ' ').replace('\r', '')


def findType(question):  # determining the type of question
    try:
        if question.find('/') != -1:
            return calc(question, '/')
        if question.find('-') != -1 and question[question.find('-') + 1] == " ":
            return calc(question, '-')
        if question.find('+') != -1:
            return calc(question, '+')
        if question.find('*') != -1:
            return calc(question, '*')
        else:
            return "Only one operator"
    except Exception as e:
        return e


def solve():
    try:
        questions = open(sys.argv[1], 'r')
    except Exception as e:
        return e
    try:
        answers = open(sys.argv[2], 'w')
    except Exception as e:
        return e
    for question in questions:
        a = findType(question)
        answers.write(a + '\n')
    return "yesh"


def main():
    print(solve())


if __name__ == "__main__":
    main()
