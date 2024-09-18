# Write a function that receives as a parameters a list of musical notes (strings),
# a list of moves (integers) and a start position (integer). The function will return the song composed by
# going though the musical notes beginning with the start position and following the moves given as parameter.
# 	Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"]
#                       0      1     2     3    4

def compose(notes, moves, start) :
    song = list()
    song.append(notes[start])
    current_position = start

    for move in moves :
        current_position =  (current_position + move ) % len(notes)
        song.append(notes[current_position])

    print("The new song is: %s" % song)


if __name__ == "__main__" :
    notes = list(input("Enter a list of musical notes separated by space: ").split())
    number_of_notes = len(notes)
    moves = list(map(int, input("Enter a list of moves (you need to introduced %d  numbers): " % (number_of_notes-1)).split()))
    start = int(input("Enter a start position to compose a song: "))

    compose(notes, moves, start)