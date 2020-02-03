import wikipedia
import sys


def scrape():
    search_results = wikipedia.search("cats", results=50)
    index = 0
    for result in search_results:
        try:
            print(str(index) + " [scraping]: " + result, file=sys.stderr)
            page = wikipedia.page(result)
            summary = page.summary
            summary = summary.replace('"', '\\"')
            summary = summary.replace('\n', '\\n')
            string_literal = '"' + summary + '",'
            print(string_literal)
        except wikipedia.exceptions.DisambiguationError:
            print("DisambiguationError: skipping...", file=sys.stderr)
        except wikipedia.exceptions.WikipediaException:
            print("WikipediaException: skipping...", file=sys.stderr)
        finally:
            index = index + 1
