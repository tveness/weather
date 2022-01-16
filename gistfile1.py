import requests
import re

# precompile our regexs since we use them on every iteration
wordRE = re.compile(r'"hw">([^<]+)<')
pronounceRE = re.compile(r'\\([^;,\\]+)')
typeRE = re.compile(r'<i>([^<]+)</i>')
defRE = re.compile(r'<b>1.</b> ([^<]+)')
otherDefRE = re.compile(r'-->([^<]+)</p>', re.DOTALL)

# helper function to extract a regex from a string
def get(html, RE):
    return RE.search(html).group(1).strip()
    
# helper function to extract one of two regexs from a string
# yeah, it's ugly. who cares
def getTry(html, re1, re2):
    match = re1.search(html)
    if match:
        return match.group(1).strip()
    return get(html, re2)

def scrapePage(year, month, day):
    try:
        response = requests.get("http://dictionary.reference.com/wordoftheday/archive/%d/%02d/%02d.html" % (year, month, day));
        html = response.read()

        # slice it twice so the second find is faster
        # could have been done better by saving the result of the first find
        # and searching from that point for the second one
        html = html[html.find("<span class=\"hw\">"):]
        html = html[:html.find("<!-- SECBR -->")]
        
        word = "%s /%s/ (%s)" % (get(html, wordRE), get(html, pronounceRE), get(html, typeRE))
        defin = getTry(html, defRE, otherDefRE)
        
        print("%s\t%s" % (word, defin))
        print("%s\t%s" % (defin, word))
    except:
        pass

# no leap years - good enough
daysInMonth = [31, 27, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for year in range(2000, 2013):
    for month in range(1, 13):
        for day in range(1, daysInMonth[month - 1] + 1):
            scrapePage(year, month, day)
