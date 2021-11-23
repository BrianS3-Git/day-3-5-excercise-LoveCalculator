# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

#Remove two below lines later
print(lower_case_name1)
print(lower_case_name2)

true = 0
# print(true)
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
  print(f"R occurs {true_t_count} time")
else:
  print(f"R occurs {true_t_count} times")

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


print(true)
