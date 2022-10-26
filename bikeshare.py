import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
all_and_midyear = ['all','january','february','march','april','may','june']
all_and_days = ['All','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please enter the city you want to know your results ').lower()
    while city.lower() not in CITY_DATA :
          city = input('Please enter one of the following cities:(chicago, new york city, washington):_ ').lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please enter the month you want to know your results ').lower()
    while month.lower() not in all_and_midyear :
          month = input('Please enter the month you want to know your results(all, january, february, ... , june) ').lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please enter the day you want to know your results ').title()
    while day.title() not in all_and_days :
          day = input('Please enter the day you want to know your results(all, monday, tuesday, ... sunday) ').title()

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
    df['day_week_name'] = df['Start Time'].dt.weekday_name   
    if month != 'all':
       midyear = ['january', 'february', 'march', 'april', 'may', 'june']
       month = midyear.index(month) + 1
       df = df[df['month'] == month]
    if day != 'All':
       df = df[df['day_week_name'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('the most common month is : {}'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('the most common day of week is : {}'.format(df['day_week_name'].mode()[0]))

    # TO DO: display the most common start hour
    print('the most common start hour is : {}'.format(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('the most common start station is : {}'.format(df['Start Station'].mode()[0]))
    # TO DO: display most commonly used end station
    print('the most common end station is : {}'.format(df['End Station'].mode()[0]))
    # TO DO: display most frequent combination of start station and end station trip
    df['itinerary'] = df['Start Station'] + ':'+ df['End Station']
    print('the most common itinerary in this city is : {}'.format(df['itinerary'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time in hours : {}h'.format(((df['Trip Duration'].sum())/360).round()))

    # TO DO: display mean travel time
    print('mean travel time in minute : {}M'.format(((df['Trip Duration'].mean())/60).round()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Types of users and the number of each:_\n{}'.format(df['User Type'].value_counts().to_frame()))

    # TO DO: Display counts of gender
    if city != 'washington': 
        print('Types of Gender and the number of each:_\n{}'.format(df['Gender'].value_counts().to_frame()))

    # TO DO: Display earliest, most recent, and most common year of birth
        print('the oldest common year of birth is:_ {} year'.format(int(df['Birth Year'].min())))
        print('the most common year of birth is:_ {} year'.format(int(df['Birth Year'].mode()[0])))
        print('the newest common year of birth is:_ {} year'.format(int(df['Birth Year'].max())))
    else:
        print('I don\'t know enough information about this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(df):
    #Displays would like to see the raw data in the city
    print('\ndata is available to check.....\n')
    t = 0
    content = input('would like to see the raw data? yes or no:').lower()
    if content not in ['yes','no']:
       content = input('invalid choice....would like to see the raw data? yes or no:').lower()
    elif content != 'yes':
       print('Thanks a lot')
    else:
        while t+5 < df.shape[0]:
             print(df.iloc[t:t+5])
             t += 5
             content = input('would like to see the raw data? yes or no:').lower()
             if content != 'yes' :
                print('Thanks a lot')
                break  

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        show_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('you are welcome')
            break


if __name__ == "__main__":
	main()
