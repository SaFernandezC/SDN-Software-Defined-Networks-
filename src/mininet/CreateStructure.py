HOSTS = [
    ('h1', '10.0.0.1', '00:00:00:00:00:01'),
    ('h2', '10.0.0.2', '00:00:00:00:00:02'),
    ('h3', '10.0.0.3', '00:00:00:00:00:03'),
    ('h4', '10.0.0.4', '00:00:00:00:00:04')
]
INITIAL_SWITCHES = ['s1', 's2']
INITIAL_LINKS = [
    ('h1', 's1'),
    ('h2', 's1'),
    ('h3', 's2'),
    ('h4', 's2')
]


def create_structure(amount):
    switches = INITIAL_SWITCHES
    links = INITIAL_LINKS
    name = 's1'

    for i in range(amount):
        before = name
        name = "s" + str(i + 3)
        switches.append(name)
        links.append((before, name))

    links.append((name, 's2'))
    return HOSTS, switches, links
