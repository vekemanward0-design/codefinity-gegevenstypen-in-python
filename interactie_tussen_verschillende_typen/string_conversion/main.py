age_str = "19"
has_id_str = " Yes "
ticket_code = "VIP-023-A"
is_member = False
adult_age = 18
max_seat_number = 150

# 1) Age as int
age = int(age_str.strip())

# 2) ID possession as Boolean from text
has_id = has_id_str.strip().casefold() == "yes"

# 3) Parse ticket parts by fixed positions
tier = ticket_code[:3]             # "VIP"
seat_number_str = ticket_code[4:7] # "023"
zone = ticket_code[-1]             # "A"

# 4) Seat number as int
seat_number = int(seat_number_str)

# 5) Rules
is_adult = age >= adult_age
can_enter = has_id and is_adult
vip_perk = tier == "VIP"
member_fastlane = is_member and can_enter
seat_ok = 1 <= seat_number <= max_seat_number
entry_granted = can_enter and seat_ok

# 6) Summary line
summary = f"{tier}-{seat_number_str}-{zone} | age={age} | enter={entry_granted} | vip={vip_perk} | fastlane={member_fastlane}"

print(age, has_id, tier, seat_number_str, zone, seat_number, is_adult, can_enter, vip_perk, member_fastlane, seat_ok, entry_granted, sep=" | ")
print(summary)