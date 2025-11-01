import pprint
from dataclasses import dataclass

val=['one','two','three','four','five']
# print(*val)

# print(*val,sep=' -- ')

# for i in range (0,len(val)):
#     print(val[i], end=f" [Line: {str(i+1)}]\n")


# r"""Output:


# PS C:\Users\Ayush Kumar Gupta\Desktop\Advance Python> & "C:/Users/Ayush Kumar Gupta/AppData/Local/Programs/Python/Python314/python.exe" "c:/Users/Ayush Kumar Gupta/Desktop/Advance Python/pprint.py"
# one two three four five
# one -- two -- three -- four -- five
# one [Line: 1]
# two [Line: 2]
# three [Line: 3]
# four [Line: 4]
# five [Line: 5]
# """
# nf=open("output.txt","w")
# print(*val,sep=" -- ",file=nf,flush=True)

worldcup_data = {
    "current_champion": {
        "year": 2022,
        "winner": "Argentina 🇦🇷",
        "runner_up": "France 🇫🇷",
        "host_country": "Qatar 🇶🇦",
        "final_score": "3-3 (4-2 on penalties)",
        "golden_boot": "Kylian Mbappé (8 goals)",
        "teams_participating": 32
    },
    "next_tournament": {
        "year": 2026,
        "host_countries": ["United States 🇺🇸", "Canada 🇨🇦", "Mexico 🇲🇽"],
        "dates": "June 11 – July 19, 2026",
        "teams_participating": 48, # Expanded from 32
        "total_matches": 104,
        "key_venues": {
            "Opening Match": "Estadio Azteca, Mexico City",
            "Final Match": "MetLife Stadium, New York/New Jersey"
        }
    },
    "historical_data": {
        "most_titles": "Brazil (5)",
        "continental_titles": {
            "Europe": 12,
            "South America": 10
        }
    }
}

# Example of how to access the data
print(f"The host countries for the next World Cup in {worldcup_data['next_tournament']['year']} are: {', '.join(worldcup_data['next_tournament']['host_countries'])}")

print(f"The reigning champion from {worldcup_data['current_champion']['year']} is {worldcup_data['current_champion']['winner']}.")



pprint.pprint(worldcup_data)
exit()