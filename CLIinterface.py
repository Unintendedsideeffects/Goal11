import os
import sys
import re
sys.path.append(os.path.realpath('.'))
from pprint import pprint

import inquirer


# TODO conflicts


def searchSettlementByPosition():
        questions = [
            inquirer.Text('lat', message = 'Input the latitude'),
            inquirer.Text('lon', message = 'Input the longitude')
            ]
            # TODO add validator

        answers = inquirer.prompt(questions)
        pprint(answers)

        requestedLocation = [answer['lat'], answer['lon']]
        
        closeBySettlements = []
        for settlement in listOfSettlements:
            if distance(requestedLocation, settlement.location, distanceMax):
                closeBySettlements.append(settlement)

# TODO names
def settlementChoice():

    questions = [
        inquirer.List('settlements',
                                message = 'Pick a settlement',
                                choices = closeBySettlements),
                                ]

    answer = inquirer.prompt(questions)

    def singleSettlementChoice(settlement):
        # TODO listoflayers
        questions   = [
        inquirer.Confirm('DownloadLayer0', message = 'Do you want to download the settlement satellite map?', default = True),
        ]

        if(answer):
            notImplemented
            # dowload layer 0

        questions = [
        inquirer.Checkbox('layers', message = 'Pick the layers you want to download', choices = listoflayers),
        ]

        answers = inquirer.prompt(questions)
        if(answers.size > 0):
            download(answers)


searchSettlementByPosition()