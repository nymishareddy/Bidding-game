import json
import random
from colorama import Fore,Back,Style
import pyttsx3

engine = pyttsx3.init()
player_money = 120000
print( Back.LIGHTMAGENTA_EX +"\t\t\t\t\t\t\t\t\t\t\t😊😊WELCOME TO THIS INTERESTING BIDDING GAME😊😊")
print(Style.RESET_ALL)
print(Fore.LIGHTRED_EX+"Rules💫")
print(Style.RESET_ALL)
def rules():
    print("There a 6 topics in this game")
    print("Any of the topic need to chosen from those 6")
    print("Each of the topic has 6 questions")
    print("Each question has a clue")
    print("Players can also take hints by paying Rs.20,000")
rules()

print("Are you ready 🤗?")
player_name = input(Fore.BLUE+"Enter the name of player : ")
print(Style.RESET_ALL)
player_name=Fore.CYAN+player_name
print(f"{player_name} has 120000 amount with you now!!!")
print(Style.RESET_ALL)

print("Select any topic from the following for the quiz : ")
topic = {1:"TV_shows_and_movies",2:"Riddles",3:"Mythology",4:"Sports",5:"Geography",6:"General_Knowledge"}
print(topic)
chosen = int(input("\nSelect any topic from 1 to 6 in the given topics : "))
selected_topic = topic[chosen]
print("You have chosen : ",selected_topic)
def player_bid(player_name,player_money):
    print(f"{player_name} have {player_money} in your account")
    print(Style.RESET_ALL)
    bid = int(input("Enter the bid amount : "))
    while bid <= 0 or bid>player_money  :
        print(Style.RESET_ALL)
        bid = int(input("Enter the valid amount to bid : "))
    return bid


questions = []
with open("C:/Users/Danduchandrashikara/PycharmProjects/Filehandling/Info.json","r") as f :
    d = json.load(f)
    for j in d[0][selected_topic][0]:
        questions.append(j)

def hint(selected_topic,i):
    hints = {"TV_shows_and_movies":{"Who lifted Mjolnir in avengers endgame?":"the role played by Chris Evans",
                                    "Who is the host of kaun banega karodpathi?": "Hero of the movie Sholay",
                                    "First Indian movie nominated for oscar?": "The second word in the answer is INDIA",
                                    "The song to win the oscar in the best original song category 2023?": "Ram charan and "
                                                                                                      "NTR are actors",
                                    "What is the second Harry potter movie?":"Harry has been using the diary to possess and control Ginny, who had been behaving strangely.",
                                    "Who is the director of movie bollywood three idiots?":"He is also the director of PK movie"},
           "Riddles":{"What is always in front of you but can’t be seen?": "it is related to tenses in english grammar",
                      "What gets wet while drying?": "It is usually carried to bathroom",
                      "What can you hold in your right hand but never in your left hand?": "It is one of the part of your body",
                      "What kind of band never plays music?": "Used to tie your hair",
                      "What can travel all around the world without leaving a corner?": "Ink pad is the partner of it",
                      "What can you catch but cannot throw?": "attacks in winter"},
           "Mythology":{"Which one is the first avatar of lord Vishnu?": "another name of fish",
                        "Who wrote the epic Mahabharata while vyasa was dictating?": "husband of siddhi and buddhi",
                        "For how many days did the battle of kurukshetra fought?": "jersey number of virat kohli",
                        "Who gifted the shiv danush to king janak,broken by Rama at Sita swayamvar?": "he is the guru of karna",
                        "Who is the other person in the trimurthi's along with lord Brahma and lord Vishu?": "he usually lives in kailash parvat",
                        "Who is the first wife of lord krishna?": "sister of rukmi"},
           "Sports":{"What is the begining level in karate?": "usually wears it to waist",
                     "The game of Cricket originated in which country?": "queen elizabeth II was a queen of that country",
                     "In volley ball the number of players in each side?": "also called as sextet",
                     "Which team won the ODI world cup in 2011?": "it was the last match played by god of cricket",
                     "Who is the No.1 grand master of chess in india?": "also known as father of chess in India",
                     "Who won gold medal in Javelin Throw at Tokyo olympics?": "HE WON GOLD MEDAL IN 2018 Asian games"},
           "Geography":{"Which country is the largest in the world in terms of surafce area?": " the moscow is the capital of that country",
                        "Which is the latitude that runs through the centre of the earth?": "latitude passing through africa",
                        "The tallest mountain in the world is located in which country?": "kathmandu is the capital of that country",
                        "Which is the longest river in the world?": "name of a shampoo🤷‍♀",
                        "In which city is Eiffel tower located?": "it is also known as city of love",
                        "Shortest city in the world?": "It is surrounded by Rome and Italy"},
           "General_knowledge":{"Which is the sensitive organ in our body?": "the body's largest organ",
                                "Which planet is known as red planet?": "it has very weak gravity near about 37%",
                                "Which continent is known as dark continent?": "brazil is one of the country in it",
                                "Who is popularly known as Iron man of India?": "statue of unity",
                                "General election in India hold after how many years?": "The number of sense organs in human body",
                                "Who represents statue of equality": "he is a vedic philosopher anf social reformer who revived bhakti movement"}}
    print(hints[selected_topic][i])


