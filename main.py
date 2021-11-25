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


def setup():
    print("Welcome to the 2022 Election Pendulum simulator!")
    input("Press Enter to continue...")
    electorateslist = []
    # Using readlines()
    file1 = open('basedatafile.txt', 'r')
    lines = file1.readlines()

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
    while not want_to_quit:
        os.system('cls')
        print("If you would like to view or manipulate a specific electorate, type 1.")
        print("If you would like to simulate an election with a uniform swing and view the results, type 2.")
        print("If you would like to quit, type Q.")
        choice = input("")
        while choice not in ["1", "2", "Q"]:
            choice = input("Please select a valid option.")
        if choice == "1":
            search_complete = False
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
               ##     if len(list1) > len(list2) and len(list1) > len(list3):
                    ##          longest_list = list1
                        ##        elif len(list2) > len(list1) and len(list2) > len(list3):
                    ##           longest_list = list2
                    ##              elif len(list3) > len(list1) and len(list3) > len(list2):
                    ##               longest_list = list3
                        ##                 for i in range(round((len(list1)+len(list2)+len(list3))/3)):
                        ##                    list_of_electorates += list1[i]
                        ##                    list_of_electorates += list2[i]
                        ##                   list_of_electorates += list3[i]
                        ##               if longest_list == list1:
                    ##                   list_of_electorates += list1[-1]
                        ##                elif longest_list == list2:
                    ##                      list_of_electorates += list1[-1]
                        ##                    list_of_electorates += list2[-1]
                        ##               elif longest_list == list3:
                    ##                  list_of_electorates += list1[-1]
                        ##                 list_of_electorates += list2[-1]
                ##                  list_of_electorates += list3[-1]
            os.system('cls')
            print("You have selected the electorate of " + selected_electorate.name + ".")
            print("This electorate is in " + selected_electorate.state + ".")
            print("The member for this electorate in 2021 is " + selected_electorate.incumbent + ".")
            print("The member for this electorate's party is " + selected_electorate.party + ".")
            print("This member held or gained this seat at its last election by a margin of " + str(selected_electorate.margin) + "%.")
            print("The party of the closest candidate at this seat's last election was " + selected_electorate.competitorParty + ".")
            print("You can return to the main menu, or simulate a by-election in this electorate.")
            print("Type 1 to return, or 2 to simulate a by-election")
            choice2 = input("")
            while choice2 not in ["1", "2"]:
                choice2 = input("Please select a valid option.\n")
            if "2" in choice2:
                print("Type in a value to swing the seat away from the incumbent. A negative value will swing the seat towards the incumbent.")
                swing_input = input("Input a numeric value.\n")
                swing_value = float(swing_input)
                if (swing_value + selected_electorate.margin) < 100:
                    if (swing_value + selected_electorate.margin) > -100:
                        result = selected_electorate.margin - swing_value
                        if result < 0:
                            print("The seat was lost by " + selected_electorate.incumbent + " by a margin of " + str(result) + "%.")
                            print("The seat is now held by a " + selected_electorate.competitorParty + " candidate.")
                        if result >= 0:
                            print("The seat was held by " + selected_electorate.incumbent + " by a margin of " + str(result) + "%.")
                    else:
                        print("Swing inputted results in a percentage less than -100.")
                else:
                    print("Swing inputted results in a percentage greater than 100.")
                input("Press enter to return to the main menu.")
        if choice == "2":
            print("Type in a party acronym to swing away from.")
            print("Party acronyms are: LIB, ALP, NAT, GRN, PHON, CA, IND, KAP, UAP.")
            desired_party = input("(LNP becomes LIB for sake of simplicity, independents all swing together).\n")
            while desired_party not in ["LIB", "ALP", "NAT", "GRN", "PHON", "CA", "IND", "KAP", "UAP"]:
                desired_party = input("Please select a valid party acronym.\n")
            print("Select an amount to swing away from. Swing values over 50 or below -50 may result in a turnout greater than 100% in some seats.")
            swing_amount = input("Please select an amount to swing away by (must be between 75 and -75).\n")
            while float(swing_amount) > 75:
                swing_amount = input("Input a value less than 75.\n")
            while float(swing_amount) < -75:
                swing_amount = input("Input a value greater than -75.\n")
            swing_selected = float(swing_amount)
            lib_count = 0
            alp_count = 0
            nat_count = 0
            grn_count = 0
            phon_count = 0
            ca_count = 0
            ind_count = 0
            kap_count = 0
            uap_count = 0
            for elect in electorateslist:
                if elect.party == desired_party:
                    result = elect.margin - swing_selected
                    if result < 0:
                        print("The seat of " + elect.name + " has changed hands!")
                        temp_party = elect.party
                        elect.party = elect.competitorParty
                        elect.competitorParty = temp_party
                if elect.party != desired_party and elect.competitorParty == desired_party:
                    result = elect.margin + swing_selected
                    if result < 0:
                        print("The seat of " + elect.name + " has changed hands!")
                        temp_party = elect.party
                        elect.party = elect.competitorParty
                        elect.competitorParty = temp_party
                if elect.party != desired_party and elect.competitorParty != desired_party:
                    result = 50 + elect.margin - swing_selected
                    if result < 0:
                        print("The seat of " + elect.name + " has changed hands!")
                        temp_party = elect.party
                        elect.party = desired_party
                        elect.competitorParty = temp_party
                if elect.party == "LIB":
                    lib_count += 1
                if elect.party == "ALP":
                    alp_count += 1
                if elect.party == "NAT":
                    nat_count += 1
                if elect.party == "GRN":
                    grn_count += 1
                if elect.party == "PHON":
                    phon_count += 1
                if elect.party == "CA":
                    ca_count += 1
                if elect.party == "IND":
                    ind_count += 1
                if elect.party == "KAP":
                    kap_count += 1
                if elect.party == "UAP":
                    uap_count += 1
            print("The election is over!")
            government_formed = False
            if (lib_count + nat_count) > 76:
                print("The Coalition was able to form majority government with " + str(lib_count+nat_count) + " seats.")
                government_formed = True
            if alp_count > 76:
                print("Labor was able to form majority government with " + str(alp_count) + " seats.")
                government_formed = True
            if grn_count > 76:
                print("The Greens were able to form majority government with " + str(grn_count) + " seats.")
                government_formed = True
            if phon_count > 76:
                print("Pauline Hanson's One Nation was able to form majority government with " + str(phon_count) + " seats.")
                government_formed = True
            if ca_count > 76:
                print("The Centre Alliance was able to form majority government with " + str(ca_count) + " seats.")
                government_formed = True
            if ind_count > 76:
                print("A coalition of Independents formed majority government with " + str(ind_count) + " seats.")
                government_formed = True
            if kap_count > 76:
                print("The Katter Australia Party formed majority government with " + str(kap_count) + " seats.")
                government_formed = True
            if uap_count > 76:
                print("The United Australia Party formed majority government with " + str(uap_count) + " seats.")
                government_formed = True
            if alp_count < 70 < (lib_count + nat_count) < 76:
                print("The Coalition outnumbers Labor, and forms minority government with " + str(lib_count+nat_count) + " seats.")
                government_formed = True
            if (lib_count + nat_count) < 70 < alp_count < 76:
                print("Labor outnumbers the Coalition, and forms minority government with " + str(alp_count) + " seats.")
                government_formed = True
            if (lib_count + nat_count) < 70 and alp_count < 70 and not government_formed:
                print("Due to neither party acquiring enough seats for minority government, the Parliament was declared hung.")
            print("The final seat count was:")
            print("Coalition: " + str(lib_count+nat_count))
            print("Labor: " + str(alp_count))
            print("Greens: " + str(grn_count))
            print("Pauline Hanson's One Nation: " + str(phon_count))
            print("Center Alliance: " + str(ca_count))
            print("Independents: " + str(ind_count))
            print("Katter Australia Party: " + str(kap_count))
            print("United Australia Party: " + str(uap_count))
            input("Press enter to return to the main menu.\n")
        if choice == "Q":
            break


if __name__ == '__main__':
    setup()
