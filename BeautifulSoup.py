"""Gets a url and returns the word frequency in that page

Args:
    url(str) = The url you'd like to request the word frequency of

returns: The frequency of the words in the webpage resulted from the scraping.

"""

from import_file import *

def webscraper():
    url = sys.argv[1]
    print(url)
    with urllib.request.urlopen(url) as response: html = response.read()
    soup = BeautifulSoup(html, features='html.parser')
    text = soup.get_text()
    #to parse the data we have differenct options
    #getting text only
    #print(text)
    #to get all the urls in the page
    urls = soup.find_all('a')
    #print(urls)
    #we can also search for specific 
    # print(soup.find_all("about"))
    #Let's go ahead and tokenize the text into words to create the frequency of them
    tkn_word = word_tokenize(text)
    # print(tkn_word)
    sw = set(stopwords.words("english"))
    filtered_words = [w for w in tkn_word if not w in sw]
    #Words after removing the stop words are
    # print(filtered_words)
    #Let's remove the unecessary punctuations from the words
    filtered_words = [wd for wd in filtered_words if wd not in string.punctuation]
    common_words = ["Python", "Module", "Documentation", "license"]
    filtered_words = [wds for wds in filtered_words if wds not in common_words]
    return filtered_words

#def main():
    #main function to call the webscraper and plotitout method
    
    
def plotitout(filtered_words):
    fd = FreqDist(filtered_words)
    layout = dict(title="Frequency distribution of the words", xaxis=dict(title="x-axis"), yaxis=dict(title="y-axis"))
    # fig = ex.bar(fd)
    # fig.show()
    fd.plot(20)
    
    #df_filtered_words = [df_filtered_words]
 
    # fig.show()
    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Word Frequency generator')

    parser.add_argument('URL', type=str,
        help='The URL to fetch the word densities from')
    args = parser.parse_args()
    filtered_words = []
    filtered_words = webscraper()
    # print(filtered_words)
    plotitout(filtered_words)