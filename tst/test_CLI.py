import unittest
from src.CLI import CLI
from tst.fixtures.cli_fixtures import *
import responses
import requests

class TestCLI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cli = CLI()

    @responses.activate
    def test_view_ticket_id(self):   #(checks both methods)
        url = "https://zccpranav.zendesk.com/api/v2/tickets/45"
        url_count = "https://zccpranav.zendesk.com/api/v2/tickets/count"
        responses.add(responses.GET, url,json=view_by_ticket_response, status=200)
        responses.add(responses.GET, url_count, json=view_by_count_response, status=200)
        response=self.cli.view_ticket(45)
        #print(response)
        self.assertTrue(response['status'],200)
        self.assertTrue(response['exist'], True)

        url2 = "https://zccpranav.zendesk.com/api/v2/tickets/45766"
        url_count2 = "https://zccpranav.zendesk.com/api/v2/tickets/count"
        responses.add(responses.GET, url2,json=view_by_error_response, status=404)
        responses.add(responses.GET, url_count2, json=view_by_count_response, status=404)
        response2=self.cli.view_ticket(45766)
        #print(response2)
        self.assertTrue(response2['status'], 404)
        #print(response2['exist'])
        self.assertFalse(response2['exist'], False)

    @responses.activate
    def test_view_all(self):  #checks viewticket() method
        url = "https://zccpranav.zendesk.com/api/v2/tickets.json?page%5Bsize%5D=25&accept=application%2Fjson&Authorization=Bearer25aa76d0368709d1af774bd4df74287e036f3634c9aa2d4a791ec5fda13dd8b0"
        #url_count = "https://zccpranav.zendesk.com/api/v2/tickets/101"
        responses.add(responses.GET, url, json=view_by_all_response, status=200)
        #responses.add(responses.GET, url_count, json=view_by_count_response, status=200)
        response = self.cli.view_all_tickets()
        self.assertTrue(response, 200)


    # def test_CLIInput(self):    #checks user input
    #     #one happycase
    #     #one invalid input from user
    #
    # def test_view_all_ticket(self):
    #     #one happycase
