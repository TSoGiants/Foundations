reject = ["a", "an", "the", "to"]

verbs = {
         "take": ["pick up", "grab", "pilfer"],
         "read": [],
         "open": [],
         "look at": ["examine", "inspect", "look"]
         }

nouns = [
        "door",
        "mailbox",
        "pamphlet",
        "knife"
        ]

s = input(">>> ")
s = s.lower().split(" ")

words = []
verb = ""
noun = ""
for word in s:
    if word in verbs:
        verb = word
    else:
        for key in verbs.keys():
            if word in verbs[key]:
                verb = key
                
    if word in nouns:
        noun = word
        
if noun and verb:
    print(f"You {verb} the {noun}.")
elif not noun and verb:
    print(f"What are you trying to {verb}?")
elif not verb and noun:
    print(f"I don't understand what you are trying to do with the {noun}.")
else:
    print("I don't know what you are saying.")