full_name = "  Ada Lovelace  "
sentence = "The (quick) brown-fox jumps over 13 lazy dogs!"
email = "  Support@Example.COM \n"
SEP = " | "

# 1) Trim spaces
name_clean = full_name.strip()

# 2) Check "quick" (case-insensitive)
has_quick = "quick" in sentence.lower()

# 3) Text inside parentheses
start = sentence.find("(")
end = sentence.find(")")
inside_parens = sentence[start + 1 : end]

# 4) Count 'o' (case-insensitive)
o_count = sentence.lower().count("o")

# 5) Domain after '@'
email_clean = email.strip().lower()
at_pos = email_clean.find("@")
domain = email_clean[at_pos + 1 :]

# 6) Summary string
report = f"{name_clean}{SEP}{domain}{SEP}{o_count}"

print(name_clean, has_quick, inside_parens, o_count, domain)
print(report)