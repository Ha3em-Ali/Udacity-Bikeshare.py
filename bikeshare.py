import time
import pandas as pd
import numpy as np
import calendar
CITY_DATA = {'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bike share data!')
    # TO DO: get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('which city would you like to show its data? chicago, new york city, washington?').lower()
        if city not in CITY_DATA:
            print('please choose a city')

        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('please type the desired month from january to june or type all to show all months').lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        if month != 'all' and month not in months:
            print('please type a valid entry')
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('please enter a week day or type all to show all week days').lower()
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        if day != 'all' and day not in days:
            print('please type a valid entry')
        else:
            break
               
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
                                     
    if month != 'all':

        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)

        df = df[df['month'] == month]
                                     
    if day != 'all':
                                     
        df = df[df['day_of_week'] == day.title()]

    return df


def display_raw_data(df):

    i = 0
    answer = input('do you want to display first 5 rows? yes or no:').lower()
    pd.set_options('display.max_columns', None)
    
    while True:
        if answer == 'no':
            break
            
        print(df[i:i+5])
        answer = input('do you want to display the next 5 rows? yes or no:').lower()
        i += 5


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('most common month', calendar.month_name[common_month])

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('most common day', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['start time'].dt.hour

    common_hour = df['hour'].mode()[0]

    print('most common start hour', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['start station'].mode()[0]
    print('most commonly used start station', common_start)

    # TO DO: display most commonly used end station
    common_end = df['end station'].mode()[0]
    print('most commonly used end station', common_end)

    # TO DO: display most frequent combination of start station and end station trip

    common_start_end = (df['start station'] + ' - ' + df['end station']).mode()[0]
    print('most frequent combination of start and end stations:', common_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time 
    total_time = df['trip duration'].sum()
    print('total travel time', total_time, ' seconds, or ', total_time/3600, ' hours')

    # TO DO: display mean travel time 
    avg_time = df['trip duration'].mean() 
    print('average travel time', avg_time, ' seconds, or ', avg_time/3600, 'hours')

    print("\nThis took %s seconds." % (time.time() - start_time)) 
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('number of user types\n', df['user type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('\n number of gender\n', df['gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'birth year' in df:
        earliest_by_year = int(df['birth year'].min())
        print('\n earliest year of birth\n', earliest_by_year)
        recent_by_year = int(df['birth year'].max())
        print('\n recent year of birth\n', recent_by_year)
        common_by_year = int(df['birth year'].mode()[0])
        print('\n most common year of birth\n', common_by_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
