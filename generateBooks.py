import argparse
import random
import json

'''
Buckets of words
'''
title_article = ['A', 'The', '']
title_adjective_bucket = ['Rolling', 'Cold', 'Freezing', 'Outrageous', 'Good', 'Strong', 'Savage', 'Weak', 'Blazing', 'Frozen', 'Molten', 'Happy', 'Loud', 'Quiet', 'Ultimate'] + [''] * 5
title_noun1_bucket = ['War', 'Transformer', 'Emerald', 'Gem', 'Stone', 'Legend', 'Jet-Ski', 'Beacon', 'Joy', 'Fear', 'Anguish', 'Sadness', 'Agility', 'Star', 'Rock', 'Witch', 'Wizard']  + [''] * 5
title_noun2_bucket = ['Fish', 'Dog', 'King', 'Tank', 'Forest', 'Beans', 'Spring', 'Water', 'Train', 'Camper', 'Slacker', 'Noble', 'Peasant', 'Serf', 'Slime', 'Book', 'Life', 'Cat', 'Umbrella', 'Man', 'Lady', 'Dragon']
title_seq_num = [1,2,3,4,5,6,7,8,9] + [1] * 10
author_first_name_bucket = ['Jack', 'Jolin', 'Catherine', 'Michael', 'Boris', 'Torus', 'Meek', 'Peter', 'Walter', 'Edwards', 'Mick', 'Sans' ]
author_last_name_bucket = ['Talent', 'Logan', 'Lee', 'Jagger', 'Edison', 'Faust', 'Clement', 'Johns', 'Parker', 'Jordan', 'Jones', 'Michelin', 'Mark', 'Neil', 'Neumman', 'Kins']
rating_buckets = [50, 100, 400, 400, 500, 550]
subjects_buckets = ['Non-Fiction', 'Mathematics', 'Science', 'Biography', 'Physics', 'IT', 'Biology', 'Self-Improvement', 'Fiction', 'Action', 'Thriller', 'Horror', 'Comedy', 'Romance']

