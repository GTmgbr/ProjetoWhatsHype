from TikTokApipasta.TikTokApi import tiktok
#import pandas as pd 


def main():

    api = tiktok.TikTokApi()

    results = 10

    trending = api.trending(count=results)
    print(trending)

    for tiktok in trending:
        # Prints the text of the tiktok
        print(tiktok['desc'])

    print(len(trending))

if __name__ == "__main__":
    print(tiktok.TikTokApi())
    main()