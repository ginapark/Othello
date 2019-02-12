    
def add_to_file(name, score, file_path = "scores.txt"):
    """Adds the name and score of the player into the 
    scores file."""
    added = False
    score = int(score)
    file = open(file_path, 'r')
    line_list = file.readlines()
    file = open(file_path, 'w')

    if not line_list:
        file.write(name + " " + str(score) + "\n")

    else:
        for line in  line_list:
            line = line.strip("\n")
            curr = line.split(" ")
            curr_score = int(curr[1])
            if score > curr_score and not added:
                file.write(name + " " + str(score)+ "\n")
                file.write(line + "\n")
                added = True
            else:
                file.write(line + "\n")
        if not added:
            file.write(name + " " + str(score)+ "\n")
    file.close()      
    
add_to_file("Player1", 3)
add_to_file("Player2", 5)
add_to_file("Player3", 2)