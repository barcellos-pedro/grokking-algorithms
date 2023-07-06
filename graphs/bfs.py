def breadth_first_search(graph, start, target):
    people = graph[start]
    checked = []

    while people:
        person = people.pop(0)

        if person in checked:
            continue

        if target in person:
            return f"Person {person} matches the search = {target}"

        if person in graph:
            people += graph[person]

        checked.append(person)

    return None


# here james is the central vertex

graph = {
    "james": ["bob", "claire", "alice"],
    "bob": ["anuj (sales)", "mike"],
    "mike": ["peggie"],
    "alice": ["peggie"],
    "claire": ["thom", "jonny"]
}

result = breadth_first_search(
    graph,
    start="james",
    target="sales"
)

print(result)
