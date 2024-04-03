
note_degree = {'C':0, "D":1, "E":2, "F":3, "G":4, "A":5, "B":6 }
note_degree_reversed = {value: key for key, value in note_degree.items()}
music_notes_natural = {"C":0, "D":2,"E":4,"F":5,"G":7,"A":9,"B":11}
music_notes_sharp = {"C#":1, "D#":3,"E#":5,"F#":6,"G#":8,"A#":10,"B#":0}
music_notes_flat = {"Cb":11, "Db":1,"Eb":3,"Fb":4,"Gb":6,"Ab":8,"Bb":10}

music_notes_natural_reversed = {value: key for key, value in music_notes_natural.items()}
music_notes_sharp_reversed = {value: key for key, value in music_notes_sharp.items()}
music_notes_flat_reversed = {value: key for key, value in music_notes_flat.items()}

major_intervals = {"P1":0,"M2":2,"M3":4, "P4":5,"P5":7, "M6":9, "M7":11,"P8":12}
minor_intervals = {"P1":0,"m2":1,"m3":3, "P4":5,"P5":7, "m6":8, "m7":10,"P8":12}
augmented_intervals = {"A1":1,"A2":3,"A3":5, "A4":6,"A5":8, "A6":10, "A7":12,"A8":13}
diminished_intervals = {"D1":11,"D2":0,"D3":2, "D4":4,"D5":6, "D6":7, "D7":9,"D8":11}

note = "none"
while(note !="q" and note !="Q" ):
    try:
        note, interval = input("Please Enter the Note!\n").split()
    except ValueError:
        note = "q"
        break
    note_number  = -1
    try:
        if(note_number<0): note_number = music_notes_flat[note]
    except KeyError:
        if(note_number<0):note_number  = -1
    try:
        if(note_number<0): note_number = music_notes_natural[note]
    except KeyError:
        if(note_number<0):note_number  = -1
    try:
        if(note_number<0): note_number = music_notes_sharp[note]
    except KeyError:
        print("Note Does Not Exist")
        continue


    interval_number = -1
    try:
        if(interval_number<0): interval_number = major_intervals[interval]
    except KeyError:
        if(interval_number<0): interval_number = -1
    try:
        if(interval_number<0): interval_number = minor_intervals[interval]
    except KeyError:
        if(interval_number<0): interval_number = -1
    try:
        if(interval_number<0): interval_number = augmented_intervals[interval]
    except KeyError:
        if(interval_number<0): interval_number = -1
    try:
        if(interval_number<0): interval_number = diminished_intervals[interval]
    except KeyError:
        print("Interval does not exist")
        continue
    target_note = note_number+interval_number
    if(target_note>=12): target_note = target_note-12

    possible_solutions = []
    try:
        possible_solutions.append(music_notes_flat_reversed[target_note])
    except KeyError:
        print(" ")
    try:
        possible_solutions.append(music_notes_natural_reversed[target_note])
    except KeyError:
        print(" ")
    try:
        possible_solutions.append(music_notes_sharp_reversed[target_note])
    except KeyError:
        print(' ')
    print("Possible Solutions", possible_solutions)
    expected_note_index = note_degree[note[0]] + int(interval[1])-1
    if( expected_note_index > 6):
        expected_note_index = expected_note_index - 7
    expected_note = note_degree_reversed[expected_note_index]
    print("Expected note", expected_note)
    expected_solution = ''
    for solution in possible_solutions:

        if solution[0] == expected_note:
            expected_solution = solution
    print("Expected Solution", expected_solution)
    