def ques(a,player_money):
    print(Style.RESET_ALL)
    random.shuffle(a)
    def returning_a_dictionary(q):
        with open("C:/Users/Danduchandrashikara/PycharmProjects/Filehandling/Info.json","r") as f:
            d = json.load(f)
            for j in d[0][selected_topic]:
                dictionary=j
        return dictionary
    for i in a:
        dict=returning_a_dictionary(i)
        break
    for i in a:
        print(Back.LIGHTYELLOW_EX+i)
        print(Style.RESET_ALL)
        player__bid = player_bid(player_name, player_money)
        print(Style.RESET_ALL)
        clue_1 = input("Do you want to take a clue?🤔 \n(press y for yes and n for no):")
        while (clue_1 != 'y' and clue_1 != 'n'):
            clue_1 = input("Enter either y or n for the clue : ")
            if clue_1 == 'y' or 'n':
                break
        print(Style.RESET_ALL)
        if clue_1 == 'y':
            hint(selected_topic,i)
            player__bid += 20000
        answ=input("Answer:")
        print(Style.RESET_ALL)
        if answ==dict[i]:
            engine.say("CORRECT!!!")
            print(Back.LIGHTGREEN_EX+"\t\t\t\t\t\t\t\tCORRECT🥳!!!!!")
            print(Style.RESET_ALL)
            engine.runAndWait()
            engine.stop()
            player_money += player__bid
        else:
            engine.say("INCORRECT!!!")
            print(Style.RESET_ALL)
            engine.runAndWait()
            engine.stop()
            print(Back.LIGHTRED_EX+"\t\t\t\t\t\t\t\tINCORRECT☹!!!")
            print(Style.RESET_ALL)
            player_money -= player__bid
            if player_money <= 0:
                engine.say("You lost....,good try....,better luck next time")
                print(Style.RESET_ALL)
                engine.runAndWait()
                engine.stop()
                print(Fore.CYAN+"\t\t\t\t\t\tYOU LOSE.....😢\n\t\t\t\t\t\tGOOD TRY.....😀\n\t\t\t\t\t\tBETTER LUCK NEXT TIME......😉")
                print(Style.RESET_ALL)
                break
        print(f"{player_name} have {player_money} in your account🥳🤑")
        print(Style.RESET_ALL)

ques(questions,player_money)
print("THANK YOU😀,HOPE IT WAS INTERESTING")
engine.say("Hurray!!, you won.  You have money in your account!!! . Great job, keep going.........Thank you for playing")
engine.runAndWait()
engine.stop()