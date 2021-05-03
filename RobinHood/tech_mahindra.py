def loanEligibilityCal(empType: str, age: int, sal: int, loanTerm: int):
    if empType.lower() == "salaried" or empType.lower() == "self-employed":
        if 21 <= age <= 58 and loanTerm + age <= 58 and sal >= 10000 and 1<=loanTerm<=30:
            print("Eligible")
        else:
            print("Not Eligible")
    else:
        print("Not Eligible")


loanEligibilityCal("self-employed", 43, 25000, 10)