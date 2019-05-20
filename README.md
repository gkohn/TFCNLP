# They Fight Crime NLP

Begin with the Merger.py file.

The purpose of this file is to check the formatting and combine the raw data for the male and female entries extracted by web scraping from the They Fight Crimes site.

To use this script save it in the same directory as the raw data in txt format.  Some slight modification may be needed to past in the directory name of the folder with the female and male raw data.  In the case of the version saved all of the female files were saved to a subfolder called "Female" and the male files were saved to a subfolder called "Male".  The output of this script will be a single male file and a single female file with all entries called "male_merge" and "female_merge" respectfully.

The second file, Sentiment.py uses the sentiment analysis to find the polarity of each of the male and female sentences.  The most positive and most negative are then combined in the original format.

The script ingests the combined male and female files ("male_merge" and "female_merge" if the Merger script was used to create).  The output of this script is two versions of the joke; one positive and one negative.  However, there may be multiple sentences with the same sentiment rating.  Only one is chosen to create the most positive and most negative.

The last file, Descriptors.py, return the top 10 descriptors that occur across both the male and female entries.

This scrip ingest male and female files, combines them into a master file, identifies all adjectives, and assess the frequency of each.  The output is a dictionary of to the top 10 descriptors.  As with the Sentiment script the existing function could be used for files of a different name though would require slight modification (file name and file path).
