# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

#Remove two below lines later
#print(lower_case_name1)
#print(lower_case_name2)
print("")
true = 0
# print(true)
# Begin "TRUE" section

# Count for T in both names
true_t_count = lower_case_name1.count("t") + lower_case_name2.count("t")
if true_t_count < 2 and true_t_count > 0:
  print(f"T occurs {true_t_count} time")
else:
  print(f"T occurs {true_t_count} times")

true = true + true_t_count

# Count for R in both names
true_r_count = lower_case_name1.count("r") + lower_case_name2.count("r")
if true_r_count < 2 and true_r_count > 0:
  print(f"R occurs {true_r_count} time")
else:
  print(f"R occurs {true_r_count} times")

true = true + true_r_count

# Count for U in both names
true_u_count = lower_case_name1.count("u") + lower_case_name2.count("u")
if true_u_count < 2 and true_u_count > 0:
  print(f"U occurs {true_u_count} time")
else:
  print(f"U occurs {true_u_count} times")

true = true + true_u_count

# Count for E in both names
true_e_count = lower_case_name1.count("e") + lower_case_name2.count("e")
if true_e_count < 2 and true_e_count > 0:
  print(f"E occurs {true_e_count} time")
else:
  print(f"E occurs {true_e_count} times")

true = true + true_e_count
print(f"TRUE total = {true}")
print("")
# Begin "LOVE" section
love = 0


# Count for L in both names
love_l_count = lower_case_name1.count("l") + lower_case_name2.count("l")
if love_l_count < 2 and love_l_count > 0:
  print(f"L occurs {love_l_count} time")
else:
  print(f"L occurs {love_l_count} times")

love = love + love_l_count
#print(love)
# Count for O in both names
love_o_count = lower_case_name1.count("o") + lower_case_name2.count("o")
if love_o_count < 2 and love_o_count > 0:
  print(f"O occurs {love_o_count} time")
else:
  print(f"O occurs {love_o_count} times")

love = love + love_o_count
# Count for V in both names
love_v_count = lower_case_name1.count("v") + lower_case_name2.count("v")
if love_v_count < 2 and love_v_count > 0:
  print(f"V occurs {love_v_count} time")
else:
  print(f"V occurs {love_v_count} times")

love = love + love_v_count
# Count for E in both names
love_e_count = lower_case_name1.count("e") + lower_case_name2.count("e")
if love_e_count < 2 and love_e_count > 0:
  print(f"E occurs {love_e_count} time")
else:
  print(f"E occurs {love_e_count} times")

love = love + love_e_count
print(f"LOVE total = {love}")

print("")

total = true + love
print(f"Your total is: {total}")
