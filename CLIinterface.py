import os
import sys
import re
sys.path.append(os.path.realpath('.'))
from pprint import pprint
from distance import distance
import dir
from accessoryData import getListOfLayers
import inquirer
import 

# TODO conflicts

def mainMenu():
    questions = [
        inquirer.List('mainMenu', message='Welcome to Goal 11', choices= ['Search Settlement', 'Exit']),
    ]
    answer = inquirer.prompt(questions)

    if answer.get('mainMenu') == 'Search Settlement' :
        searchSettlementByPosition()
    elif answer.get('mainMenu') == 'Exit':
        exit()


def searchSettlementByPosition():
        questions = [
            inquirer.Text('lat', message = 'Input the latitude'),
            inquirer.Text('lon', message = 'Input the longitude'),
            ]
        answer = inquirer.prompt(questions)
        requestedLocation = [answer.get('lat'), answer.get('lon')]

        closeBySettlements = []
        for settlement in listOfSettlements:
            if distance(requestedLocation, settlement.location, distanceMax = 'default'):
                closeBySettlements.append(settlement)
        settlementChoice(closeBySettlements)

# TODO names
def settlementChoice(choices):
    questions = [
        inquirer.List('settlement',
                                message = 'Pick a settlement',
                                choices = choices),
                                ]
    answer = inquirer.prompt(questions)
    singleSettlementChoice(answer.get('settlement'))


    def singleSettlementChoice(settlement):

        choices = getListOfLayers()
        questions   = [
        inquirer.Confirm('DownloadLayer0', message = 'Do you want to download the settlement satellite map?', default = True),
        ]
        answer = inquirer.prompt(questions)

        if(answer):
            downloadImage('SettlementName', coordinates, date)
            # type = 0 is an Int

        questions = [
        inquirer.Checkbox('layers', message = 'Pick the layers you want to download', choices = choices),
        ]
        # pprint(requestedLocation)
        answers = inquirer.prompt(questions)
        if(answers[''] > 0):
            for answer in answers():
                downloadImage(answer)
        else:
            questions = [
                inquirer.List('nochoice', message = 'You haven\'t  picked any layer, do you want to retry or go back to the main menu?', choices = ['Retry', 'Main Menu']),
            ]
            answer = inquirer.prompt(questions)
            if answer.get('nochoice') == 'Retry':
                singleSettlementChoice(settlement)
            elif answer.get('choice') == 'Main Menu':
                mainMenu()

            def settlementInfo():

                numberOfConflicts(path, coordinates, number)
                # numberOfConflicts(path, coordinates, numberofYears)
searchSettlementByPosition()
