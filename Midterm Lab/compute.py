def paymentMode1(subjects,studentInfo):
    generalCourseUnits = subjects[studentInfo["Year"]].get("General Courses")
    professionalCourseUnits = subjects[studentInfo["Year"]].get("Professional Courses")
    coreCourseUnits = subjects[studentInfo["Year"]].get("Core Courses")

    unitsPrice = 0
    for i in generalCourseUnits.values():
        unitPrice = i * 1000
        unitsPrice += unitPrice

    for i in professionalCourseUnits.values():
        unitPrice = i * 1000
        unitsPrice += unitPrice

    for i in coreCourseUnits.values():
        unitPrice = i * 1000
        unitsPrice += unitPrice

    tuition = (unitsPrice - (0.05 * unitsPrice) + subjects[studentInfo["Year"]].get("Misc Fee"))

    print("\n\nGeneral Subjects {}\nProfessional Subjects {}\nCore Courses {}".format(generalCourseUnits,professionalCourseUnits,coreCourseUnits))
    print("{}, {} {} - {} {} - Tuition: {}".format(studentInfo["Last Name"], studentInfo["First Name"], studentInfo["Middle Initial"], studentInfo["Year"],studentInfo["Course"],tuition))

    exit()


def paymentMode2(subjects,studentInfo):
    generalCourseUnits = subjects[studentInfo["Year"]].get("General Courses")
    professionalCourseUnits = subjects[studentInfo["Year"]].get("Professional Courses")
    coreCourseUnits = subjects[studentInfo["Year"]].get("Core Courses")

    unitsPrice = 0
    for i in generalCourseUnits.values():
        unitPrice = i * 1000
        unitsPrice += unitPrice

    for i in professionalCourseUnits.values():
        unitPrice = i * 1000
        unitsPrice += unitPrice

    for i in coreCourseUnits.values():
        unitPrice = i * 1000
        unitsPrice += unitPrice

    tuition = (unitsPrice - (0.03 * unitsPrice) + subjects[studentInfo["Year"]].get("Misc Fee"))

    print("\n\nGeneral Subjects {}\nProfessional Subjects {}\nCore Courses {}".format(generalCourseUnits,professionalCourseUnits,coreCourseUnits))
    print("{}, {} {} - {} {} - Tuition: {}".format(studentInfo["Last Name"], studentInfo["First Name"], studentInfo["Middle Initial"], studentInfo["Year"],studentInfo["Course"],tuition))

    exit()


def paymentMode3(subjects,studentInfo):
    generalCourseUnits = subjects[studentInfo["Year"]].get("General Courses")
    professionalCourseUnits = subjects[studentInfo["Year"]].get("Professional Courses")
    coreCourseUnits = subjects[studentInfo["Year"]].get("Core Courses")

    unitsPrice = 0
    for i in generalCourseUnits.values():
        unitPrice = i * 1000
        unitsPrice += unitPrice

    for i in professionalCourseUnits.values():
        unitPrice = i * 1000
        unitsPrice += unitPrice

    for i in coreCourseUnits.values():
        unitPrice = i * 1000
        unitsPrice += unitPrice

    tuition = (unitsPrice + subjects[studentInfo["Year"]].get("Misc Fee"))

    print("\n\nGeneral Subjects {}\nProfessional Subjects {}\nCore Courses {}".format(generalCourseUnits,professionalCourseUnits,coreCourseUnits))
    print("{}, {} {} - {} {} - Tuition: {}".format(studentInfo["Last Name"], studentInfo["First Name"], studentInfo["Middle Initial"], studentInfo["Year"],studentInfo["Course"],tuition))

    exit()