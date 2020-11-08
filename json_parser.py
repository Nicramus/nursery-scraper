from nursery import Nursery
import json

class JsonParser:
    """
    JsonParser need to be created for every request 
    The purpose of this class is parse nursery json data
    """
    def __init__(self, nursery_json: str):
       self.nursery_json = nursery_json
       self.json = json.loads(nursery_json).get('data')
       self.parsed_nursery_list = [] #list of parsed data (objects)
       self._parse_data_to_list()

    def _parse_data_to_list(self) -> list:
        for list_item in self.json:
            nursery = Nursery()
            nursery.register_number = list_item[0]['val']
            nursery.institution_type = list_item[1]['val']
            nursery.institution_name = list_item[2]['val']
            nursery.localization = list_item[3]['val']
            nursery.website_url = list_item[4]['val']
            nursery.e_mail = list_item[5]['val']
            nursery.telephone_number = list_item[6]['val']
            nursery.capacity = list_item[7]['val']
            nursery.children_assigned = list_item[8]['val']
            nursery.month_payment = list_item[9]['val']        
            nursery.food_payment = list_item[10]['val']
            nursery.discounts = list_item[11]['val']
            nursery.when_open = list_item[12]['val']
            nursery.is_ready_for_disabled = list_item[13]['val']
            nursery.host_entity_name = list_item[14]['val']
            nursery.nip = list_item[15]['val']
            nursery.regon = list_item[16]['val']
            nursery.host_entity_registry_number = list_item[17]['val']
            nursery.host_entity_website_url = list_item[18]['val']
            nursery.is_activity_suspended = list_item[19]['val']
            #nursery.map_url = list_item[20]['val'] #sometimes map_url is not present
            self.parsed_nursery_list.append(nursery)

    def get_parsed_nursery_json(self) -> list:
        #TODO return already parsed list with Nursery
        return self.parsed_nursery_list


#test
#test_file: str = 'sample_response.json'
#with open(test_file) as f:
#    nursery_test_file = f.read()

#json_parser = JsonParser(nursery_test_file)
#print(json_parser.get_parsed_nursery_json())
#json_list: list = json_parser.json
#aaa = json_list[0]
#print(aaa)
# for list_item in json_list:
    # print(list_item)

#any(x for x in json_result if x.n == 10)

# row = json_result[0]
# registry_number = json_result[0]['val']
# nursery_type = json_result[1]['val']
# name = json_result[2]['val'] 

# nursery = Nursery()
# nursery.register_number = json_result[0]['val']
# nursery.institution_type = json_result[1]['val']
# nursery.institution_name = json_result[2]['val']
# nursery.localization = json_result[3]['val']
# nursery.website_url = json_result[4]['val']
# nursery.e_mail = json_result[5]['val']
# nursery.telephone_number = json_result[6]['val']
# nursery.capacity = json_result[7]['val']
# nursery.children_assigned = json_result[8]['val']
# nursery.month_payment = json_result[9]['val']
# nursery.food_payment = json_result[10]['val']
# nursery.discounts = json_result[11]['val']
# nursery.when_open = json_result[12]['val']
# nursery.is_ready_for_disabled = json_result[13]['val']
# nursery.host_entity_name = json_result[14]['val']
# nursery.nip = json_result[15]['val']
# nursery.regon = json_result[16]['val']
# nursery.host_entity_registry_number = json_result[17]['val']
# nursery.host_entity_website_url = json_result[18]['val']
# nursery.is_activity_suspended = json_result[19]['val']
# #nursery.map_url = json_result[20]['val'] #sometimes map_url is not present

# print(json_result[0])
# assert json_result != None
