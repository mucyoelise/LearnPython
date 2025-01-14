def total(galleons,sickles, knuts):
    return (galleons*17 + sickles)*29+knuts

# You need to create dict keys with the same name as the funct argument
coins_dict = {"galleons": 100, "sickles": 50, "knuts": 25}

coins_list = [100,50,25]
# Unpacking list values
print("List unpacking:",total(*coins_list))

# Unpacking dict values
# When you unpack dictionary seems like this: total(galleons=100, sickles=50, knuts=25)
print("Dictionary unpacking:",total(**coins_dict))
