import re

def number_unique_emails(emails):
    all_unique_emails = set()

    for email in emails:
        split_email = email.split("@")

        local_name = split_email[0]
        local_name_without_dots = re.sub("\.", "", local_name)

        if "+" in local_name_without_dots:
            parsed_localname = local_name_without_dots[
                : local_name_without_dots.index("+")
            ]
        else:
            parsed_localname = local_name_without_dots

        parsed_email = parsed_localname + "@" + split_email[1]
        all_unique_emails.add(parsed_email)

    return len(all_unique_emails)
