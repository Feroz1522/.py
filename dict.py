dict_lb = {
    "idk": "i don't know",
    "omw": "on my way",
    "os" :"operating system",
    "foss" :"free and open source software"
}
print(dict_lb["idk"])
print(dict_lb.get("foss"))


arts_groups = {
    "bca":"bachelor of computer application",
    "bcom":"bachelor of commerce",
    "bba":"bachelor of business administration"
}
print(arts_groups["bba"])
print(arts_groups.get("bca"))