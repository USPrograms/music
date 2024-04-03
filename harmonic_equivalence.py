def reverse(intervals):
    reversed_intervals = {}
    for key, value in intervals.items():
        reversed_intervals[value] = key
    return reversed_intervals

note_degree = {'C':0, "D":1, "E":2, "F":3, "G":4, "A":5, "B":6 }
note_degree_reversed = reverse(note_degree)
music_notes_natural = {"C":0, "D":2,"E":4,"F":5,"G":7,"A":9,"B":11}
music_notes_sharp = {"C#":1, "D#":3,"E#":5,"F#":6,"G#":8,"A#":10,"B#":0}
music_notes_flat = {"Cb":11, "Db":1,"Eb":3,"Fb":4,"Gb":6,"Ab":8,"Bb":10}

music_notes_natural_reversed = reverse(music_notes_natural)
music_notes_sharp_reversed = reverse(music_notes_sharp)
music_notes_flat_reversed = reverse(music_notes_flat)

major_intervals = {"P1":0,"M2":2,"M3":4, "P4":5,"P5":7, "M6":9, "M7":11,"P8":12}
minor_intervals = {"P1":0,"m2":1,"m3":3, "P4":5,"P5":7, "m6":8, "m7":10,"P8":12}
augmented_intervals = {"A1":1,"A2":3,"A3":5, "A4":6,"A5":8, "A6":10, "A7":12,"A8":13}
diminished_intervals = {"D1":11,"D2":0,"D3":2, "D4":4,"D5":6, "D6":7, "D7":9,"D8":11}


reversed_major_intervals = reverse(major_intervals)
reversed_minor_intervals = reverse(minor_intervals)
reversed_augmented_intervals = reverse(augmented_intervals)
reversed_diminished_intervals = reverse(diminished_intervals)

input_value = "none"
while(input_value !="q" and input_value !="Q" ):
    try:
        input_value, note_or_interval = input("Please Enter the Note!\n").split()
    except ValueError:
        input_value = "q"
        break
    if note_or_interval == "N":
        note = input_value
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
        target_note = note
        if(target_note>=12): target_note = target_note-12

        possible_solutions = []
        try:
            possible_solutions.append(music_notes_flat_reversed[target_note])
        except KeyError:
            pass
        try:
            possible_solutions.append(music_notes_natural_reversed[target_note])
        except KeyError:
            pass
        try:
            possible_solutions.append(music_notes_sharp_reversed[target_note])
        except KeyError:
            pass
        print("Harmonically Equivalent Notes", possible_solutions)

    if note_or_interval == "I":
        interval = input_value
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
        harmonically_equivalent = []
        try:
            harmonically_equivalent.append(reversed_major_intervals[interval_number])
        except KeyError:
            pass        
        try:
            harmonically_equivalent.append(reversed_minor_intervals[interval_number])
        except KeyError:
            pass
        try:
            harmonically_equivalent.append(reversed_augmented_intervals[interval_number])
        except KeyError:
            pass
        try:
            harmonically_equivalent.append(reversed_diminished_intervals[interval_number])
        except KeyError:
            pass        
        print("Harmonically Equivalent Intervals ", harmonically_equivalent)