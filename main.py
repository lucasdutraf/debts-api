import sys
import json
from service import SPService
from parser import SPParser

def normalize_license_plate(license_plate):
    conversion_table = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7,
        "I": 8,
        "J": 9
    }
    if license_plate[4].isalpha():
        resultant_license_plate = ""
        for index in range(0, len(license_plate)):
            if index == 4:
                resultant_license_plate += str(conversion_table[license_plate[index]])
            else:
                resultant_license_plate += license_plate[index]
        return resultant_license_plate
    return license_plate

if __name__ == "__main__":
    try:
        if len(sys.argv) == 3:    
            debt_option = None
            license_plate = sys.argv[1]
            renavam = sys.argv[2]
        elif len(sys.argv) == 4:    
            debt_option = sys.argv[1]
            license_plate = sys.argv[2]
            renavam = sys.argv[3]
        assert len(sys.argv) == 4 or len(sys.argv) == 3
    except (AssertionError, IndexError):
        print("Argumentos inválidos")
        sys.exit(1)

    service = SPService(
        license_plate=normalize_license_plate(license_plate),
        renavam=renavam,
        debt_option=debt_option
    )
    try:
        search_result = service.debt_search()
    except Exception as exc:
        print(exc)
        sys.exit(1)

    parser = SPParser(search_result)

    if debt_option == "ticket":
        result = parser.collect_ticket_debts()
    elif debt_option == "ipva":
        result = parser.collect_ipva_debts()
    elif debt_option == "dpvat":
        result = parser.collect_insurance_debts()
    elif debt_option == "licensing":
        result = parser.collect_licensing_debts()
    elif debt_option == None:
        result = parser.collect_all_debts()
    else:
        print("Opção inválida")
        sys.exit(1)

    print(
        json.dumps(result, indent=4, ensure_ascii=False)
    )
    sys.exit(0)