#postprocess summarize results
detect_without_mask = 0;
detect_with_mask = 0;

dom_races = [];
dom_races_num_changed = [];
dom_races_num_changed_null = [];
dom_race_num_same = [];

dom_race_change_strs = [];
dom_race_change_unique = [];
asian_to_white = [];

race_dominant_list = open('race_dominant_out.txt', 'r').readlines();
race_dominant_masked_list = open('race_dominant_masked_out.txt', 'r').readlines();
for i in range(0, len(race_dominant_list)):
    if (race_dominant_list[i] != "NULL\n"):
        race_dominant_list[i] = race_dominant_list[i].split("\t")[1][:-1];
    else:
        race_dominant_list[i] = "NULL";

    if (race_dominant_masked_list[i] != "NULL\n"):
        race_dominant_masked_list[i] = race_dominant_masked_list[i].split("\t")[1][:-1];
    else:
        race_dominant_masked_list[i] = "NULL";

for i in range(0, len(race_dominant_list)):

    if (race_dominant_list[i] != "NULL"):
        detect_without_mask+=1;  # num face was undetectable without mask
        if (race_dominant_list[i] not in dom_races): #if race is unique
            dom_races.append(race_dominant_list[i]); #add to list of uniques

    if (race_dominant_masked_list[i] != "NULL"):
        detect_with_mask+=1;  # num face was undetectable after adding mask

    #if face was detected with and without mask, and the race changed
    if (race_dominant_list[i] != "NULL" and race_dominant_masked_list[i] != "NULL" and race_dominant_list[i] !=  race_dominant_masked_list[i]):
        change_str = race_dominant_list[i].title() + " to " + race_dominant_masked_list[i].title();
        dom_race_change_strs.append(change_str); #record race change
        #assess asian-to-white change for presentation
        if (change_str == "Asian to White"):
            asian_to_white.append(i);
        if (change_str not in dom_race_change_unique): #if change is unique
            dom_race_change_unique.append(change_str); #add to list of uniques

num_per_change = [0] * len(dom_race_change_unique);
for i in range (0, len(dom_race_change_unique)): #look at each unique change
    num_per_change[i] = dom_race_change_strs.count(dom_race_change_unique[i]); #count number that each change occurs

race_changes_out = open("race_changes_out.txt", "w");
for i in range (0, len(dom_race_change_unique)):
    race_changes_out.write(dom_race_change_unique[i] + "\t" + str(num_per_change[i]) + "\n");

#print results to console
print(detect_without_mask);
print(detect_with_mask / detect_without_mask);
#print(num_per_change);
#print(dom_race_change_unique);
#print(dom_race_change_strs);
#print(no_detect_with_mask);



