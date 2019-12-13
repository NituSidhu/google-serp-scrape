# Scraping Google's Search Engine Results Page
*Note: Sometimes the meta-description does not line up with the meta-title or URL!*

This is a tool to help marketers easily track how their website is ranking on priority keywords, track movement when it comes to a specific search (keep an eye on competitors), and to collect information on keywords and phrases that are helping sites rank higher when it comes to Google.

This script will also save a .csv file everytime you execute it—using the search that you made and the day's date as the title. 

## How it Works
1. Run this script in your command line.
2. A new window will pop up asking you "What information would you like to gain today?"
3. Enter the term that's most helpful for your business (ex: "online therapy")
4. Results will instantly populate, any key will close the window. Don't worry as that same information will be stored as a .csv in your files. The title of the csv will contain what you searched with a "+" symbol used as a space. (ex: "online+therapy_serp_2019-12-12.csv")
5. Review your query, results contain the ranking, meta-title, url, and meta-description.

### Example of csv
![sample of google serp scrape](https://i.imgur.com/g1JVWan.png)

## What's Next
* Find out how to make sure the meta-description aligns with the meta-title and url. 
* Create a new column using regular expressions that extracts just the domain name.
* Create a graph that visualizes movement over time. Something along these lines: 
![sample graph for next steps](https://www.coretennis.net/ct/1/image/Players/Graphs/topPointsAtp.png)
