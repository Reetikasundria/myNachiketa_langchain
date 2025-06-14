def is_safe(prompt):
    bad_keywords = ["blood", "violence", "gun", "naked", "kill", "weapon", "war"]
    return not any(word in prompt.lower() for word in bad_keywords)
