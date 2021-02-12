import json
from service import SPService
from parser import SPParser

# Sinta-se livre para deletar o teste abaixo, caso queira.
def test_search_ticket():
    service = SPService(
        license_plate="license_plate",
        renavam="renavam",
        debt_option="ticket"
    )
    result = service.debt_search()
    assert result == True

@pytest.mark.parametrize("license_plate, renavam, debt_option, output_file", [('ABC1234', '11111111111', 'dpvat', './tests/dpvat.out'), ('ABC1234', '11111111111', 'ipva', './tests/ipva.out'), ('ABC1234', '11111111111', 'licensing', './tests/licensing.out'),('ABC1234', '11111111111', 'ticket', './tests/ticket.out'), (('ABC1234', '11111111111', None, './tests/all_debt.out'))])
def test_main_flow(license_plate, renavam, debt_option, output_file):
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
    assert result == output_file


# @pytest.mark.parametrize("input_file", [('./src/utils/read_file_es.out'), ('./test_utils/read_file_en.out')])
# def test_read_input_file_not_found(input_file):
#     with pytest.raises(ArquivoNaoEncontradoException):
#         parser = Parser()

#         assert parser.read_input_file(input_file)
