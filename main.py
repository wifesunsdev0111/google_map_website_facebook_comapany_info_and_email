from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep
import time
import threading
import getEmail
import re
import quickstart
import threading
import getWebsiteIn
import facebook
# import getAllCities




all_cities = [   'Runge, TX', 'Tatum, TX', 'Bluffton, TX', 'Katy, TX', 'Jayton, TX', 'Weinert, TX', 'Coahoma, TX', 'Orange Grove, TX', 'Lorenzo, TX', 'Frisco, TX', 'Fort Mc Kavett, TX',
 'Driftwood, TX', 'Lott, TX', 'Damon, TX', 'Stockdale, TX', 'Groesbeck, TX', 'Ennis, TX', 'Hamilton, TX', 'Gainesville, TX', 'Beasley, TX', 'Lolita, TX', 'Briscoe, TX', 'Riviera, TX', 'Ravenna, TX', 'Kemah, TX',
 'Blue Ridge, TX', 'Fieldton, TX', 'Denver City, TX', 'Wallisville, TX', 'Blanco, TX', 'Tokio, TX', 'Morgan, TX', 'Ferris, TX', 'Mount Enterprise, TX', 'Cranfills Gap, TX', 'Savoy, TX', 'Pearland, TX', 'Leander, TX',
 'Kountze, TX', 'Masterson, TX', 'Spearman, TX', 'Pinehurst, TX', 'Tell, TX', 'Granbury, TX', 'Sulphur Springs, TX', 'Daingerfield, TX', 'Yoakum, TX', 'Rosebud, TX', 'Moore, TX', 'Memphis, TX', 'Rogers, TX',
 'Fort Hancock, TX', 'Van, TX', 'Forreston, TX', 'Seabrook, TX', 'Overton, TX', 'Tyler, TX', 'Huntsville, TX', 'Onalaska, TX', 'Wolfe City, TX', 'Sunnyvale, TX', 'Eden, TX', 'Atascosa, TX', 'Nash, TX',
 'Wildorado, TX', 'Alba, TX', 'Linn, TX', 'Goodfellow Afb, TX', 'Galveston, TX', 'Smithville, TX', 'Nolan, TX', 'Coolidge, TX', 'Van Vleck, TX', 'Claude, TX', 'Christine, TX', 'Delmita, TX', 'Woodville, TX',
 'Willis, TX', 'Texas City, TX', 'Horseshoe Bay, TX', 'Era, TX', 'D Hanis, TX', 'Pecos, TX', 'Lelia Lake, TX', 'Bergheim, TX', 'Forney, TX', 'Fort Hood, TX', 'George West, TX', 'New Braunfels, TX', 'Pilot Point, TX',
 'Valentine, TX', 'Diboll, TX', 'Southlake, TX', 'Chico, TX', 'Bigfoot, TX', 'Willow City, TX', 'Robstown, TX', 'El Campo, TX', 'Alvin, TX', 'Dumas, TX', 'Adrian, TX', 'Earth, TX', 'Chatfield, TX', 'Leesville, TX',
 'Haltom City, TX', 'Pottsville, TX', 'Bynum, TX', 'Wills Point, TX', 'Balch Springs, TX', 'Gardendale, TX', 'Clute, TX', 'Henrietta, TX', 'Wimberley, TX', 'Stinnett, TX', 'Loraine, TX', 'Aledo, TX', 'Electra, TX',
'Abbott, TX', 'Brazoria, TX', 'Farwell, TX', 'Satin, TX', 'Ivanhoe, TX', 'Arthur City, TX', 'Fritch, TX', 'Texline, TX', 'Comfort, TX', 'Grapevine, TX', 'Maryneal, TX', 'Throckmorton, TX', 'Gilmer,TX', 'Lometa, TX',
'Kingsville, TX', 'Asherton, TX', 'Garwood, TX', 'Gatesville, TX', 'Colmesneil, TX', 'Wingate, TX', 'Elm Mott, TX', 'Bridgeport, TX', 'Powderly, TX', 'Brownsville, TX', 'Eagle Pass, TX', 'Camp Wood, TX',
'Canutillo, TX', 'Hempstead, TX', 'Stratford, TX', 'Clint, TX', 'Dodd City, TX', 'Campbellton, TX', 'Lake Dallas, TX', 'Kempner, TX', 'The Colony, TX', 'Higgins, TX', 'Garland, TX', 'Point, TX', 'Donie, TX',
'Rio Vista, TX', 'Milford, TX', 'Manchaca, TX', 'Thrall, TX', 'Kingwood, TX', 'Bellevue, TX', 'Carlsbad, TX', 'Garden City, TX', 'Bangs, TX', 'Center Point, TX', 'Lopeno, TX', 'Lancaster, TX', 'La Joya, TX',
'London, TX', 'Wiergate, TX', 'Commerce, TX', 'Hawkins, TX', 'West, TX', 'Edcouch, TX', 'Chillicothe, TX', 'Meridian, TX', 'Loop, TX', 'Centerville, TX', 'Santo, TX', 'Tarzan, TX', 'Ingleside, TX', 'Midlothian, TX',
'Salado, TX', 'Highlands, TX', 'Borger, TX', 'Childress, TX', 'Ringgold, TX', 'Evant, TX', 'Cibolo, TX', 'Scotland, TX', 'Mart, TX', 'Needville, TX', 'Bivins, TX', 'Bryan, TX', 'Ralls, TX', 'Alamo, TX',
'Seminole, TX', 'De Berry, TX', 'Diana, TX', 'Chandler, TX', 'Wortham, TX', 'Richland, TX', 'Mertzon, TX', 'Palo Pinto, TX', 'Harlingen, TX', 'Turkey, TX', 'La Marque, TX', 'Edgewood, TX', 'Sandia, TX',
'Trinity, TX', 'Brookeland, TX', 'Montalba, TX', 'Clarksville, TX', 'Mesquite, TX', 'Cuero, TX', 'Ladonia, TX', 'Lindale, TX', 'Fairfield, TX', 'Valley Spring, TX', 'Silverton, TX', 'La Grange, TX', 'Anderson, TX',
'San Benito, TX', 'Carrollton, TX', 'Euless, TX', 'Tilden, TX', 'O Brien, TX', 'Rockwall, TX', 'Grand Saline, TX', 'Meadow, TX', 'Corsicana, TX', 'Hitchcock, TX', 'Caddo Mills, TX', 'Boyd, TX', 'Hutto, TX',
'Weimar, TX', 'Emory, TX', 'Lipan, TX', 'Anahuac, TX', 'Kendalia, TX', 'Sinton, TX', 'Taft, TX', 'Converse, TX', 'Beckville, TX', 'Whitesboro, TX', 'Caddo, TX', 'New Boston, TX', 'Marshall, TX', 'Grand Prairie, TX',
'Kirbyville, TX', 'Warren, TX', 'San Juan, TX', 'Canyon, TX', 'West Point, TX', 'Millsap, TX', 'Valley Mills, TX', 'Rio Grande City, TX', 'Little Elm, TX', 'Morse, TX', 'Portland, TX', 'Petersburg, TX',
'Harker Heights, TX', 'Hewitt, TX', 'Hebbronville, TX', 'Klondike, TX', 'Ingram, TX', 'Collinsville, TX', 'Bertram, TX', 'Spicewood, TX', 'Mineola, TX', 'Florence, TX', 'Quitman, TX', 'Richland Springs, TX',
'Olton, TX', 'Muleshoe, TX', 'Kress, TX', 'Greenville, TX', 'Yorktown, TX', 'Shallowater, TX', 'Stanton, TX', 'Whitney, TX', 'Kennedale, TX', 'Burlington, TX', 'Dallas, TX', 'Gorman, TX', 'Bandera, TX',
'Balmorhea, TX', 'Brookesmith, TX', 'Spring Branch, TX', 'Woodsboro, TX', 'Flower Mound, TX', 'Fred, TX', 'Falfurrias, TX', 'Flint, TX', 'Italy, TX', 'Granger, TX', 'Dickens, TX', 'Keller, TX', 'Porter, TX',
'Poteet, TX', 'Yancey, TX', 'Graford, TX', 'Vega, TX', 'Anthony, TX', 'Santa Elena, TX', 'Mc Caulley, TX', 'Webster, TX', 'Abilene, TX', 'Andrews, TX', 'Follett, TX', 'Scroggins, TX', 'San Augustine, TX',
'Tenaha, TX', 'Bluff Dale, TX', 'Desdemona,TX', 'Pledger, TX', 'Aspermont, TX', 'Sachse, TX', 'Bedford, TX', 'Whitsett, TX', 'Chester, TX', 'Axtell, TX', 'Bartlett, TX', 'Elgin, TX', 'Marble Falls, TX', 'Louise, TX',
'Brackettville, TX', 'Anton, TX', 'Palmer, TX', 'Tynan, TX', 'Rhome, TX', 'Telephone, TX', 'Talpa, TX', 'Refugio, TX', 'Glidden, TX', 'Rockwood, TX', 'White Oak, TX', 'Winnsboro, TX', 'Uvalde, TX', 'Baird, TX',
'Art, TX','Rotan, TX', 'La Vernia, TX', 'South Bend, TX', 'Hamlin, TX', 'Tivoli, TX', 'Coppell, TX', 'Batesville, TX', 'Rule, TX', 'Castell, TX', 'Lovelady, TX', 'Coupland, TX', 'Prairie Hill, TX', 'Albany, TX',
'Pleasanton, TX', 'Seadrift, TX', 'Miles, TX', 'Gruver, TX', 'Crosby, TX', 'Petrolia, TX', 'Dawson, TX', 'Richards, TX', 'Queen City, TX', 'Mcadoo, TX', 'Goree, TX', 'Merkel, TX', 'Canadian, TX', 'Haskell, TX',
'Tye, TX', 'Benjamin, TX', 'Crowell, TX', 'Hondo, TX', 'Linden, TX', 'Dike, TX', 'El Paso, TX', 'Krum, TX', 'Argyle, TX', 'Del Valle, TX', 'Trinidad, TX', 'Hull, TX', 'Brady, TX', 'Big Sandy, TX', 'Kemp, TX',
'Melvin, TX', 'Santa Rosa, TX', 'Vernon, TX', 'Mount Pleasant, TX', 'Harwood, TX', 'Oakwood, TX', 'Roaring Springs, TX', 'Riesel, TX', 'Richmond, TX', 'Georgetown, TX', 'Fort Davis, TX', 'Kaufman, TX',
'Angleton, TX', 'Hext, TX', 'Pointblank, TX', 'Denton, TX', 'Bruceville, TX', 'Sudan, TX', 'Booker, TX', 'Burkett, TX', 'Lorena, TX', 'Manor, TX', 'Grandview, TX', 'Karnack, TX', 'Blooming Grove, TX', 'Conroe, TX',
'Jourdanton, TX', 'Sabinal, TX', 'Jonesboro, TX', 'Liverpool, TX', 'Sylvester, TX', 'Hughes Springs, TX', 'Tarpley, TX', 'Waxahachie, TX', 'Hallsville, TX', 'Liberty, TX', 'Washington, TX', 'Quinlan, TX',
'Harrold, TX', 'Crystal City, TX', 'Beeville, TX', 'Bronte, TX', 'Addison, TX', 'Newton, TX', 'Buffalo, TX', 'Pearsall, TX', 'Mirando City, TX', 'Jermyn, TX', 'Sweeny, TX', 'Wayside, TX', 'Quanah, TX', 'Belton, TX',
'Brownfield, TX', 'Lueders, TX', 'Justiceburg, TX', 'Voca, TX', 'Bremond, TX', 'Haslet, TX', 'Rio Frio, TX', 'Pineland, TX', 'Bonham, TX', 'Premont, TX', 'Cedar Creek, TX', 'Omaha, TX', 'Fischer, TX',
'Palestine, TX', 'Seymour, TX', 'Millersview, TX', 'Cost, TX', 'Stafford, TX', 'Crosbyton, TX', 'Natalia, TX', 'Rio Medina, TX', 'Bruni, TX', 'Eldorado, TX', 'Elkhart, TX', 'Rockport, TX', 'Baytown, TX',
'Falls City, TX', 'Honey Grove, TX', 'Sulphur Bluff, TX', 'Troup, TX', 'Tomball, TX', 'Barry, TX', 'Tennessee Colony, TX', 'Canyon Lake, TX', 'Comstock, TX', 'Edinburg, TX', 'Paradise, TX', 'Quail, TX', 'Roby, TX',
'Crane, TX', 'Colorado City, TX', 'Fort Worth, TX', 'Cat Spring, TX', 'Gary, TX', 'Oakhurst, TX','Carmine, TX', 'Mason, TX', 'Laneville, TX', 'Buna, TX', 'Paris, TX', 'Summerfield, TX', 'Howe, TX', 'Dayton, TX',
'Athens, TX', 'Bedias, TX', 'Cedar Hill, TX', 'Whitt, TX', 'Bulverde, TX', 'La Feria, TX', 'Montgomery, TX', 'Oakville, TX', 'Kingsbury, TX', 'Mabank, TX', 'Eagle Lake, TX', 'Mineral Wells, TX', 'Silsbee, TX',
'Hallettsville, TX', 'Dublin, TX', 'Mount Calm, TX', 'Stephenville, TX', 'Springtown, TX', 'Call, TX', 'Troy, TX', 'Plano, TX', 'Lone Star, TX', 'Larue, TX', 'Santa Anna, TX', 'Cotulla, TX', 'Bayside, TX',
'Round Top, TX', 'Salt Flat, TX', 'Midland, TX', 'Madisonville, TX', 'Danbury, TX', 'Tuscola, TX', 'Del Rio, TX']

