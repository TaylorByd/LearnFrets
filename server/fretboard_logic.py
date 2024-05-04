def rotateNoteArray(arr, note):
    if note == arr[0]:
        return arr
    note_index = 0
    for i in range(13):
        if arr[i] == note:
            note_index = i
    sub_array_1 = arr[note_index:]
    sub_array_2 = arr[1:note_index]
    sub_array_2.append(note)
    return sub_array_1 + sub_array_2

def setTune(fretboard, tunearray):
    for i in range(6):
        tunenote = tunearray[i]
        subarr_fretboard = fretboard[i][:]
        fretboard[i][:] = rotateNoteArray(subarr_fretboard, tunenote)
    return fretboard

default_notes = ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#',
         'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E']
fretboard = [['0']*25 for i in range(6)]

tunearr = ['E', 'A', 'D', 'G', 'B', 'E']

for i in range(6):
    for j in range(25):
        fretboard[i][j] = default_notes[j]

print(setTune(fretboard, tunearr))