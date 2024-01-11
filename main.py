import pyautogui
import keyboard

import threading 
import time
import os

class LC_Terminal():

    def __init__(self):

        self.plrs = []
        self.radar_boosters = []
        self.is_terminal_mode = False
        self.help_list = {

            "help": "Displays useful information about a command. Usage:help [command_name(Optional)]",
            "add": "Add a player to the player list. Usage: add [player_name]",
            "remove": "Remove a player from the player list. Usage: remove [player_name]",
            "players": "Returns a list of all current players.",
            "add_radar": "Registers a new radar booster. Usage: add_radar [radar_name]",
            "remove_radar": "Removes a radar booster from the register. Usage: remove_radar [radar_name]",
            "radars": "Returns a list of all registered radar boosters.",
            "exit": "Exits the program."

        }


    def help(self, command: str = None):

        if command != None:

            if command in list(self.help_list.keys()):

                output = "{} | {}".format(command, self.help_list[command])
                print(output)
                return
            
            else:

                print("Command not found.")


        else:

            output = []

            for key, value in self.help_list.items():

                output.append("{} | {}".format(key, value))

            print("All commands:\n")

            for i in output:

                print(i)

            print("\n")

        return


    def add(self, player: str = None):

        if player == None: return

        self.plrs.append(player)

        return


    def remove(self, player: str = None):

        if player == None: return

        for existing_player in self.plrs:

            if existing_player == player:

                self.plrs.remove(existing_player)
                return
            
        print("Player not found: {}".format(player))

        return


    def players(self):

        for player in self.plrs:

            print(player)

        return
    

    def add_radar(self, radar_name: str = None):

        if radar_name == None: print("Enter a radar booster name."); return 

        self.radar_boosters.append(radar_name)

        print("Added {} to register.".format(radar_name))

        return


    def remove_radar(self, radar_name: str = None):

        if len(self.radar_boosters) == 0:

            print("There are no registered radar boosters.")
            return 
        
        elif not radar_name in self.radar_boosters or radar_name == None:

            print("Enter a valid radar booster name")
            return 
        
        else:

            self.radar_boosters.remove(radar_name)
            print("Removed {} from register.")

        return


    def radars(self):

        if len(self.radar_boosters) < 1: print("There are no registered radar boosters.")

        for radar in self.radar_boosters:

            print(radar)

        return
    
    def exit(self):

        return os._exit(0)
        

# ------------------------------------------------------------------------------------------------------------------------------------------------


terminal = LC_Terminal()

def terminal_input_handler():

    while True:

        user_input = input("Enter a command: ")

        input_split = user_input.split()

        command = input_split[0] 

        args = [input_split[i] for i in range(1, len(input_split))]

        if command in [func for func in dir(LC_Terminal) if callable(getattr(LC_Terminal, func)) and not func.startswith("__")]:

            command_refs = {

                "help": terminal.help,
                "add": terminal.add,
                "remove": terminal.remove,
                "players": terminal.players,
                "add_radar": terminal.add_radar,
                "remove_radar": terminal.remove_radar,
                "radars": terminal.radars,
                "exit": terminal.exit

            }

            if len(args) < 1:
                command_refs[command]()
            else:
                command_refs[command](args[0])

        else:

            print("Unknown command.\n")


# ---------------------------------------------------------------------------------


def keyboard_handler():

    while True:

        key = keyboard.read_key()

        if key == "*":

            terminal.is_terminal_mode = not terminal.is_terminal_mode

            if terminal.is_terminal_mode == True:
                print("\nTerminal mode enabled.\n")
            else:
                print("\nTerminal mode disabled.\n")

        if terminal.is_terminal_mode:

            if key == "0":
                pyautogui.press("backspace")
                pyautogui.write("switch")
                pyautogui.press("enter")

            elif key in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:

                if not int(key) > len(terminal.plrs):

                    pyautogui.press("backspace")
                    pyautogui.write("switch " + terminal.plrs[int(key) - 1])
                    pyautogui.press("enter")

        time.sleep(0.1)

terminal_handler_thread = threading.Thread(target=terminal_input_handler, args=())
terminal_handler_thread.start()

keyboard_handler_threat = threading.Thread(target=keyboard_handler, args=())
keyboard_handler_threat.start()