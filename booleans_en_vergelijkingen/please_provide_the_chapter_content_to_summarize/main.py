age = 17
adult_age = 21
has_id = True
is_member = False

purchase_total = 120.0
free_shipping_threshold = 100.0

email_verified = True
phone_verified = False

score = 74
min_score = 0
max_score = 100

# 1) Adult check
is_adult = age >= adult_age

# 2) Entry rule
can_enter = is_adult and has_id

# 3) Free shipping rule
qualifies_free_shipping = (purchase_total >= free_shipping_threshold) or is_member

# 4) Manual review rule
needs_manual_review = (not email_verified) or (not phone_verified)

# 5) Score range rule
valid_score_range = min_score <= score <= max_score

print(is_adult, can_enter, qualifies_free_shipping, needs_manual_review, valid_score_range)