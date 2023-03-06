import security
import compute

security.askUsername()

firstYear = {
    "General Courses" : {
        "EnviSci" : 3,
        "Algebra" : 3,
    },
    "Professional Courses" : {
        "Eng 1": 3,
        "Fil 1" : 3,
        "PE 1" : 3,
    },
    "Core Courses" : {
        "CC1" : 3,
        "CC2" : 3,
    },
    "Misc Fee" : 2000,
}

secondYear = {
    "General Courses" : {
        "Cal 2" : 3,
        "Linear" : 3,
        "Physics1" : 3,
    },
    "Professional Courses" : {
        "Eng 3" : 3,
        "Fil 3" : 3,
        "PE 3" : 3,
    },
    "Core Courses" : {
        "CC4" : 3,
        "CC5" : 3,
    },
    "Misc Fee" : 2500,
}

thirdYear = {
    "General Courses" : {
        "PolSci 1" : 3,
        "Anthro 1" : 3,
        "Psych 1" : 3,
    },
    "Professional Courses" : {
        "Writing 1" : 3,
        "DataSci 1": 3,
    },
    "Core Courses" : {
        "CC6" : 3,
        "CC10" : 3,
        "Thesis 1" : 3,
    },
    "Misc Fee" : 3000,
}

fourthYear = {
    "General Courses" : {
        "Acctg 1" : 3,
        "Rizal" : 3, 
    },
    "Professional Courses" : {
        "Writing 3" : 3,
        "DataSci 3" : 3,
    },
    "Core Courses" : {
        "Elect 1" : 3,
        "Elect 2" : 3,
        "Thesis 2" : 3,
    },
    "Misc Fee" : 3500,
}

subjects = {
    "First Year" : firstYear,
    "Second Year" : secondYear,
    "Third Year" : thirdYear,
    "Fourth Year" : fourthYear,
}


# Goods
studentInfo = {}
studentInfoKeys = ["First Name","Middle Initial","Last Name","Course","Year"]
for i in studentInfoKeys:
    studentInfo.update({i:input(f"Enter {i}: ").strip().title()})

paymentScheme = input("\nEnter payment scheme(Full Payment, Installments,Partial Payment): ").title().strip()

if paymentScheme == "Full Payment":
    compute.paymentMode1(subjects,studentInfo)

elif paymentScheme == "Installments":
    compute.paymentMode2(subjects,studentInfo)

elif paymentScheme == "Partial Payment":
    compute.paymentMode3(subjects,studentInfo)