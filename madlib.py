def madlib():
    person1 = input("Person in room:")
    adjective = input("Adjective (describes a noun. e.g. small, large, square):")
    verb1 = input("Verb (action):")
    body_part = input("Body part:")
    number = input("Number:")
    noun = input("Noun (person, place, or thing):")
    adverb = input("Adverb (e.g., gently, quite, then, there):")
    verb2 = input("Verb (action):")
    plural_prounoun = input("Plural pronoun (e.g. they):")
    person2 = input("Other person in the room:")

    print("Dear {}\n".format(person1))
    print("You are extremly {} and I {} you!".format(adjective,verb1))
    print("I want to kiss your {} {} times.".format(body_part,number))
    print("You make my {} burn with desire.".format(noun))
    print("When I first saw you, I {} stared at you and fell in love. \nWill you {} out with me? Don`t let your parents discourage you, {} are just jealous.".format(adverb,verb2,plural_prounoun))
    print("\nYours forever, {}".format(person2))
    return


madlib()