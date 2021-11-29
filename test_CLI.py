import unittest
import CLI
import requests

class TestCLI(unittest.TestCase):

    def test_api(self):   #(checks both methods)
        #one happy case(response_code=200)
        #other cases will return the respective status codes

    def test_view_ticket_id(self):  #checks viewticket() method
        #one happycase
        #one invalid ticket id case
        #one case where ticket id is not integer

    def test_CLIInput(self):    #checks user input
        #one happycase
        #one invalid input from user

    def test_view_all_ticket(self):
        #one happycase
