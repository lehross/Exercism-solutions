def recite(start_verse, end_verse):
    lyrics = []

    for i in range(start_verse - 1, end_verse):
        lyrics.append(f"On the {verses[i][0]} day of Christmas my true love gave to me: {''.join([verses[j][1] for j in range(i, -1, -1)])}")
    
    return lyrics

verses = [["first", "a Partridge in a Pear Tree."],
["second", "two Turtle Doves, and "],
["third", "three French Hens, "],
["fourth", "four Calling Birds, "],
["fifth", "five Gold Rings, "],
["sixth", "six Geese-a-Laying, "],
["seventh", "seven Swans-a-Swimming, "], 
["eighth", "eight Maids-a-Milking, "], 
["ninth", "nine Ladies Dancing, "], 
["tenth", "ten Lords-a-Leaping, "], 
["eleventh", "eleven Pipers Piping, "], 
["twelfth", "twelve Drummers Drumming, "]]
