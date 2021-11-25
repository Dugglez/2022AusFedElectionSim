--------------------------------------------------------------------------------------



		   2022 Australian Federal Election Pendulum


				     By


				   Dugglez



---------------------------------------------------------------------------------------

1. Features
2. How to Run


1. Features

- Contains data from the 2019 election in the file named "basedatafile.txt". These values are separated by tabs. If you would like to make up your own electorates, you can do so in the following format (tabs between each variable):

Electorate_Name	Electorate_state	Electorate_Incumbent	Electorate_Party_Acronym	Electorate_Competitor_Party	Electorate_Margin

Electorate_Name: The name of the electorate, e.g. Higgins
Electorate_State: The state of the electorate, e.g. VIC
Electorate_Incumbent: The Member currently representing the electorate, e.g. Katie Allen
Electorate_Party_Acronym: The acronym of the member's party, e.g. LIB
Electorate_Competitor_Party: The acronym of the party that came 2nd in the last election of that seat, e.g. ALP
Electorate_Margin: The percentage of votes by which the member won the seat, e.g. 3.7 (do not include a percentage sign)

- Features an electorate search engine to search through all electorates matching the search query. Below is shown the output from a search for the letter 'e'. (Electorate names are case sensitive, i.e. requires a capital at the start of an electorate name)

Adelaide        Barker          Bean
Bendigo         Bennelong       Berowra
Bonner          Bradfield       Brisbane
Bruce           Calare          Calwell
Canberra        Casey           Chifley
Cooper          Corangamite     Cowper
Deakin          Dobell          Dunkley
Eden-Monaro     Fadden          Farrer
Fenner          Fisher          Flinders
Forde           Forrest         Fowler
Fraser          Fremantle       Gellibrand
Gilmore         Grayndler       Greenway
Goldstein       Grey            Hawke
Herbert         Hinkler         Hughes
Hume            Hunter          Kennedy
La Trobe        Leichhardt      Lilley
Lyne            Mackellar       Macquarie
Mallee          McEwen          McPherson
Melbourne       Menzies         Mitchell
Moncrieff       Moore           Moreton
New England     Newcastle       North Sydney
Oxley           Page            Parkes
Paterson        Pearce          Perth
Petrie          Reid            Riverina
Robertson       Spence          Sydney
Tangney         Wentworth       Werriwa
Wide Bay

- After selecting an electorate, displays all available information about the electorate. Here is the output for the electorate of Wide Bay.

You have selected the electorate of Wide Bay.
This electorate is in Qld.
The member for this electorate in 2021 is Llew O'Brien.
The member for this electorate's party is LIB.
This member held or gained this seat at its last election by a margin of 13.1%.
The party of the closest candidate at this seat's last election was ALP.

- When you've selected an electorate, you can choose to simulate a by-election. Since this is the most interesting part of the program, I'll leave it to you to discover.

- You can also simulate a general swing in a federal election. Again, you'll have to find out about this yourself.

2. How to run

I'm fairly new at this, but these steps should work for most Windows PCs. (If you're on something else, use a YouTube Tutorial)

1. Download the repository
2. Make sure the 'main.py' and 'basedatafile.txt' files are in the same place.
3. At the location where you have saved these files, open the command line at this location by typing in 'cmd' to the address bar in Windows Explorer.
4. If the command line has something like C:\Users\Dugglez\PycharmProjects\2022Pendulum>, you are in the right place.
5. Type in 'python main.py' and press enter. The program should start automatically.
6. After getting past the main page, you should see 151 electorates load. If this happens, you are ready to go.
