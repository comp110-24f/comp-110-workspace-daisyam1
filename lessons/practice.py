def find_eligible(names: list[str], ages: list[int]) -> dict[str, int]:
    if len(names) != len(ages):
        raise ValueError("Diff lengths.")
    eligible_ppl: dict[str, int] = {}
    for idx in range(0, len(names)):
        if ages[idx] >= 25:
            eligible_ppl[names[idx]] = ages[idx]
    return eligible_ppl


names = ["Allan", "Ken", "Barbie"]
ages = [23, 26, 25]
renters: dict[str, int] = find_eligible(names, ages)
print(renters)

if "Ken" in renters:
    renters.pop("Ken")

print(renters)
