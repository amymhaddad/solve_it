from collections import namedtuple, defaultdict, OrderedDict
import operator


class FullTable(Exception):
    pass


class GuestList:
    max_people_at_table = 10

    def __init__(self):
        self.table_and_guests = defaultdict(list)
        self.unassigned_guests = []

    def assign(self, person, table_number):

        if self._valid_table(person, table_number):

            for number, guests in self.table_and_guests.items():
                if person in guests:
                    guests.remove(person)
                    break
            self.table_and_guests[table_number].append(person)

    def _valid_table(self, person, table_number):

        if not table_number:
            self.unassigned_guests.append(person)
            return False

        if len(self.table_and_guests[table_number]) >= GuestList.max_people_at_table:
            raise FullTable("No more room at this table")

        return True

    def free_space(self):
        return {
            table_count: GuestList.max_people_at_table - len(guests)
            for table_count, guests in self.table_and_guests.items()
        }

    def __len__(self):
        return sum([len(guests) for guests in self.table_and_guests.values()])

    def table(self, number):
        return self.table_and_guests[number]

    def unassigned(self):
        return self.unassigned_guests

    def guests(self):
        for unassigned_guest in self.unassigned_guests:
            self.table_and_guests[0].append(unassigned_guest)

        output = ""
        for table, guests in sorted(self.table_and_guests.items()):
            output += f"{table}\n"
            for guest in sorted(guests, key=operator.itemgetter(1, 0)):
                guest_name = f"\t{guest.last} {guest.first}\n"
                output += guest_name
        return output


Person = namedtuple("Person", ["first", "last"])
gl = GuestList()

gl.assign(Person("Waylon", "Dalton"), 1)
gl.assign(Person("Justine", "Henderson"), 1)
gl.assign(Person("Abdullah", "Lang"), 3)
gl.assign(Person("Marcus", "Cruz"), 1)
gl.assign(Person("Thalia", "Cobb"), 2)
gl.assign(Person("Mathias", "Little"), 2)
gl.assign(Person("Eddie", "Randolph"), None)
gl.assign(Person("Angela", "Walker"), 2)
gl.assign(Person("Lia", "Shelton"), 3)
gl.assign(Person("Hadassah", "Hartman"), None)
gl.assign(Person("Joanna", "Shaffer"), 3)
gl.assign(Person("Jonathon", "Sheppard"), 2)
