import os
import ast


class Electorate:
    def __init__(self, nElecName, nState, nIncumbent, nParty, nCompetitorParty, nMargin):
        self.name = nElecName
        self.state = nState
        self.incumbent = nIncumbent
        self.party = nParty
        self.competitorParty = nCompetitorParty
        self.margin = float(nMargin)


class Candidate:
    def __init__(self, nElecName, nState, nFirstName, nLastName, nPartyShort, nPartyLong, nGender, nIncumbent):
        self.elecName = nElecName
        self.state = nState
        self.firstName = nFirstName
        self.lastName = nLastName
        self.partyShort = nPartyShort
        self.partyLong = nPartyLong
        self.gender = nGender
        self.incumbent = nIncumbent
        self.candidateNumber = 0

def setup():
    print("Welcome to the 2022 Election Pendulum simulator!")
    input("Press Enter to continue...")
    electorateslist = []
    candidateslist = []
    # Using readlines()
    file1 = open('basedatafile.txt', 'r')
    lines = file1.readlines()
    file2 = open('candidates.csv', 'r')
    lines2 = file2.readlines()
    totallines = 0
    count = 0
    for line in lines:
        totallines += 1

    for line in lines:
        count += 1
        removenewline = line.strip('\n')
        values = removenewline.split('\t')
        electorateslist.append(Electorate(values[0], values[1], values[2], values[3], values[4], values[5]))
        print("Electorate " + str(count) + " of " + str(totallines) + " successfully loaded.")
    print("All electorates loaded.")
    input("Press Enter to continue...")
    want_to_quit = False

    for line in lines2:
        removenewline = line.strip('\n')
        values = removenewline.split(',')
        candidateslist.append(Candidate(values[0], values[1], values[2], values[3], values[4], values[5], values[6],
                                        values[7]))
    print("All candidates loaded.")
    input("Press Enter to continue...")



    while not want_to_quit:
        os.system('cls')
        print("If you would like to search for an electorate to view its candidates, type 1.")
        print("If you would like to quit, type Q.")
        print("Data from tallyroom.com.au")
        choice = input("")
        while choice not in ["1", "Q"]:
            choice = input("Please select a valid option.")
        if choice == "1":
            search_complete = False
            finished_with_electorate = False
            while not search_complete:
                print("\n\nEnter the name or part of the name of the electorate you wish to search for (Capital for first letter of name).")
                query = input("")
                print("The following results were found.")
                print("Type the name of the desired electorate exactly as it appears below to select it.")
                print("If there is nothing below, no results were found.\n\n")
                list_of_electorates = ""
                format_counter = 0
                results_counter = 0
                list1 = []
                list2 = []
                list3 = []
                longest_list = None
                for i in electorateslist:
                    if query == i.name:
                        os.system('cls')
                        selected_electorate = i
                        search_complete = True
                        break
                    if query in i.name and format_counter <= 1:
                        results_counter += 1
                if not search_complete:
                    for i in electorateslist:
                        if query in i.name and format_counter == 0:
                            distance = 16 - len(i.name)
                            list_of_electorates += (i.name + (" " * distance))
                            format_counter += 1
                        elif query in i.name and format_counter == 1:
                            distance = 16 - len(i.name)
                            list_of_electorates += (i.name + (" " * distance))
                            format_counter += 1
                        elif query in i.name and format_counter == 2:
                            list_of_electorates += (i.name + "\n")
                            format_counter = 0
                    print(list_of_electorates)
            while not finished_with_electorate:
                os.system('cls')
                print("You have selected the electorate of " + selected_electorate.name + ".")
                print("This electorate is in " + selected_electorate.state + ".")
                print("The member for this electorate in 2021 is " + selected_electorate.incumbent + ".")
                print("The member for this electorate's party is " + selected_electorate.party + ".")
                print("This member held or gained this seat at its last election by a margin of " + str(
                    selected_electorate.margin) + "%.")
                print(
                    "The party of the closest candidate at this seat's last election was " + selected_electorate.competitorParty + ".")
                print("The announced candidates for this electorate in 2022 are:\n")
                candidate_count = 1
                for i in candidateslist:
                    if i.elecName == selected_electorate.name:
                        print(f"{candidate_count}. {i.firstName} {i.lastName}")
                        i.candidateNumber = candidate_count
                        candidate_count += 1
                print("Please input the number of the candidate you wish to read about, or type Q to return to the "
                      "main menu.")
                search = input("")
                if search == "Q":
                    finished_with_electorate = True
                if not finished_with_electorate:
                    while not search.isnumeric():
                        print("Please input the number of the candidate you wish to read about.")
                        search = input("")
                    for i in candidateslist:
                        if i.candidateNumber == int(search):
                            selected_candidate = i
                            break
                    os.system('cls')
                    print(f"You have selected {selected_candidate.firstName} {selected_candidate.lastName}.")
                    print("This candidate is in " + selected_candidate.state + ".")
                    print(f"This candidate will be contesting the electorate of {selected_candidate.elecName}.")
                    print(f"This candidate is a member of {selected_candidate.partyLong} ({selected_candidate.partyShort}).")
                    if selected_candidate.gender == "M":
                        print("This candidate is male.")
                    else:
                        print("This candidate is female.")
                    elecName = selected_electorate.incumbent.split(" ")
                    if selected_candidate.firstName == elecName[0] and selected_candidate.lastName == elecName[1]:
                        print("This candidate is the incumbent.")
                    else:
                        print("This candidate is not the incumbent.")
                    print("Press any key to return to the electorate.")
                    input("")



        if choice == "Q":
            break


if __name__ == '__main__':
    setup()
