import tweepy
import csv
import codecs

consumer_key = 'FN3I2eMlJVlAfeG6epxzOOWQs'
consumer_secret = 'cWC4nXZpmb0TvJvkOZjaTvuUdf6suStlmyPKfOvKe4X4CotkiA'
access_key = '46220270-6zsYQ0yAaeTZad3nacxu8cz3xdvmG8KoNueSbt5lG'
access_secret = 'YxzgrcyGUS8evS09CKqd0Or4tdY57FujD4IysKo7yEEOr'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)
api_client = tweepy.API(auth)

tweets = tweepy.Cursor(api_client.search,
                       q='python',
                       result_type="recent",
                       include_entities=True,
                        lang="en").items(1)


#write a function that inputs a key word and it returns the list of tweets
# The cursor method of tweepy return an intemiterator python object
#so now by default our tweets are contained in an itemiterator object

#itemterator objects are like lists but contain much more meta data

#there are 3 ways of dealing with itemiterator objects:
#1, put the itemitterator inside a for loop, for example:
#for t in tweets:
#    print(t.text)

#2, cast the itemiterator into a list, then you can access it like a list:
#eg:
#tweet_list = list(tweets)
#my_first_tweet = tweet_list[0]

#3, use the next() method of the itemiterator object:
#eg
#my_first_tweet = tweet_list.next()



def get_tweets(expression_in,count_in):
    list_out=[]
    tweets = tweepy.Cursor(api_client.search,
                       q=expression_in,
                       result_type="recent",
                       include_entities=True,
                        lang="en").items(count_in)

    tweets_list = list(tweets)
    for t in tweets_list:
        list_out.append((t.author.screen_name,t.author.followers_count,t.text))


    return list_out

def print_tweets(tweet_info_list):
    for t in tweet_info_list:
        print("User{},with {} followers, tweeted ".format(t[0],t[1]))
        print(t[2])
        print('\n')
    return

def write_to_csv(tweet_info_list): # do this!!
    with open('my_new_file.csv', 'w', newline='') as my_file:
        writer = csv.writer(my_file)
        writer.writerows(tweet_info_list)


#get tweets
    #index the tweets (count number of specific word in tweets)
def get_word_freq(string_in):
    freq_table={}
    for w in string_in.split():
        #iterate through strng word by word
        if w in freq_table:
            freq_table[w] = freq_table[w]+1
        else:
            freq_table[w] = 1


    freq_table = list(freq_table.items())
    freq_table.sort(key=lambda x: x[1], reverse=True)
    return freq_table

def aggregate_twits(tweets_list):
    #input: twit1,twit2,twit3
    #output:all the tweets in a twits

    tweet_string_out = ' '.join(tweets_list)

    #freq_table_keys={}
    #sum(freq_table.values())
    #all_words = freq_table.keys()
    #all_words.sort(key=lambda x : freq_table[x])

    return tweet_string_out

def agg_tweets_forloop(tweets_list):
    tweet_sting_out = ''
    for tweet in tweets_list:
        tweet_sting_out = tweet_sting_out + ' ' + tweet

    return tweet_sting_out[1:]

def write_to_csv(tweet_info_list, csv_file_name):
    #with open (csv_file_name, 'w', newline='')as my_file:
    with codecs.open(csv_file_name, 'w', encoding='utf8') as my_file: #microsoft ver
        writer = csv.writer(my_file)
        writer.writerows(tweet_info_list)

    return

def write_freq_to_csv(freak_table_list, csv_file_name):
    with codecs.open(csv_file_name, 'w', encoding='utf8') as my_file: #microsoft ver
        writer = csv.writer(my_file)
        writer.writerows(freak_table_list)
    return

my_blacklist = ['and','it']

def gen_csv(expression_in,count_in, tweet_file_name,freq_file_name):
    tweets = get_tweets(expression_in,count_in)
    write_to_csv(tweets,tweet_file_name)

    my_tweet_string = [x[2] for x in tweets]
    my_tweet_string = aggregate_twits(my_tweet_string)
    frequencies = get_word_freq(my_tweet_string)
    frequencies = filter_words(my_blacklist,frequencies)
    write_to_csv(frequencies,freq_file_name)
    return

my_marketing_list = [('tesco', 25, 'tesco_tweets.csv','tesco_freq.csv'),
                     ('sainsbury', 25, 'sainsbury_tweets.csv', 'sainsbury_freq.csv'),
                     ('aldi', 25, 'aldi_tweets.csv', 'aldi_freq.csv'),
                     ('asda', 25, 'asda_tweets.csv', 'asda_freq.csv')]


def auto_gen_csv(marketing_list):
    for m in marketing_list:
        gen_csv(m[0],m[1],m[2],m[3])
    return

def filter_words(blacklist, freq_list_in):
    # example: blacklist = ['and','i' etc]
    return[f for f in freq_list_in if f[0] not in blacklist and 'http' not in f[0]]
