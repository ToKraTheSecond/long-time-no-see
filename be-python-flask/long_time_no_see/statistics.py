def summarize(records: list)-> dict:
    total_meetings = len(records)
    unique_people = list(set(record.person for record in records))
    return {
        'total_meetings': total_meetings,
        'unique_people_met': unique_people
    }
