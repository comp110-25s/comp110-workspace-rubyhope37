"""Examples of set and dictionary syntax."""

print("HI")
ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}
if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("No orders of mint")

for flavor in ice_cream:
    print(
        "BKSDFB"
    )  # where flavor is the name of the key value in the dictionary named ice_cream
