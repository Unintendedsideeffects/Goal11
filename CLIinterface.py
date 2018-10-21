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
from Weather import weather

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
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
        closeBySettlements = extractSettlementsNames(requestedLocation, 10)
        if len(closeBySettlements) <= 0:
            print('No settlements in the area nearby')
            clear()
            mainMenu()
        settlementChoice(closeBySettlements)

def settlementChoice(choices):
    questions = [
        inquirer.List('settlement',
                                message = 'Pick a settlement',
                                choices = choices),
                                ]
    answer = inquirer.prompt(questions)
    singleSettlementChoice(answer.get('settlement'))

def singleSettlementChoice(settlementName):
        settlement = getSettlementsByName(settlementName)
        settlementcoordinates = [float(settlement["LAT"]),float(settlement["LONG"])]
        choices = getListOfLayers()
        questions   = [
        inquirer.Confirm('DownloadLayer0', message = 'Do you want to download the settlement satellite map?', default = True),
        ]
        answer = inquirer.prompt(questions)

        if(answer.get('DownloadLayer0')):
            path = downloadImage(settlementName, settlementcoordinates)
            print('We just finished downloading the image would you like to check that out? It\'s at ' + path)

        questions = [
        inquirer.Checkbox('layers', message = 'Pick the layers you want to download', choices = choices),
        ]
        answers = inquirer.prompt(questions)
        if answers.get('layers') is not None:
            for answer in answers.get('layers'):
               path = downloadImage(settlementName, settlementcoordinates, layerNumberFromName(answer))
               print('We just finished downloading the image would you like to check that out? It\'s at ' + path)

        else:
            questions = [
                inquirer.List('nochoice', message = 'You haven\'t  picked any layer, do you want to retry or go back to the main menu?', choices = ['Retry', 'Main Menu']),
            ]
            answer = inquirer.prompt(questions)
            if answer.get('nochoice') == 'Retry':
                singleSettlementChoice(settlement)
            elif answer.get('choice') == 'Main Menu':
                mainMenu()

# TODO names

def pickdate():
    questions =  [
        inquirer.Text('year', message= 'pick the year'),
        inquirer.Text('month', message = 'pick the month'),
        inquirer.Text('day', message = 'pick the day')
    ]
    answers = inquirer.prompt(questions)

    date = ("{}{}{}{}{}".format(answers.get('year'), "-", answers.get('month'), '-', answers.get('day')))

    return date

    

def settlementInfo(settlementName):
        # Weather
        # Conflicts
        questions = [
            inquirer.List('SettlementInfo', choices = ['Weather', 'Conflicts'] )
        ]
        answer = inquirer.prompt(questions)
        if answer.get('SettlementInfo') == 'Weather':
            weatherMenu(settlementName)
        elif answer.get('SettlementInfo') == 'Conflicts':
            conflictsMenu(settlementName)

def todayWeatherdisplay(coordinates):
    weatherChannel = weather(coordinates)
    print('{}{}'.format("The weather today is: ", weatherChannel[0]))
    print('{}{}{}{}'.format('min: ', weatherChannel[1], ' max: ', weatherChannel[2]))

    questions= [
        inquirer.List('TodayWeatherChannel', message= 'Would you like to go back or do you want to browse for a specific date?', choices= ['Specific Date', 'Main Menu', 'Exit']),
    ]
    answer = inquirer.prompt(questions)
    if answer.get('TodayWeatherChannel') == 'Main Menu':
        clear()
        mainMenu()
    elif answer.get('TodayWeatherChannel') == 'Specific Date':
        clear()
        pickdate()
    elif answer.get('TodayWeatherChannel') == 'Exit':
        clear()
        exit()
    
def weatherMenu(settlementName):
        questions = [
            inquirer.List('weatherMenu', message='Do you want to know the weather here today or do you want to browse historical data?', choices=['Weather Today', 'Historical Data', 'Main Menu', 'Exit'])
        ]
        answer = inquirer.prompt(questions)

        if answer.get('weatherMenu') == 'Weather today':
            clear()
            coordinates = getCoordinatesByName(settlementName)
            todayWeatherdisplay(coordinates)
        elif answer.get('weatherMenu') == 'Historical Data':
            NotImplemented
        elif answer.get('weatherMenu') == 'Main Menu':
            mainMenu()
        elif answer.get('weatherMenu') == 'Exit':
            exit()


mainMenu()
