import ujson
import unicodedata
import utils 
from reviewersorter import review_sorter



def main():
    db = utils.connect_db('Two_Pick_Too_Drunk')
    beer_collection = db['beers']

    ObannonsBeerList = ['42723', #1. *Great Divide Espresso Oak Aged Yeti (9.5%)
                        '40177', #2. *Buffalo Bills Blueberry Oatmeal Stout (7.5%)
                        '29015', #3.  Leinenkugel Sunset Wheat (4.2%)
                        '21192', #4.  Rahr & Sons Ugly Pug (4.5%)
                        '1062' , #5.  Live Oak Hefe (5.2%)
                        '409'  , #6.  North Coast Scrimshaw (4.4%)
                        '2093' , #7.  Dogfish Head 90 Minute IPA (9%)
                        '1907' , #8.  Dos Equis (5%)
                        '2296' , #9.  Big Sky Moose Drool Brown Ale (4.2%)
                        '31601', #10. Rahr & Sons Summertime Wheat (5.2%)
                        '1212' , #11. Blue Moon (5.4%)
                        '1071' , #12. St. Arnold Summer Pils (4.9%)
                        '2508' , #13. Maredsous 8 (8%)
                        '80522', #14. No Label Don Jalapeno (6.7%)
                                 #15. Leprechaun Cider (7.1%)
                        '29602', #16. Smithwick's (4.5%)
                        '862'  , #17. Harp (5%)
                        '6518' , #18. Oskar Blues Dale's Pale Ale (6.5%)
                        '909'  , #19. Killian's Irish Red (4.9%)
                        '639'  , #20. New Castle (4.7%)
                        '1163' , #21. Belhaven Scottish Ale (3.2%)
                        '754'  , #22. Guinness (4.1%)
                        '73'   , #23. Young's Double Choc. Stout (5.2%)
                        '49070', #24. Alaskan White (5.3%)
                        '3434' , #25. Left Hand Milk Stout NITRO (6%)
                        '248'  , #26. Hoegaarden (4.9%)
                        '1352' , #27. Shiner Bock (4.4%)
                        '67274', #28. Shiner Ruby Redbird (4.2%)
                        '13563', #29. Live Oak Liberation (6.2%)
                        '106'  , #30. Sam Adams Spring (5.6%)
                        '299'  , #31. Magic Hat #9 (5.1%)
                        '666'  , #32. Hacker Pschorr Dunkel Weisse (5.3%)
                        '1946' , #33. Franziskaner Hefe-Weiss (5%)
                        '607'  , #34. Fat Tire (5.3%)
                        '1914' , #35. 1554 Enlightened Black Ale (5.5%)
                        '924'  , #36. Franziskaner Dunkel Weiss (5%)
                        '77951', #37. Brooklyn Mary Maple Porter (6.9%)
                        '45576', #38. Southern Star Bombshell Blonde (5.25%)
                        '104'  , #39. Sam Adams Boston Lager (4.7%)
                        '61276', #40. Rahr TX Red (4.5%)
                        '2270' , #41. *Carlsberg 11.2oz (5%)
                        '48139', #42. *Oskar Blues Mama's Yella Pils (5.3%)
                        '47026', #43. *Southern Star Buried Hatchet Stout(8%)
                        '25649', #44. *Pyramid Apricot (5.1%)
                        '65133', #45.  No Label Ridgeback (6.1%)
                        '70379', #46. *Real Ale 15th Anniversary (9.8%)
                        '59987', #47. *Victory Summer Love (5.2%)
                        '34804', #48. *Land Shark 4.7%)
                        '4041' , #49.   Moylan's Kilt Lifter (8%)
                        '34704', #50. *Independence Austin Amber (4.9%)
                        '412'  , #51. *North Coast Old Rasputin (9%)
                        '1344' , #52. *St. Arnold Fancy Lawn Mower (4.9%)
                        '752'  , #53. *Guinness Foreign Extra Stout (7.5%)
                        '57286', #54. *Guinness Black Lager (4.5%)
                        '650'  , #55. *Guinness Extra Stout (6%)
                        '1587' , #56. *Dogfish Head Midas Touch (9%)
                        '246'  , #57. *Heineken (5%)
                        '4083' , #58. *Stone Ruination IPA (7.7%)
                        '77266', #59. Harpoon Black IPA (7%)
                        '7712' , #60. *Lindeman's Faro (4%)
                        '23713', #61. *Full Sail Sessions Lager (5.3%)
                        '50740', #62. *Full Sail Sessions Black (5.4%)
                        '65325', #63. *Clown Shoes Tramp Stamp (7%)
                        '8951' , #64. *Stone Oaked Arrogant Bastard (7.2%)
                        '11922', #65. *Geat Divide Titan IPA (7.1%)
                        '49789', #66. *Lagunitas Lil Sumpin (7.5%)
                                 #67. *Angry Orchard Ginger Apple Cider (5%)
                        '132'  , #68. *Ayinger Brau-Weisse (5.1%)
                        '689'  , #69. *Red Stripe (4.7%)
                        '222'  , #70. *Fullers London Pride (5.4%)
                                 #71. *Strongbow Cider (5%)
                        '3951' , #72. *Dogfish Head Aprihop (7%)
                        '14712', #73. *Oskar Blues Old Chub Scottish Ale(6.5%)
                        '48933', #74. *Harpoon UFO White (4.8%)
                        '19956'] #75. *Rahr & Sons Blonde Lager (4.8%)


    reviews = reviews = utils.read_beers()
    obannonsReviews = list()
    obannonsDict = dict()
    json = open('ObannonsData.json','w')
    for review in reviews:
        if review['BeerId'] in ObannonsBeerList:
            obannonsReviews.append(review)
            s = ujson.dumps(review)
            json.write(s+'\n')
    json.close()
    reviewersorter = review_sorter('obannons_reviews')
    reviewersorter.sort_reviews(obannonsReviews)

    for review in obannonsReviews:
        if review['BeerId'] in obannonsDict:
            obannonsDict[review['BeerId']].append(review['Reviewer'])
        else:
            obannonsDict[review['BeerId']] = [review['Reviewer']]

    for beer in obannonsDict:
        Beer = beer_collection.find_one({"BeerId":beer})
        #print 'Beer: '+Beer['Brewery']+ ' '+ Beer['Name'] + '\nNumber of reviews: '+str(len(obannonsDict[beer]))+'\n'
    


if __name__=="__main__":
    main()
