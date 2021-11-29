import sys
import requests
from tabulate import tabulate


class CLI:


    def answer_of_main_menu(self):
        print("\n Welcome to the ticket viewer")
        print('\n Type "menu" to view options or "quit" to exit')
        val = input()
        return val

    def answer_of_ticket_menu(self):
        print("\n Type 1 to view all tickets")
        print("\n Type 2 to view a ticket")
        print("\n Type quit to exit")
        print('\n Type "back" to go back to main menu')
        val1 = input()
        return val1


    def view_all_tickets(self):
        # count_shown_ticket = 0
        url = "https://zccpranav.zendesk.com/api/v2/tickets.json?page[size]=25"
        # count_url = 'https://zccpranav.zendesk.com/api/v2/tickets/count'
        user = "pranavnaik0700@gmail.com"
        f = open(r'C:\Users\naikp\PycharmProjects\Zendesk\src\password', 'r')
        content = f.read()
        pwd=content
        # Do the HTTP get request
        headersAPI = {
            "accept": "application/json",
            "Authorization": "Bearer"
            "25aa76d0368709d1af774bd4df74287e036f3634c9aa2d4a791ec5fda13dd8b0",
        }
        # count_response = requests.get(count_url, params=headersAPI, auth=(user, pwd))
        # count_data = count_response.json()
        while url:
            # count=count_data['count']['value']
            response = requests.get(url, params=headersAPI, auth=(user, pwd))
            data = response.json()
            if response.status_code != 200:
                print("Status:", response.status_code, "Problem with the request. Exiting.")
                return response.status_code
                exit()
                # Decode the JSON response into a dictionary and use the data
            temp = []
            for ticket in data['tickets']:
                temp.append(
                    [
                        ticket["id"],
                        ticket["created_at"],
                        ticket["updated_at"],
                        ticket["subject"],
                    ]
                )

            # print("There are total {} tickets, {} are shown below".format(count,temp.__len__()))
            print(
                tabulate(
                    temp, headers=["Ticket ID", "Created At", "Last updated At", "Subject"]
                )
            )
            # count_shown_ticket+=temp.__len__()

            if data['meta']['has_more']:
                url = data['links']['next']
                print("press 'n' to view more tickets")
                output = input("")
                if output != "n":
                    break
            else:
                url = None
        return response.status_code


    def view_ticket(self, ticket_number):
        url = "https://zccpranav.zendesk.com/api/v2/tickets/" + str(ticket_number)
        count_url = "https://zccpranav.zendesk.com/api/v2/tickets/count"
        user = "pranavnaik0700@gmail.com"
        f = open(r'C:\Users\naikp\PycharmProjects\Zendesk\src\password', 'r')
        content = f.read()
        pwd = content
        # Do the HTTP get request
        headersAPI = {
            "accept": "application/json",
            "Authorization": "Bearer"
            "25aa76d0368709d1af774bd4df74287e036f3634c9aa2d4a791ec5fda13dd8b0",
        }
        response = requests.get(url, params=headersAPI, auth=(user, pwd))
        count_response = requests.get(count_url, params=headersAPI, auth=(user, pwd))
        count_data = count_response.json()
        ticket_exist = True
        count = count_data["count"]["value"]
        data = response.json()
        # Check for HTTP codes other than 200
        if ticket_number > count:
            print("uh oh!, Ticket id does not exist")
            ticket_exist = False
        if response.status_code != 200:
            print("Status:", response.status_code, "Problem with the request. Exiting.")
            return {'status' :response.status_code, 'exist' :ticket_exist,'result' : response}
            exit()
            # Decode the JSON response into a dictionary and use the data
        # print(data)
        ticket_results = []

        ticket_results.append(
            [
                data["ticket"]["id"],
                data["ticket"]["created_at"],
                data["ticket"]["updated_at"],
                data["ticket"]["subject"],
            ]
        )
        print(
            tabulate(
                ticket_results,
                headers=["Ticket ID", "Created At", "Last updated At", "Subject"],
            )
        )
        return {'status' :response.status_code, 'exist' :ticket_exist,'result' : response}


    def show_output(self, number):
        if int(number) == 1:
            self.view_all_tickets()
        else:
            print("Enter ticket number")
            ans = input()
            self.view_ticket(int(ans))

    def start(self):
        while True:
            main_menu = self.answer_of_main_menu()
            invalid_input_error = main_menu + " is not valid input"
            if main_menu == "quit":
                break
            elif main_menu == "menu":
                ticket_menu = self.answer_of_ticket_menu()
                # print(type (int(ticket_menu)))
                if ticket_menu == "quit":
                    break
                if ticket_menu == "back":
                    continue
                elif ticket_menu.isnumeric() and (
                    int(ticket_menu) == 1 or int(ticket_menu) == 2
                ):
                    self.show_output(ticket_menu)
                else:
                    print(ticket_menu + " is not valid input")
            else:
                print(invalid_input_error)
        sys.exit()

cli=CLI()
cli.start()