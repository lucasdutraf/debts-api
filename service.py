from api import API
from collections import defaultdict

class SPService:
    """
    Conecta com o webservice do Detran-SP.
    """

    def __init__(self, **kwargs):
        """
        Construtor.
        """

        self.params = kwargs

    def get_json_response(self, method):
        """
        Pega a resposta da requisição em json.
        """
        api = API(self.params["license_plate"], self.params["renavam"], method)
        return api.fetch()

    def debt_search(self):
        """
        Pega os débitos de acordo com a opção passada.
        """

        if self.params['debt_option'] == 'ticket':
            response_json = self.mount_debt_data(multas=self.get_json_response("ConsultaMultas"))

        elif self.params['debt_option'] == 'ipva':
            response_json = self.mount_debt_data(ipva=self.get_json_response("ConsultaIPVA"))

        elif self.params['debt_option'] == 'dpvat':
            response_json = self.mount_debt_data(dpvat=self.get_json_response("ConsultaDPVAT"))

        elif self.params['debt_option'] == None:
            response_json = self.mount_debt_data(multas=self.get_json_response("ConsultaMultas"),
                                                ipva=self.get_json_response("ConsultaIPVA"),
                                                dpvat=self.get_json_response("ConsultaDPVAT"))
                                    
        else:
            raise Exception("opção inválida")

        return response_json

    def mount_debt_data(self, **kwargs):
        ipva = kwargs.get('ipva')
        dpvat = kwargs.get('dpvat')
        multas = kwargs.get('multas')

        debts = defaultdict()

        if ipva:
            debts['IPVAs'] = ipva.get('IPVAs') or {}
        if dpvat:
            debts['DPVATs'] = dpvat.get('DPVATs') or {}
        if multas:
            debts['Multas'] = multas.get('Multas') or {}

        for debt in debts:
            if debts[debt] == {}:
                debts[debt] = None

        return debts