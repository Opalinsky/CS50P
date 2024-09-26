# def main():
#     spacecraft = {"name": "Voyager 1", "distance": 163}
#     print(create_report(spacecraft))

# def create_report(spacecraft):
#     return f"""
#     ========== REPORT ==========

#     Name: {spacecraft["name"]}
#     Distance: {spacecraft["distance"]} AU

#     ========== REPORT ==========
#     """
# main()
# def main():
#     spacecraft = {"name": "Voyager 1",}
#     spacecraft["distance"] = 0.01
#     #possibility to add some key with value later
#     print(create_report(spacecraft))

# def create_report(spacecraft):
#     return f"""
#     ========== REPORT ==========

#     Name: {spacecraft["name"]}
#     Distance: {spacecraft["distance"]} AU

#     ========== REPORT ==========
#     """
# main()
def main():
    spacecraft = {"name": "Voyager 1"}
    print(create_report(spacecraft))

#if no value Unknown:
def create_report(spacecraft):
    return f"""
    ========== REPORT ==========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU

    ========== REPORT ==========
    """
main()


#metod update to add multiple values
#spacecraft.update({"distance": 0.01, "orbit": "Sun"})

