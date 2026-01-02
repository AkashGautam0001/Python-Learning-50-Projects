name = input("Name : ").strip()
profession = input("Profession : ").strip()
goal = input("Goal : ").strip()
favorite_emoji = input("favorite_emoji : ").strip()
website = input("website : ").strip()

def add_style(style_no):
    match style_no:
        case "1":
            return (f"""\n
                {favorite_emoji} {name} | {profession}
                💡{goal}
                🔗{website}""")
        case "2":
            return (f"""\n
                {favorite_emoji} {name} | {profession}
                💡{goal}
                🔗{website}""")
        case _:
            return (f"""\n
                {favorite_emoji} {name} | {profession}
                💡 {goal}
                🔗 {website}""")

no = input("Which Style you want to print 1, 2 ")
design_bio = add_style(no)

print(design_bio)
want_to_save = input("Are you want to save ? yes/no ?").lower().strip()

if(want_to_save == "yes"):
    file_name = input("Enter file name : ").lower().strip().replace(" ", "_")
    with open(f'{file_name}_bio.txt', "w", encoding="utf-8") as file:
        file.write(design_bio)
else:
    print("Thanks You")