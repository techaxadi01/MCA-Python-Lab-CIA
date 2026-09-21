'''
 # Reusable Domain-Independent Utility Modules
'''


# Prints a Title Banner in between '='
def print_title(msg):
    print("\n" + "=" * 45)
    print(msg)
    print("=" * 45)


# Prints a simple line divider
def print_divider():
    print("-" * 45)


# Checks if a string is non-empty
def check_empty(text):
    return text.strip() != ""


# Formates the Float with 2 Decimal places
def format_decimal(val):
    return f"{float(val):.2f}"


# Check if the string enter is a no or not
def check_num(val_str):
    return val_str.strip().replace(".", "", 1).isdigit()


# Takes confirmation before Prociding
def confirm_action(prompt_text):
    ans = input(f"{prompt_text} (y/n): ").strip().lower()
    return ans == "y"


# Checks if the Value is in the reange or not
def check_range(val, min_val, max_val):
    return min_val <= val <= max_val



'''
 # Reusable Domain-Based Modules
'''


# Add power reading to the History List
def add_reading(readings_list, new_kw):
    readings_list.append(round(new_kw, 2))


# Calculate Average Readings for the Site
def cal_average(readings_list):
    if len(readings_list) == 0:
        return 0.0
    return round(sum(readings_list) / len(readings_list), 2)


# Find Highest (peak) Reading
def get_peak(readings_list):
    if len(readings_list) == 0:
        return 0.0
    return max(readings_list)


# Search site using ID
def search_site(sites_dict, site_id):
    return sites_dict.get(site_id.strip().upper())


# Calculate net power surplus or deficit
def calculate_balance(solar_kw, load_kw):
    net = solar_kw - load_kw
    if net > 0:
        status = "SURPLUS"
    elif net < 0:
        status = "DEFICIT"
    else:
        status = "BALANCED"
    return round(net, 2), status


# Check if battery temperature is within safe limits
def check_thermal_status(temp_c, max_limit=45.0):
    if temp_c > max_limit:
        return False, "OVERHEAT_WARNING"
    return True, "TEMP_NORMAL"


# Calculate solar performance ratio (PR)
def cal_pr(actual_kw, rated_capacity_kw):
    # Computes system efficiency ratio: (Actual Power / Rated Capacity) * 100.
    if rated_capacity_kw <= 0:
        return 0.0
    pr = (actual_kw / rated_capacity_kw) * 100
    if pr > 100.0:
        pr = 100.0
    return round(pr, 2)
