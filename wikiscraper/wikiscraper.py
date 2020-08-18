import wikipedia
import sys
import argparse

def scrape():
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--query", help="number of results", type=str, default="cats")
    parser.add_argument("-c", "--count", help="number of results", type=int, default=50)
    parser.add_argument("--csv", help="output csv formatted strings", action="store_true")
    args = parser.parse_args()

    print("[Query]: " + args.query, file=sys.stderr)
    print("[ResultCount]: " + str(args.count), file=sys.stderr)
    print("[CSV]: " + str(args.csv), file=sys.stderr)
   
    search_results = wikipedia.search(args.query, results=args.count)

    if args.csv:
        print("key,input1")
        
    index = 0
    for result in search_results:
        try:
            print(str(index) + " [result]: " + result, file=sys.stderr)
            page = wikipedia.page(result)
            summary = page.summary

            if args.csv:
                summary = summary.replace('"', '""')
                string_literal = str(index) + ',"' + summary + '"'
                print(string_literal)
            else:
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
