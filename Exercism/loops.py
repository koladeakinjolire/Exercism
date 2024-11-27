"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    rounded_scores = []
    for score in student_scores:
        rounded_scores.append(round(score))
    return rounded_scores

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    i = 0
    for score in student_scores:
        if score <= 40:
            i += 1
    
    return i


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    best_scores = []
    for score in student_scores:
        if score >= threshold:
            best_scores.append(score)

    return best_scores
    


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    thresholds = []

    if type(highest) == int:
        interval = round((highest - 41) / 4)
        x = range(41, (highest-interval)+3, interval)
        thresholds = [i for i in x]

    if type(highest) == list:
        for score in highest:
            interval = round((score - 41) / 4)
            x = range(41, (score-interval)+3, interval)
            thresholds.append(list(x))

    return thresholds

print(letter_grades([100,97,91,82]))
print(letter_grades(98))


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    ranked_students = []
    for rank, (score, name) in enumerate(zip(student_scores, student_names), 1):
        ranked_students.append(f"{rank}. {name}: {score}")

    return ranked_students

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for student in student_info:
        if student[1] == 100:
          return student
  
    return []

test_data = [
             [['Joci', 100], ['Vlad', 100], ['Raiana', 100], ['Alessandro', 100]],
             [['Jill', 30], ['Paul', 73]],
             [],
             [['Rui', 60], ['Joci', 58], ['Sara', 91], ['Kora', 93], ['Alex', 42],
              ['Jan', 81], ['Lilliana', 40], ['John', 60], ['Bern', 28], ['Vlad', 55]],
             [['Yoshi', 52], ['Jan', 86], ['Raiana', 100], ['Betty', 60],
              ['Joci', 100], ['Kora', 81], ['Bern', 41], ['Rose', 94]]
             ]
