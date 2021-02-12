import pytest
import json
from service import SPService
from parser import SPParser
from api import API

@pytest.mark.parametrize("license_plate, renavam, debt_option, output_file", [('ABC1234', '11111111111', 'dpvat', './tests/dpvat.json'), ('ABC1234', '11111111111', 'ipva', './tests/ipva.json'), ('ABC1234', '11111111111', 'licensing', './tests/licensing.json'),('ABC1234', '11111111111', 'ticket', './tests/ticket.json'), (('ABC1234', '11111111111', None, './tests/all_debt.json'))])
def test_main_flow(license_plate, renavam, debt_option, output_file):
    with open(output_file, 'r') as f:
        output_ = json.load(f)

    service = SPService(
        license_plate=license_plate,
        renavam=renavam,
        debt_option=debt_option
    )
    search_result = service.debt_search()
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
    assert result == output_


# @pytest.mark.parametrize("input_file", [('./src/utils/read_file_es.json'), ('./test_utils/read_file_en.json')])
# def test_read_input_file_not_found(input_file):
#     with pytest.raises(ArquivoNaoEncontradoException):
#         parser = Parser()

#         assert parser.read_input_file(input_file)
