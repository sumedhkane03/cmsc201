"""
File:    minor_key.py
Author:  Sumedh Kane
Date:    10/22/2021
Section: 16
E-mail:  sumedhk1@umbc.edu
Description:
  Takes user input of any note and outputs the minor harmonic scale of that note.
"""
#[1 Step] [½ Step] [1 Step] [1 Step] [½ Step] [1½ Step] [½ Step]
#   2       1         2       2        1         3         1
if __name__ == '__main__':

    MUSICAL_NOTES = ['C', 'D\u266d', 'D', 'E\u266d', 'E', 'F', 'G\u266d', 'G', 'A\u266d', 'A', 'B\u266d', 'B']

    A_FLAT = ['A\u266d','B\u266d','B','D\u266d','E\u266d','E','G','A\u266d']

    B_FLAT = ['B\u266d','C','D', 'E','G\u266d','G']
    starting_note = ' '
    while starting_note.lower() != 'quit':

        starting_note = str(input("Enter the starting note (A, A flat) or enter 'quit' to quit: "))
        def first_note(starting_note):
            count = 0
            starting_note = starting_note.upper()
            starting_note = starting_note.split(sep=' ')
            for i in range(len(starting_note)):
                if starting_note[i] == 'FLAT':
                    starting_note.remove(starting_note[i])
                    starting_note.append('\u266d')
                    note = starting_note[0].upper() + starting_note[1]
                else:
                    note = starting_note
            return(note)

        def scale_generator(first_note):
            final_scale = []
            if first_note not in MUSICAL_NOTES:
                if len(first_note) > 1:
                    eeeeee = first_note[0] + first_note[1]
                else:
                    eeeeee = first_note[0]
                return eeeeee, 'is not a valid starting note.'


            if len(first_note)==1:
                if first_note[0] in MUSICAL_NOTES:
                    cur_note = 0
                    count = 0
                    while count < 8:
                        if count == 0:
                            cur_note = MUSICAL_NOTES.index(first_note[0])

                        if cur_note >= len(MUSICAL_NOTES):
                            cur_note = 0
                        if count == 0 or count == 2 or count == 3:
                            final_scale.append(MUSICAL_NOTES[cur_note])
                            cur_note+=2
                            count+=1
                        elif count == 1 or count == 4 or count == 6:
                            final_scale.append(MUSICAL_NOTES[cur_note])
                            cur_note+=1
                            count+=1
                        elif count == 5:
                            final_scale.append(MUSICAL_NOTES[cur_note])
                            cur_note+=3
                            count+=1
                        else:
                            final_scale.append(first_note[0])
                            count+=1
            else:
                if first_note in MUSICAL_NOTES:
                    cur_note = 0
                    count = 0
                    while count < 8:
                        if count == 0:
                            cur_note = MUSICAL_NOTES.index(first_note)

                        if cur_note >= len(MUSICAL_NOTES):
                            cur_note = 0
                        if count == 0 or count == 2 or count == 3:
                            final_scale.append(MUSICAL_NOTES[cur_note])
                            cur_note += 2
                            count += 1
                        elif count == 1 or count == 4 or count == 6:
                            final_scale.append(MUSICAL_NOTES[cur_note])
                            cur_note += 1
                            count += 1
                        elif count == 5:
                            final_scale.append(MUSICAL_NOTES[cur_note])
                            cur_note += 3
                            count += 1
                        else:
                            final_scale.append(first_note)
                            count += 1


            print(*final_scale,sep=' ')


        scale_generator(first_note(starting_note))

