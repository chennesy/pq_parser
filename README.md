## Parse ProQuest Metadata
This notebook includes a python function to parse newspaper articles downloaded from ProQuest Global Newsstream into one CSV file with metadata and full text (when full text is available). 

Created by Cody Hennesy and David Naughton (University of Minnesota, Twin Cities, Libraries). Email Cody (chennesy@umn.edu) with any questions. 

UPDATE (Feb 3, 2020):
ProQuest re-enabled the save as text option, so the parsing code included here is once again working. If you would like instead save your documents as HTML files, see instead [Jae Yeon Kim's ProQuest parser](https://github.com/jaeyk/proquest_parser).

See also: [Factiva parser](https://github.com/chennesy/factiva_parser)

~~NOTE: As of ~ September 15, 2019, ProQuest disabled the Save as "Text" option for multiple search results that this script requires to function. Requests are in to restore this functionality.~~