lorem_ipsum_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In sagittis mauris congue quam tincidunt sollicitudin. Aliquam a mollis odio. Cras ut ipsum vitae leo scelerisque viverra. Donec tellus augue, congue at est quis, convallis lobortis tortor. Nulla rhoncus pulvinar sem, vitae malesuada nisl. Ut dolor turpis, laoreet hendrerit ullamcorper eget, blandit ac diam. Cras scelerisque vitae urna at fermentum. Aliquam rhoncus lobortis eros, at dignissim mi tempus quis. Quisque et venenatis risus, sed rhoncus sem. Morbi venenatis gravida lectus, vitae porttitor magna feugiat non. Ut gravida tincidunt est nec sodales. Pellentesque maximus, enim vitae varius venenatis, orci sapien porttitor ex, id tempor arcu leo aliquam nunc. Fusce ultricies turpis at ligula interdum hendrerit. Integer bibendum arcu eget bibendum consequat. Donec efficitur velit ut purus auctor blandit. Nulla consequat id ipsum et tincidunt. Integer non sollicitudin est. Etiam consequat eu neque id scelerisque. In placerat odio eros, a ornare risus euismod consectetur. Fusce quis condimentum nisl. Sed dignissim suscipit nisl et ultrices. Etiam euismod condimentum nisl, nec vestibulum lorem. Praesent a enim at augue egestas lobortis vitae sed augue. Morbi id quam at dui interdum luctus. Duis fermentum dolor ipsum, ut convallis dui ullamcorper vel. Suspendisse convallis, tortor consectetur elementum lacinia, ipsum nisl commodo nulla, id sollicitudin quam metus pellentesque eros. Aliquam ac dictum mi. Sed elementum risus nulla, ut congue felis porta at. Curabitur hendrerit ligula eu orci commodo, non fermentum turpis mattis. Integer commodo risus vel tortor luctus lobortis. Vestibulum sodales congue semper. Vestibulum in eros in lectus tempus vehicula non non sem. Sed pharetra pharetra facilisis. In quis justo erat. Donec gravida in orci at porttitor. Quisque eget faucibus urna. Aenean sed imperdiet nulla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Etiam vitae nibh non felis condimentum eleifend. Donec auctor id purus nec lobortis. Suspendisse eleifend fermentum sollicitudin. Sed nec lacus tempus enim hendrerit aliquet. Lorem ipsum dolor sit amet, consectetur adipiscing elit. In sagittis mauris congue quam tincidunt sollicitudin. Aliquam a mollis odio. Cras ut ipsum vitae leo scelerisque viverra. Donec tellus augue, congue at est quis, convallis lobortis tortor. Nulla rhoncus pulvinar sem, vitae malesuada nisl. Ut dolor turpis, laoreet hendrerit ullamcorper eget, blandit ac diam. Cras scelerisque vitae urna at fermentum. Aliquam rhoncus lobortis eros, at dignissim mi tempus quis. Quisque et venenatis risus, sed rhoncus sem. Morbi venenatis gravida lectus, vitae porttitor magna feugiat non. Ut gravida tincidunt est nec sodales. Pellentesque maximus, enim vitae varius venenatis, orci sapien porttitor ex, id tempor arcu leo aliquam nunc. Fusce ultricies turpis at ligula interdum hendrerit. Integer bibendum arcu eget bibendum consequat. Donec efficitur velit ut purus auctor blandit. Nulla consequat id ipsum et tincidunt. Integer non sollicitudin est. Etiam consequat eu neque id scelerisque. In placerat odio eros, a ornare risus euismod consectetur. Fusce quis condimentum nisl. Sed dignissim suscipit nisl et ultrices. Etiam euismod condimentum nisl, nec vestibulum lorem. Praesent a enim at augue egestas lobortis vitae sed augue. Morbi id quam at dui interdum luctus. Duis fermentum dolor ipsum, ut convallis dui ullamcorper vel. Suspendisse convallis, tortor consectetur elementum lacinia, ipsum nisl commodo nulla, id sollicitudin quam metus pellentesque eros. Aliquam ac dictum mi. Sed elementum risus nulla, ut congue felis porta at. Curabitur hendrerit ligula eu orci commodo, non fermentum turpis mattis. Integer commodo risus vel tortor luctus lobortis. Vestibulum sodales congue semper. Vestibulum in eros in lectus tempus vehicula non non sem. Sed pharetra pharetra facilisis. In quis justo erat."

'''
Functions to generate fake data
'''
def generateTitle():
    title_array = []
    article = random.choice(title_article)
    adjective = random.choice(title_adjective_bucket)
    noun1 = random.choice(title_noun1_bucket)
    noun2 = random.choice(title_noun2_bucket)
        
    if article != '':
        title_array.append(article)
    if adjective != '':
        title_array.append(adjective)    
    if noun1 != '':
        title_array.append(noun1)
        title_array.append('of')
    title_array.append(noun2)
    
    title = ' '.join(title_array)   
    num = random.choice(title_seq_num)

    if num != 1:
        title += ' %d' % num

    return title

def generateAuthor():
    return random.choice(author_first_name_bucket) + ' ' + random.choice(author_last_name_bucket)

def generateRandomText():
    textDeck = lorem_ipsum_text.split()
    randSize = random.randrange(60, len(textDeck))
    subDeck = textDeck[:randSize]
    random.shuffle(subDeck)
    return ' '.join(subDeck)

