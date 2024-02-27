import datetime

def convert_date(input_date):
    # Split the input date into day, month, and year
    day, month, year = input_date.split('.')

    # Map month abbreviations to numeric values
    # Create a datetime object
    print(type(day), type(month), type(year))
    formatted_date = datetime.datetime(int(year), int(month), int(day))

    # Format the datetime as YYYY-MM-DD
    formatted_string = formatted_date.strftime('%Y-%m-%d')
    return formatted_string

# Example usage
input_date = "5.5.2089"
print(convert_date(input_date))