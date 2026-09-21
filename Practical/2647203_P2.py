import Module_2647203_P2 as mod

# Operational Dataset
sites = {
    "SITE_1": {
        "location": "Substation North",
        "capacity_kw": 150.0,
        "soc": 75.0,
        "temp": 32.0,
        "readings": [40.0, 55.0, 65.0]
    },
    "SITE_2": {
        "location": "Substation South",
        "capacity_kw": 90.0,
        "soc": 25.0,
        "temp": 48.0,
        "readings": [20.0, 30.0, 25.0]
    },
    "SITE_3": {
        "info": ("Substation East", 200.0),
        "location": "Substation East",
        "capacity_kw": 200.0,
        "soc": 85.0,
        "temp": 28.0,
        "readings": [80.0, 95.0, 110.0]
    }
}


# Print All the Added Sites
def view_all_sites():
    mod.print_title("ALL REGISTERED MICROGRID SITES")
    for s_id, d in sites.items():
        avg_kw = mod.cal_average(d["readings"])
        peak_kw = mod.get_peak(d["readings"])
        is_safe, thermal_status = mod.check_thermal_status(d["temp"])

        print(f"[{s_id}] Location: {d['location']} | Rated Capacity: {d['capacity_kw']} kW")
        print(f"\t Battery SoC: {mod.format_decimal(d['soc'])}% | Cell Temp: {mod.format_decimal(d['temp'])}°C [{thermal_status}]")
        print(f"\t Power Readings (kW): {d['readings']}")
        print(f"\t Average Power: {avg_kw} kW | Peak Recorded: {peak_kw} kW")
        mod.print_divider()


# Add new reading for a Site
def add_power_reading():
    mod.print_title("LOG REAL-TIME POWER READING")
    s_id = input("Enter Site ID: ").strip().upper()
    site = mod.search_site(sites, s_id)

    if not site:
        print("Error: Site ID does not exist.")
        return

    val_str = input("Enter current generated power in kW (0 to 500): ").strip()
    
    # Using module validation utilities
    if not mod.check_num(val_str):
        print("Validation Error: Input must be a valid number.")
        return

    val = float(val_str)
    if not mod.check_range(val, 0.0, 500.0):
        print("Validation Error: Reading must be between 0.0 and 500.0 kW.")
        return

    # Check performance ratio before saving
    pr = mod.cal_pr(val, site["capacity_kw"])
    print(f"Calculated Performance Ratio (PR): {pr}%")

    if mod.confirm_action("Confirm logging this reading?"):
        mod.add_reading(site["readings"], val)
        print(f"Success: Appended {mod.format_decimal(val)} kW to {s_id}.")
    else:
        print("Action cancelled.")


# Searching a Site
def search_site_record():
    mod.print_title("SEARCH SITE DETAILS")
    s_id = input("Enter Site ID: ").strip().upper()
    site = mod.search_site(sites, s_id)

    if site:
        avg_kw = mod.cal_average(site["readings"])
        peak_kw = mod.get_peak(site["readings"])
        is_safe, thermal_status = mod.check_thermal_status(site["temp"])

        print("\n")
        print(f"Site ID : {s_id}")
        print(f"Location : {site['location']}")
        print(f"Rated Capacity : {site['capacity_kw']} kW")
        print(f"Battery SoC : {mod.format_decimal(site['soc'])}%")
        print(f"Cell Temp : {mod.format_decimal(site['temp'])}°C ({thermal_status})")
        print(f"Power Log (kW) : {site['readings']}")
        print(f"Average Power : {avg_kw} kW")
        print(f"Peak Power : {peak_kw} kW")
    else:
        print("Error: Site record not found.")



def simulate_dispatch():
    mod.print_title("System Operation & Energy Analysis")
    s_id = input("Enter Site ID: ").strip().upper()
    site = mod.search_site(sites, s_id)

    if not site:
        print("Error: Site record not found.")
        return

    sol_str = input("Enter current Solar Generation (kW): ").strip()
    load_str = input("Enter current Grid Load Demand (kW): ").strip()

    if not (mod.check_num(sol_str) and mod.check_num(load_str)):
        print("Validation Error: Both solar and load inputs must be numbers.")
        return

    sol = float(sol_str)
    load = float(load_str)

    # Calculate net balance using module function
    net, status = mod.calculate_balance(sol, load)
    pr = mod.cal_pr(sol, site["capacity_kw"])

    print(f"\nOperational Status : {status}")
    print(f"Net Power Flow     : {mod.format_decimal(net)} kW")
    print(f"Asset Efficiency   : {pr}% PR")

    # Warn if battery cell temperature is high
    is_safe, thermal_status = mod.check_thermal_status(site["temp"])
    if not is_safe:
        print(f"[ALERT]: Unit core temperature is high ({site['temp']}°C)! Dispatch with caution.")


while True:
    mod.print_title("SOLAR-BESS OPERATIONS CONSOLE")
    print("1. View All Sites & Thermal Diagnostics")
    print("2. Log Power Reading & Performance Ratio")
    print("3. Search Site Record by ID")
    print("4. System Operation & Energy Analysis")
    print("5. Exit")

    choice = input("\nEnter choice (1-5): ").strip()

    if choice == "1":
        view_all_sites()
    elif choice == "2":
        add_power_reading()
    elif choice == "3":
        search_site_record()
    elif choice == "4":
        simulate_dispatch()
    elif choice == "5":
        print("Terminating console application.")
        break
    else:
        print("Invalid selection. Please choose 1 to 5.")
