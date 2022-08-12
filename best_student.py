student1 = {
    "nombre": "Pedro",
    "matematicas": 2,
    "español": 2.1,
    "ciencias": 3,
    "literatura": 3,
    "arte": 5
}

student2 = {
    "nombre": "Ana",
    "matematicas": 3,
    "español": 4,
    "ciencias": 5,
    "literatura": 2.1,
    "arte": 3.5
}


student3 = {
    "nombre": "Maria",
    "matematicas": 4,
    "español": 2.3,
    "ciencias": 1.2,
    "literatura": 3,
    "arte": 1
}

student4 = {
    "nombre": "Carlos",
    "matematicas": 1,
    "español": 2,
    "ciencias": 3,
    "literatura": 3,
    "arte": 4
}

student5 = {
    "nombre": "Diana",
    "matematicas": 3,
    "español": 4,
    "ciencias": 1,
    "literatura": 5,
    "arte": 1
}


def majorNote(subject: str, student1: dict, student2: dict, student3: dict, student4: dict, student5: dict) -> str:
    majorNote = student1[subject]
    bestStudent = student1['nombre']
    if(student2[subject] > majorNote or (student2[subject] == majorNote and student2['nombre'].lower() < bestStudent.lower())):
        majorNote = student2[subject]
        bestStudent = student2['nombre']
    if(student3[subject] > majorNote or (student3[subject] == majorNote and student3['nombre'].lower() < bestStudent.lower())):
        majorNote = student3[subject]
        bestStudent = student3['nombre']
    if(student4[subject] > majorNote or (student4[subject] == majorNote and student4['nombre'].lower() < bestStudent.lower())):
        majorNote = student4[subject]
        bestStudent = student4['nombre']
    if(student5[subject] > majorNote or (student5[subject] == majorNote and student5['nombre'].lower() < bestStudent.lower())):
        majorNote = student5[subject]
        bestStudent = student5['nombre']
    return bestStudent


def majorMathNote(student1: dict, student2: dict, student3: dict, student4: dict, student5: dict) -> str:
    return majorNote('matematicas', student1, student2, student3, student4, student5)


def majorSpanishNote(student1: dict, student2: dict, student3: dict, student4: dict, student5: dict) -> str:
    return majorNote('español', student1, student2, student3, student4, student5)


def majorScientsNote(student1: dict, student2: dict, student3: dict, student4: dict, student5: dict) -> str:
    return majorNote('ciencias', student1, student2, student3, student4, student5)


def majorLiteratureNote(student1: dict, student2: dict, student3: dict, student4: dict, student5: dict) -> str:
    return majorNote('literatura', student1, student2, student3, student4, student5)


def majorArtNote(student1: dict, student2: dict, student3: dict, student4: dict, student5: dict) -> str:
    return majorNote('arte', student1, student2, student3, student4, student5)


def get_best_student_by_course(student1: dict, student2: dict, student3: dict, student4: dict, student5: dict) -> dict:
    best_student_by_course = {
        "matematicas": majorMathNote(student1, student2, student3, student4, student5),
        "español": majorSpanishNote(student1, student2, student3, student4, student5),
        "ciencias": majorScientsNote(student1, student2, student3, student4, student5),
        "literatura": majorLiteratureNote(student1, student2, student3, student4, student5),
        "arte": majorArtNote(student1, student2, student3, student4, student5),
    }

    return best_student_by_course


print(get_best_student_by_course(student1, student2, student3, student4, student5))
