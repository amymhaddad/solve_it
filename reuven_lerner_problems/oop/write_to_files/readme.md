download information in JSON format about the 1,000 largest cities. I've put it on GitHub as:

    https://gist.github.com/reuven/77edbb0292901f35019f17edb9794358

but you should download the "raw" version, which is here:

    https://gist.githubusercontent.com/reuven/77edbb0292901f35019f17edb9794358/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json

(Please don't even try to write down this URL.)

After you retrieve the data and decode the JSON into Python data structures, I want you to create a CSV file. That file, which should have tabs as delimiters (rather than commas), should include the following data from the JSON file:
City name
State name
City population
City size rank
More specifically: You should write a function that takes a URL and a filename. It'll download the JSON information from the URL, and then write it to the file specified.
