import os
import sys
import re
sys.path.append(os.path.realpath('.'))
from pprint import pprint
from distance import distance
from accessoryData import getListOfLayers
import inquirer
from ExtractSettlements import *
from GetImages import *
from convert import *
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
        closeBySettlements = extractSettlements(requestedLocation, 30)
        closeBySettlementsNames = []
        for settlement in closeBySettlements['NAME']:
            closeBySettlementsNames.append(settlement['NAME'])
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

    def pickdate():
        questions =  [
            inquirer.Text('year', message= 'pick the year'),
            inquirer.Text('month', message = 'pick the month'),
            inquirer.Text('day', message = 'pick the day')
        ]
        answers = inquirer.prompt(questions)

        date = ("{}{}{}{}{}".format(answers.get('year'), "-", answers.get('month'), '-', answers.get('day')))

        return date

    def singleSettlementChoice(settlementName):
        settlement = getSettlementsByName(settlementName)
        settlementcoordinates = [float(settlement["LAT"]),float(settlement["LONG"])]
        choices = getListOfLayers()
        questions   = [
        inquirer.Confirm('DownloadLayer0', message = 'Do you want to download the settlement satellite map?', default = True),
        ]
        answer = inquirer.prompt(questions)

        if(answer.get('DownloadLayer0')):
            downloadImage(settlementName, settlementcoordinates)
            # type = 0 is an Int

        questions = [
        inquirer.Checkbox('layers', message = 'Pick the layers you want to download', choices = choices),
        ]
        # pprint(requestedLocation)
        answers = inquirer.prompt(questions)
        if answers.get('layers') is not None:
            downloadImage(settlementName, settlementcoordinates,  layerNumberFromName(answer.get('layers')))
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
                NotImplemented

mainMenu()