def generateRating():
    score_count = [0] * 6
    score_count[0] = random.randrange(0, rating_buckets[0] + 1)
    score_count[1] = random.randrange(0, rating_buckets[1] + 1)
    score_count[2] = random.randrange(0, rating_buckets[2] + 1)
    score_count[3] = random.randrange(0, rating_buckets[3] + 1)
    score_count[4] = random.randrange(0, rating_buckets[4] + 1)
    score_count[5] = random.randrange(0, rating_buckets[5] + 1)

    total_count = score_count[0] + score_count[1] + score_count[2] + score_count[3] + score_count[4] +  score_count[5] 
    total_score = score_count[1] + score_count[2] * 2 + score_count[3] * 3 + score_count[4] * 4 + score_count[5] * 5

    return total_score / total_count

def generatePrice():
    return random.randrange(200, 10000) / 100

def generateSubjects():
    subject_count = random.randrange(1, 5)
    subjects = random.sample(subjects_buckets, k=subject_count)

    return subjects

def generatePublishedDate():
    rand_year = 2021 - random.randrange(0, 40)
    rand_month = random.randrange(1, 13)
    rand_day = random.randrange(1, 27)

    '"2010-11-18T00:00:00.000+00:00"'
    return "%d-%.2d-%.2dT00:00:00.000+00:00" % (rand_year, rand_month, rand_day)

def generateISBN():

    '''
    Not real
    '''
    rand_1 = random.randrange(960, 980)
    rand_2 = random.randrange(0, 5)
    rand_3 = random.randrange(1000, 9999)
    rand_4 = random.randrange(1000, 9999)
    rand_5 = random.randrange(1, 9)

    return "%.3d-%d-%.4d-%.4d-%d" % (rand_1, rand_2, rand_3, rand_4, rand_5)

def generateBooksJSON(count, outFile) -> None:

    booksArray = []

    int_count = int(count)

    for i in range(int_count):       
        '''
        {
    "title" : "Rolling Stone",
    "author" : "Mick Jagger",
    "summary" : "In vitae iaculis erat, et laoreet est. Nam lectus nulla, hendrerit ac ipsum ut, scelerisque imperdiet justo. Integer dapibus ipsum eu condimentum dapibus. Proin nisl metus, congue non odio et, ultricies cursus nisi. Proin neque augue, molestie eget mi nec, suscipit rhoncus lorem. Aliquam fermentum vel lacus quis vestibulum. Nunc fringilla rutrum massa, a convallis magna pretium ut. Nulla dictum rutrum arcu luctus tempus. Suspendisse tellus quam, auctor eget risus at, tempor pharetra dui. Integer sed feugiat augue. Morbi convallis et urna nec consectetur. Integer et ante imperdiet, vulputate mi vitae, sodales augue. Integer molestie tristique enim, sit amet luctus ante vestibulum sit amet. Aliquam elementum nunc ut mi porta, vel efficitur diam cursus.",
    "publishedDate" : {"$date": "2010-11-18T17:13:15.953+00:00"},
    "isbn" : "978-4-6797-2572-1",
    "rating" : 4.8,    
    "subjects": ["Non-Fiction", "Biography"],
    "price": 15.00
    "_class": "com.canary.bookstore.Book"
}
        '''
        book = {}
        book['title'] = generateTitle()
        book['author'] = generateAuthor()
        book['summary'] = generateRandomText()
        book['publishedDate'] = {'$date': generatePublishedDate()}
        book['isbn'] = generateISBN()
        book['rating'] = generateRating()
        book['subjects'] = generateSubjects()
        book['price'] = generatePrice()
        book['_class'] = "com.canary.bookstore.Book"
        booksArray.append(book)

    with open(outFile, 'w') as outFile:
        json_out = json.dumps(booksArray)
        outFile.write(json_out)

def main() -> None:
    parser = argparse.ArgumentParser(description="Generate fake book data and output as json")
    parser.add_argument('-c', '--count', help='Specify number of books to generate', required=True)
    parser.add_argument('-out', '--outFile', help='Specify the output file name', required=True)
    
    args = parser.parse_args()

    generateBooksJSON(args.count, args.outFile)    

if __name__ == "__main__":
    main()