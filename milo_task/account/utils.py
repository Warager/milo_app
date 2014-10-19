from datetime import date


def get_eligible(born):
    if not born:
        return 'blocked'
    today = date.today()
    age = today.year - born.year - ((today.month, today.day) < (
                                    born.month, born.day))
    if age > 13:
        return 'allowed'
    else:
        return 'blocked'


def get_bizzfuzz(random):
    if random % 3 == 0 and random % 5 == 0:
        return 'BizzFuzz'
    if random % 3 == 0:
        return 'Bizz'
    if random % 5 == 0:
        return 'Fuzz'
    else:
        return random