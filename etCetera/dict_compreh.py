name_list= ["Student1","Student2","Student2"]
nbrs = ["079999999","07888888","07839283938"]
new_dict = {stud: f"{nbr}" for stud in name_list for nbr in nbrs}

print(new_dict)