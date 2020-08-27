import keyboard as kb
import pandas as pd
import sys
import time

class Main():
    def __init__(self):
        self.currentIndex = 0
        self.entryList = pd.read_csv(sys.argv[1])
        kb.add_hotkey(",", self.prev_entry)
        kb.add_hotkey("-", self.next_entry)
        kb.add_hotkey(".", self.current_entry)
        kb.wait()
    
    def next_entry(self):
        if self.currentIndex + 1 < len(self.entryList.index):
            self.currentIndex += 1
            self.paste_current_system()
        else:
            print("End of list")

    def prev_entry(self):
        if self.currentIndex > 0:
            self.currentIndex -= 1
            self.paste_current_system()
        else:
            print("Anfang der Liste")

    def current_entry(self):
        if 0 <= self.currentIndex < len(self.entryList.index):
            self.paste_current_system()
        else:
            print("Kein Listenelement ausgewählt")
    
    def paste_current_system(self):
        entry = self.entryList.iloc[self.currentIndex]
        sysName = entry["System Name"]
        refuel = entry["Refuel"]
        neutron = entry["Neutron Star"]

        notes = ""

        if neutron == "No":
            notes += " | Kein Neutron!"

        if refuel == "Yes":
            notes += " | Refuel!"

        print(f"{self.currentIndex}: System - {sysName}{notes}")
        pressKey("i")
        time.sleep(0.5)
        pressKey("e")
        time.sleep(0.1)
        pressKey("o")
        time.sleep(0.1)
        kb.write(sysName)
        time.sleep(0.1)
        pressKey("enter")
        time.sleep(3)
        pressKey("o")
        time.sleep(0.5)
        pressKey("j")

def pressKey(key: str):
    kb.press(key)
    time.sleep(0.2)
    kb.release(key)

if __name__ == "__main__":
    Main()