for index, city in enumerate(all_cities):
    
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com/maps/")

    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[jsname=\"b3VHJd\"]"))).click()
    except:
        pass

    sleep(5)
        
    search_input = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class=\"searchboxinput xiQnY\"]")))

    search_string = "fence contractors in " + city
    print(f'Search String = ', search_string)
    search_input.clear()
    search_input.send_keys(search_string)
    sleep(2)
    search_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class=\"google-symbols\"]")))
    search_button.click()
    sleep(5)

    # Get the initial page height
    try:
        scroll_div = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"m6QErb DxyBCb kA9KIf dS8AEf ecceSd\"]")))
        page_height = driver.execute_script("return arguments[0].scrollHeight;", scroll_div)

        while True:
            # Scroll to the bottom of the page
            driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", scroll_div)
            fence_lists = fence_lists = driver.find_elements(By.CSS_SELECTOR, "div[class=\"Nv2PK tH5CWc THOPZb \"], div[class=\"Nv2PK Q2HXcd THOPZb \"]")
            sleep(7)

            try:
                end_contet = driver.find_element(By.CSS_SELECTOR, "span[class=\"HlvSq\"]")
                if end_contet:
                    print(f"Scroll End", end_contet.text)
                    break
            except:
                continue
    except:
        fence_lists = fence_lists = driver.find_elements(By.CSS_SELECTOR, "div[class=\"Nv2PK tH5CWc THOPZb \"], div[class=\"Nv2PK Q2HXcd THOPZb \"]")
        pass

    # try:
    #     fence_lists = driver.find_elements(By.CSS_SELECTOR, "div[class=\"Nv2PK tH5CWc THOPZb \"]")
    # except:
    #     pass
        
   
    sleep(2)

    for index, fence in enumerate(fence_lists):

        try:
            driver.execute_script("arguments[0].scrollIntoView(false); window.scrollBy(0, 0);", fence)
        except:
            pass
        print(f'Total Fence Count = ', len(fence_lists), index)
                    
        try:
            location_click = WebDriverWait(fence, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class=\"hfpxzc\"]")))
            driver.execute_script("arguments[0].click();", location_click)
        except:
            pass

        sleep(4)
        email = ""
        fence_name = ""
        website= ""
        facebook_url = ""
        phone_number = ""
        location_name = ""
        rating_of_reviews = ""
        google_map_website = ""
        google_map_domain = ""
        facebook_email = []

        try:
            quickstart.main()
        except:
            pass
        
        try:
            
            fence_name = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1[class=\"DUwDvf lfPIob\"]"))).text
        except:
            pass
        
        print(f'fence_name = ', fence_name)
        
        try:
            phone_button = driver.find_element(By.CSS_SELECTOR, 'img.Liguzb[src="//www.gstatic.com/images/icons/material/system_gm/1x/phone_gm_blue_24dp.png"]').find_element(By.XPATH, 'ancestor::div[4]')
            phone_number = phone_button.find_element(By.CSS_SELECTOR, "div[class=\"Io6YTe fontBodyMedium kR99db \"]").text
        except:
            pass

        
        try:
            cleaned_number = re.sub(r'[+\s]', '', phone_number)
            duplicate_state = quickstart.test_duplicate(fence_name, cleaned_number)
            print(f'phone_number and duplicate state = ', cleaned_number, duplicate_state)
        except:
            duplicate_state = False

        if duplicate_state == False:

            try:
                website_button = driver.find_element(By.CSS_SELECTOR, 'img.Liguzb[src="//www.gstatic.com/images/icons/material/system_gm/1x/public_gm_blue_24dp.png"]').find_element(By.XPATH, 'ancestor::div[5]')
                website_domain = driver.find_element(By.CSS_SELECTOR, 'img.Liguzb[src="//www.gstatic.com/images/icons/material/system_gm/1x/public_gm_blue_24dp.png"]').find_element(By.XPATH, 'ancestor::div[3]')
                website_a = website_button.find_element(By.CSS_SELECTOR, "a[class=\"CsEnBe\"]")
                google_map_domain = website_domain.find_element(By.CSS_SELECTOR, "div[class=\"Io6YTe fontBodyMedium kR99db \"]").text
                google_map_website = website_a.get_attribute("href")
            except:
                pass

            print(f'google maps website = ', google_map_website)

            if  google_map_domain == "" or "business.site" in google_map_domain:
                website = getWebsiteIn.get_website_in(fence_name + " in " + city)
            
            if "facebook" in google_map_website:
                website = google_map_website
            else:
                if google_map_domain != "" and google_map_domain != "business.site":
                    website = "https://" + google_map_domain + "/"
                
            print(f'website = ', website)
            try:
                location_button = driver.find_element(By.CSS_SELECTOR, 'img.Liguzb[src="//www.gstatic.com/images/icons/material/system_gm/1x/place_gm_blue_24dp.png"]').find_element(By.XPATH, 'ancestor::div[3]')
                location_name = location_button.find_element(By.CSS_SELECTOR, "div[class=\"Io6YTe fontBodyMedium kR99db \"]").text
            except:
                pass
            
            print(f'location_name', location_name)


            try:
                rating_value_dom = driver.find_element(By.CSS_SELECTOR, "div[class=\"fontBodyMedium dmRWX\"]")
                rating_value_div = rating_value_dom.find_element(By.CSS_SELECTOR, "div[class=\"F7nice \"]")
                rating_value_span = rating_value_div.find_elements(By.TAG_NAME, "span")[0]
                rating_of_reviews = rating_value_span.find_elements(By.TAG_NAME, "span")[0].text
            except:
                pass
            
            print(f'rating of reviews = ', rating_of_reviews)

            print(f'Website link = ', website)
            
            if "facebook.com" in website:
                try:
                    fb_email, fb_phone, fb_address = facebook.get_email_from_facebook(website)
                    print(f'facebook contact info = ', fb_email, fb_phone, fb_address)
                    email = fb_email
                    if phone_number == "":
                        phone_number = fb_phone
                    if location_name == "":
                        location_name = fb_address
                    facebook_url = website
                except:
                    pass
            else:
                try:
                    start_time = time.time()

                    # Create a thread to execute the code
                    thread = threading.Thread(target=lambda: setattr(threading.currentThread(), 'result', getEmail.extract_company_contact_info(website)))
                    thread.start()

                    # Measure the execution time at 1-second intervals
                    while thread.is_alive():
                        elapsed_time = time.time() - start_time
                        time.sleep(1)
                        if elapsed_time > 60:
                            thread.cancel()
                            break
                    # Retrieve the result from the thread
                    try:
                        email = thread.result
                    except:
                        email = []
                        pass
                except:
                    pass
                            
                try:
                    facebook_url = getWebsiteIn.get_facebook_in(fence_name + " in " + city)
                except:
                    pass
                
                if len(email) == 0 and facebook_url != "":
                    try:
                        print("facebook link = ", facebook_url)
                        facebook_email, facebook_phone, facebook_address = facebook.get_email_from_facebook(facebook_url)
                        email = facebook_email
                        if phone_number == "":
                            phone_number = facebook_phone
                        if location_name == "":
                            location_name = facebook_address    
                        print(f"facebook contact info = ", phone_number, address)
                    except:
                        pass

            print(f'final email = ', email)

            try:
                
                columnCount = quickstart.getColumnCount()
                
                
                print(f'columnCount = ',columnCount)

                address = location_name.replace(", Vereinigte Staaten", "")
                address = location_name.replace(", Yhdysvallat", "")
                cleaned_number = re.sub(r'[+\s]', '', phone_number)
            
                email_string = " ".join(email)
                results = []
                results.append(str(columnCount + 1))
                results.append(fence_name)
                results.append(cleaned_number)
                results.append(address)
                results.append(website)
                results.append(facebook_url)
                results.append(email_string)
                results.append(rating_of_reviews)

                print(results)

                RANGE_DATA = f'fence_installers_data_texas!A{columnCount + 2}:H'
                quickstart.insert_data(RANGE_DATA, results)
            except:
                pass

            try:
                close_button = driver.find_element(By.CSS_SELECTOR, "button[class=\"VfPpkd-icon-LgbsSe yHy1rc eT1oJ mN1ivc\"]")
                close_span = close_button.find_element(By.CSS_SELECTOR, "span[class=\"VfPpkd-kBDsod\"]")
                close_span.click()
            except:
                pass
            sleep(2)

        else:
            try:
                close_button = driver.find_element(By.CSS_SELECTOR, "button[class=\"VfPpkd-icon-LgbsSe yHy1rc eT1oJ mN1ivc\"]")
                close_span = close_button.find_element(By.CSS_SELECTOR, "span[class=\"VfPpkd-kBDsod\"]")
                driver.execute_script("arguments[0].click();", close_span)
            except:
                pass
            sleep(2)
            
            continue
        
        sleep(4)

